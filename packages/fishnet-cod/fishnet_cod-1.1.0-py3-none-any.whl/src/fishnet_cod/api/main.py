import asyncio
import logging
import os
from os import listdir
from typing import List, Optional, Dict, Union, Tuple

import pandas as pd  # type: ignore
from aars.utils import PageableRequest, PageableResponse
from aleph.sdk.exceptions import BadSignatureError  # type: ignore
from aleph_message.models import PostMessage  # type: ignore

from .api_model import (  # type: ignore
    UploadTimeseriesRequest,
    UploadDatasetRequest,
    UploadAlgorithmRequest,
    RequestExecutionRequest,
    RequestExecutionResponse,
    PutUserInfo,
    PutViewRequest,
    PutViewResponse,
    Attribute,
    NotificationType,
    Notification,
    MultiplePermissions,
    FungibleAssetStandard,
    UploadDatasetTimeseriesRequest,
    UploadDatasetTimeseriesResponse,
    DatasetResponse,
    PostPermission,
    MessageResponse,
    TokenChallengeResponse,
    BearerTokenResponse,
    ApprovePermissionsResponse,
    DenyPermissionsResponse,
)
from .auth import AuthTokenManager
from .routers.timeseries import upload_timeseries
from .utils import unique
from ..core.constants import API_MESSAGE_FILTER
from ..core.model import (
    Timeseries,
    UserInfo,
    Algorithm,
    Execution,
    Permission,
    PermissionStatus,
    ExecutionStatus,
    Result,
    Dataset,
    Granularity,
    View,
)
from ..core.session import initialize_aars

logger = logging.getLogger("uvicorn")

logger.debug("import aleph_client")
from aleph.sdk.vm.app import AlephApp  # type: ignore

logger.debug("import aars")
from aars import AARS, Record

logger.debug("import fastapi")
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

logger.debug("import project modules")

logger.debug("imports done")

http_app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/challenge")

origins = ["*"]

http_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = AlephApp(http_app=http_app)
global aars_client, auth_manager
aars_client: AARS
auth_manager: AuthTokenManager


async def re_index():
    logger.info(f"API re-indexing channel {AARS.channel}")
    await asyncio.wait_for(AARS.sync_indices(), timeout=None)
    logger.info("API re-indexing done")


@app.on_event("startup")
async def startup():
    global aars_client, auth_manager
    aars_client = initialize_aars()
    auth_manager = AuthTokenManager()
    await re_index()


@app.get("/")
async def index():
    if os.path.exists("/opt/venv"):
        opt_venv = list(listdir("/opt/venv"))
    else:
        opt_venv = []
    return {
        "vm_name": "fishnet_api",
        "endpoints": [
            "/docs",
        ],
        "files_in_volumes": {
            "/opt/venv": opt_venv,
        },
    }


@app.put("/datasets/upload")
async def upload_dataset(dataset: UploadDatasetRequest) -> Dataset:
    """
    Upload a dataset.
    If an `id_hash` is provided, it will update the dataset with that id.
    """
    if dataset.ownsAllTimeseries:
        timeseries = await Timeseries.fetch(dataset.timeseriesIDs).all()
        dataset.ownsAllTimeseries = all(
            [ts.owner == dataset.owner for ts in timeseries]
        )
    if dataset.id_hash is not None:
        old_dataset = await Dataset.fetch(dataset.id_hash).first()
        if old_dataset is not None:
            if old_dataset.owner != dataset.owner:
                raise HTTPException(
                    status_code=403,
                    detail="Cannot overwrite dataset that is not owned by you",
                )
            old_dataset.name = dataset.name
            old_dataset.desc = dataset.desc
            old_dataset.timeseriesIDs = dataset.timeseriesIDs
            old_dataset.ownsAllTimeseries = dataset.ownsAllTimeseries
            return await old_dataset.save()
    return await Dataset(**dataset.dict()).save()


@app.post("/datasets/upload/timeseries")
async def upload_dataset_timeseries(
    upload_dataset_timeseries_request: UploadDatasetTimeseriesRequest,
) -> UploadDatasetTimeseriesResponse:
    """
    Upload a dataset and timeseries at the same time.
    """
    if upload_dataset_timeseries_request.dataset.id_hash is not None:
        raise HTTPException(
            status_code=400,
            detail="Cannot use this POST endpoint to update a dataset. Use PUT /datasets/upload instead.",
        )
    if any([ts.id_hash is None for ts in upload_dataset_timeseries_request.timeseries]):
        raise HTTPException(
            status_code=400,
            detail="Cannot use this POST endpoint to update timeseries. Use PUT /timeseries/upload instead.",
        )
    timeseries = await upload_timeseries(
        req=UploadTimeseriesRequest(
            timeseries=upload_dataset_timeseries_request.timeseries
        )
    )
    dataset = await upload_dataset(req=upload_dataset_timeseries_request.dataset)
    return UploadDatasetTimeseriesResponse(
        dataset=dataset,
        timeseries=[ts for ts in timeseries if not isinstance(ts, BaseException)],
    )


