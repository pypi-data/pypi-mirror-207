import asyncio
from typing import Optional, List, Union

from aars.utils import PageableRequest, PageableResponse
from fastapi import HTTPException

from fishnet_cod.api.api_model import DatasetResponse, FungibleAssetStandard, Attribute
from fishnet_cod.api.main import app
from fishnet_cod.core.model import Dataset, Permission, DatasetPermissionStatus, PermissionStatus


@app.get("/datasets")
async def get_datasets(
    id: Optional[str] = None,
    view_as: Optional[str] = None,
    by: Optional[str] = None,
    page: int = 1,
    page_size: int = 20,
) -> List[DatasetResponse]:
    """
    Get all datasets. Returns a list of tuples of datasets and their permission status for the given `view_as` user.
    If `view_as` is not given, the permission status will be `none` for all datasets.
    If `id` is given, it will return the dataset with that id.
    If `by` is given, it will return all datasets owned by that user.
    """
    dataset_resp: Union[PageableRequest, PageableResponse]
    if id:
        datasets_resp = Dataset.fetch(id)
    elif by:
        datasets_resp = Dataset.where_eq(owner=by)
    else:
        datasets_resp = Dataset.fetch_objects()
    datasets = await datasets_resp.page(page=page, page_size=page_size)

    if view_as:
        ts_ids = []
        for rec in datasets:
            ts_ids.extend(rec.timeseriesIDs)
        ts_ids_unique = list(set(ts_ids))

        req = [
            Permission.where_eq(timeseriesID=ts_id, authorizer=view_as).all()
            for ts_id in ts_ids_unique
        ]
        resp = await asyncio.gather(*req)
        permissions = [item for sublist in resp for item in sublist]

        returned_datasets: List[DatasetResponse] = []
        for rec in datasets:
            dataset_permissions = []
            for ts_id in rec.timeseriesIDs:
                dataset_permissions.extend(
                    list(filter(lambda x: x.timeseriesID == ts_id, permissions))
                )
            if not dataset_permissions:
                returned_datasets.append(
                    DatasetResponse(
                        **rec.dict(),
                        permission_status=DatasetPermissionStatus.NOT_REQUESTED,
                    )
                )
                continue

            permission_status = [perm_rec for perm_rec in dataset_permissions]
            if all(status == PermissionStatus.GRANTED for status in permission_status):
                returned_datasets.append(
                    DatasetResponse(
                        **rec.dict(), permission_status=DatasetPermissionStatus.GRANTED
                    )
                )
            elif PermissionStatus.DENIED in permission_status:
                returned_datasets.append(
                    DatasetResponse(
                        **rec.dict(), permission_status=DatasetPermissionStatus.DENIED
                    )
                )
            elif PermissionStatus.REQUESTED in permission_status:
                returned_datasets.append(
                    DatasetResponse(
                        **rec.dict(),
                        permission_status=DatasetPermissionStatus.REQUESTED,
                    )
                )
        return returned_datasets
    else:
        return [
            DatasetResponse(**rec.dict(), permission_status=None) for rec in datasets
        ]


@app.get("/datasets/{dataset_id}/permissions")
async def get_dataset_permissions(dataset_id: str) -> List[Permission]:
    """
    Get all granted permissions for a given dataset.
    """
    dataset = await Dataset.fetch(dataset_id).first()
    if not dataset:
        raise HTTPException(status_code=404, detail="No Dataset found")
    ts_ids = [ts_id for ts_id in dataset.timeseriesIDs]
    matched_permission_records = [
        Permission.where_eq(timeseriesID=ts_id, status=PermissionStatus.GRANTED).all()
        for ts_id in ts_ids
    ]
    records = await asyncio.gather(*matched_permission_records)
    permission_records = [element for row in records for element in row if element]

    return permission_records


@app.get("/datasets/{dataset_id}/metaplex")
async def get_dataset_metaplex_dataset(dataset_id: str) -> FungibleAssetStandard:
    """
    Get the metaplex metadata for a given dataset.
    """
    dataset = await Dataset.fetch(dataset_id).first()
    if dataset is None:
        raise HTTPException(status_code=404, detail="Dataset not found")
    assert dataset.id_hash
    return FungibleAssetStandard(
        name=dataset.name,
        symbol=dataset.id_hash,
        description=dataset.desc,
        # TODO: Generate chart image
        image="https://ipfs.io/ipfs/Qma2eje8yY57pNuaUyo4dsjtB9xwPz5yV6pCbK2PxpjUzo",
        animation_url=None,
        external_url=f"http://localhost:5173/data/{dataset.id_hash}/details",
        attributes=[
            Attribute(trait_type="Owner", value=dataset.owner),
            Attribute(trait_type="Last Updated", value=dataset.timestamp),
            Attribute(trait_type="Columns", value=str(len(dataset.timeseriesIDs))),
        ],
    )