def get_timestamps_by_granularity(
    start: int, end: int, granularity: Granularity
) -> List[int]:
    """
    Get timestamps by granularity
    :param start: start timestamp
    :param end: end timestamp
    :param granularity: granularity
    :return: list of timestamps
    """
    if granularity == Granularity.DAY:
        interval = 60 * 5
    elif granularity == Granularity.WEEK:
        interval = 60 * 15
    elif granularity == Granularity.MONTH:
        interval = 60 * 60
    elif granularity == Granularity.THREE_MONTHS:
        interval = 60 * 60 * 3
    else:  # granularity == Granularity.YEAR:
        interval = 60 * 60 * 24
    timestamps = []
    for i in range(start, end, interval):
        timestamps.append(i)
    return timestamps


@app.put("/datasets/{dataset_id}/views")
async def generate_view(
    dataset_id: str, view_params: List[PutViewRequest]
) -> PutViewResponse:
    # get the dataset
    dataset = await Dataset.fetch(dataset_id).first()
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    view_requests = []
    for view_req in view_params:
        # get all the timeseries
        timeseries = await Timeseries.fetch(view_req.timeseriesIDs).all()
        view_values = {}
        for ts in timeseries:
            # normalize and round values
            values = [p[1] for p in ts.data]
            ts.min = min(values)
            ts.max = max(values)
            normalized = [
                (p[0], round((p[1] - ts.min) / (ts.max - ts.min)), 2) for p in ts.data
            ]
            # drop points according to granularity
            thinned = []
            i = 0  # cursor for normalized entries
            timestamps = get_timestamps_by_granularity(
                view_req.startTime, view_req.endTime, view_req.granularity
            )
            # append each point that is closest to the timestamp
            for timestamp in timestamps:
                while i < len(normalized) and normalized[i][0] < timestamp:
                    i += 1
                if i == len(normalized):
                    break
                if i == 0:
                    thinned.append(normalized[i])
                else:
                    if abs(normalized[i][0] - timestamp) < abs(
                        normalized[i - 1][0] - timestamp
                    ):
                        thinned.append(normalized[i])
                    else:
                        thinned.append(normalized[i - 1])

            view_values[ts.id_hash] = thinned

        # prepare view request
        view_requests.append(
            View(
                id_hash=view_req.id_hash,
                startTime=view_req.startTime,
                endTime=view_req.endTime,
                granularity=view_req.granularity,
                values=view_values,
            ).save()
        )

    # save all records
    views = await asyncio.gather(*view_requests)
    dataset.views = [view.id_hash for view in views]
    await dataset.save()

    return PutViewResponse(dataset=dataset, views=views)


@app.put("/datasets/{dataset_id}/available/{available}")
async def set_dataset_available(dataset_id: str, available: bool) -> Dataset:
    """
    Set a dataset to be available or not. This will also update the status of all
    executions that are waiting for permission on this dataset.
    param `dataset_id':put the dataset hash here
    param 'available':put the Boolean value
    """

    requests = []
    dataset = await Dataset.fetch(dataset_id).first()
    if not dataset:
        raise HTTPException(status_code=404, detail="No Dataset found")
    dataset.available = available
    requests.append(dataset.save())

    ts_list = await Timeseries.fetch(dataset.timeseriesIDs).all()
    if not ts_list:
        raise HTTPException(status_code=424, detail="No Timeseries found")

    for rec in ts_list:
        if rec.available != available:
            rec.available = available
            requests.append(rec.save())
    executions_records = await Execution.fetch(dataset_id).all()
    for rec in executions_records:
        if rec.status == ExecutionStatus.PENDING:
            rec.status = ExecutionStatus.DENIED
            requests.append(rec.save())

    await asyncio.gather(*requests)
    return dataset


@app.get("/executions")
async def get_executions(
    dataset_id: Optional[str] = None,
    by: Optional[str] = None,
    status: Optional[ExecutionStatus] = None,
    page: int = 1,
    page_size: int = 20,
) -> List[Execution]:
    execution_requests: Union[PageableRequest[Execution], PageableResponse[Execution]]
    if dataset_id or by or status:
        execution_requests = Execution.where_eq(
            datasetID=dataset_id, owner=by, status=status
        )
    else:
        execution_requests = Execution.fetch_objects()
    return await execution_requests.page(page=page, page_size=page_size)


async def request_permissions(
    dataset: Dataset, execution: Execution
) -> Tuple[List[Permission], List[Permission], List[Timeseries]]:
    """
    Request permissions for a dataset given an execution.

    Args:
        dataset: The dataset to request permissions for.
        execution: The execution requesting permissions.

    Returns:
        A tuple of lists of permissions to create, permissions to update, and timeseries that are unavailable.
    """
    timeseries = await Timeseries.fetch(dataset.timeseriesIDs).all()
    requested_permissions = [
        Permission.where_eq(timeseriesID=tsID, requestor=execution.owner).first()
        for tsID in dataset.timeseriesIDs
    ]
    permissions: List[Permission] = list(await asyncio.gather(*requested_permissions))
    ts_permission_map: Dict[str, Permission] = {
        permission.timeseriesID: permission for permission in permissions if permission
    }
    create_permissions_requests = []
    update_permissions_requests = []
    unavailable_timeseries = []
    for ts in timeseries:
        if ts.owner == execution.owner:
            continue
        if not ts.available:
            unavailable_timeseries.append(ts)
        if timeseries:
            continue
        if ts.id_hash not in ts_permission_map:
            create_permissions_requests.append(
                Permission(
                    datasetID=dataset.id_hash,
                    timeseriesID=ts.id_hash,
                    algorithmID=execution.algorithmID,
                    owner=ts.owner,
                    requestor=execution.owner,
                    status=PermissionStatus.REQUESTED,
                    executionCount=0,
                    maxExecutionCount=-1,
                ).save()
            )
        else:
            permission = ts_permission_map[ts.id_hash]
            needs_update = False
            if permission.status == PermissionStatus.DENIED:
                permission.status = PermissionStatus.REQUESTED
                needs_update = True
            if (
                permission.maxExecutionCount
                and permission.maxExecutionCount <= permission.executionCount
            ):
                permission.maxExecutionCount = permission.executionCount + 1
                permission.status = PermissionStatus.REQUESTED
                needs_update = True
            if needs_update:
                update_permissions_requests.append(permission.save())
    created_permissions: List[Permission] = list(
        await asyncio.gather(*create_permissions_requests)
    )
    updated_permissions: List[Permission] = list(
        await asyncio.gather(*update_permissions_requests)
    )
    return created_permissions, updated_permissions, unavailable_timeseries


@app.post("/executions/request")
async def request_execution(
    execution_request: RequestExecutionRequest,
) -> RequestExecutionResponse:
    """
    This endpoint is used to request an execution.
    If the user needs some permissions, the timeseries for which the user needs permissions are returned and
    the execution status is set to "requested". The needed permissions are also being requested. As soon as the
    permissions are granted, the execution is automatically executed.
    If some timeseries are not available, the execution is "denied" and the execution as well as the
    unavailable timeseries are returned.
    If the user has all permissions, the execution is started and the execution is returned.
    """
    execution = Execution(**execution_request.dict())
    if not execution.owner:
        raise HTTPException(status_code=400, detail="No owner specified")
    dataset = await Dataset.fetch(execution.datasetID).first()
    if not dataset:
        raise HTTPException(status_code=400, detail="Dataset not found")

    if dataset.owner == execution.owner and dataset.ownsAllTimeseries:
        execution.status = ExecutionStatus.PENDING
        return RequestExecutionResponse(
            execution=await execution.save(),
            permissionRequests=None,
            unavailableTimeseries=None,
        )

    (
        created_permissions,
        updated_permissions,
        unavailable_timeseries,
    ) = await request_permissions(dataset, execution)

    if unavailable_timeseries:
        execution.status = ExecutionStatus.DENIED
        return RequestExecutionResponse(
            execution=await execution.save(),
            unavailableTimeseries=unavailable_timeseries,
            permissionRequests=None,
        )
    if created_permissions or updated_permissions:
        new_permission_requests = created_permissions + updated_permissions
        execution.status = ExecutionStatus.REQUESTED
        return RequestExecutionResponse(
            execution=await execution.save(),
            unavailableTimeseries=None,
            permissionRequests=new_permission_requests,
        )
    else:
        execution.status = ExecutionStatus.PENDING
        return RequestExecutionResponse(
            execution=await execution.save(),
            unavailableTimeseries=None,
            permissionRequests=None,
        )


@app.put("/permissions/approve")
async def approve_permissions(
    permission_hashes: List[str],
) -> ApprovePermissionsResponse:
    """
    Approve permission.
    This EndPoint will approve a list of permissions by their item hashes
    If an 'id_hashes' is provided, it will change all the Permission status
    to 'Granted'.
    """
    # TODO: Check if the user is the authorizer of the permissions
    permissions = await Permission.fetch(permission_hashes).all()
    if not permissions:
        return ApprovePermissionsResponse(
            updatedPermissions=[],
            triggeredExecutions=[],
        )

    # grant permissions
    dataset_ids = []
    permission_requests = []
    for permission in permissions:
        permission.status = PermissionStatus.GRANTED
        dataset_ids.append(permission.datasetID)
        permission_requests.append(permission.save())
    await asyncio.gather(*permission_requests)

    # get all requested executions and their datasets
    execution_requests = []
    dataset_requests = []
    for dataset_id in unique(dataset_ids):
        execution_requests.append(
            Execution.where_eq(
                datasetID=dataset_id, status=ExecutionStatus.REQUESTED
            ).all()
        )
        dataset_requests.append(Dataset.fetch(dataset_id).first())

    dataset_executions_map = {
        executions[0].datasetID: executions
        for executions in await asyncio.gather(*execution_requests)
        if executions and isinstance(executions[0], Execution)
    }

    # trigger executions if all permissions are granted
    execution_requests = []
    for dataset in await asyncio.gather(*dataset_requests):
        executions = dataset_executions_map.get(dataset.id_hash, [])
        for execution in executions:
            # TODO: Check if more efficient way to do this
            (
                created_permissions,
                updated_permissions,
                unavailable_timeseries,
            ) = await request_permissions(dataset, execution)
            if not created_permissions and not updated_permissions:
                execution.status = ExecutionStatus.PENDING
                execution_requests.append(await execution.save())
    triggered_executions = list(await asyncio.gather(*execution_requests))

    return ApprovePermissionsResponse(
        updatedPermissions=permissions,
        triggeredExecutions=triggered_executions,
    )


@app.put("/permissions/deny")
async def deny_permissions(permission_hashes: List[str]) -> DenyPermissionsResponse:
    """
    Deny permission.
    This EndPoint will deny a list of permissions by their item hashes
    If an `id_hashes` is provided, it will change all the Permission status
    to 'Denied'.
    """
    # TODO: Check if the user is the authorizer of the permissions
    permissions = await Permission.fetch(permission_hashes).all()
    if not permissions:
        return DenyPermissionsResponse(
            updatedPermissions=[],
            deniedExecutions=[],
        )

    # deny permissions and get dataset ids
    dataset_ids = []
    permission_requests = []
    for permission in permissions:
        permission.status = PermissionStatus.DENIED
        dataset_ids.append(permission.datasetID)
        permission_requests.append(permission.save())
    await asyncio.gather(*permission_requests)

    # get requested executions
    execution_requests = []
    for dataset_id in unique(dataset_ids):
        execution_requests.append(
            Execution.where_eq(
                datasetID=dataset_id, status=ExecutionStatus.REQUESTED
            ).all()
        )

    # deny executions
    execution_requests = []
    for executions in await asyncio.gather(*execution_requests):
        for execution in executions:
            execution.status = ExecutionStatus.DENIED
            execution_requests.append(await execution.save())
    denied_executions = list(await asyncio.gather(*execution_requests))

    return DenyPermissionsResponse(
        updatedPermissions=permissions, deniedExecutions=denied_executions
    )


@app.get("/results/{result_id}")
async def get_result(result_id: str) -> Optional[Result]:
    return await Result.fetch(result_id).first()


@app.delete("/clear/records")
async def empty_records() -> MessageResponse:
    await UserInfo.forget_all()
    await Timeseries.forget_all()
    await View.forget_all()
    await Dataset.forget_all()
    await Algorithm.forget_all()
    await Execution.forget_all()
    await Permission.forget_all()
    await Result.forget_all()
    return MessageResponse(response="All records are cleared")


@app.get("/views")
async def get_views(view_ids: List[str]) -> List[View]:
    return await View.fetch(view_ids).all()


@app.post("/event")
async def event(event: PostMessage):
    await fishnet_event(event)


@app.event(filters=API_MESSAGE_FILTER)
async def fishnet_event(event: PostMessage):
    record: Optional[Record]
    print("fishnet_event", event)
    if event.content.type in [
        "Execution",
        "Permission",
        "Dataset",
        "Timeseries",
        "Algorithm",
    ]:
        if Record.is_indexed(event.item_hash):
            return
        cls: Record = globals()[event.content.type]
        record = await cls.from_post(event)
    else:  # amend
        if Record.is_indexed(event.content.ref):
            return
        record = await Record.fetch(event.content.ref).first()
    assert record
    for inx in record.get_indices():
        inx.add_record(record)
