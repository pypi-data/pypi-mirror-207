from aleph.sdk.exceptions import BadSignatureError
from fastapi import HTTPException

from fishnet_cod.api.api_model import TokenChallengeResponse, BearerTokenResponse
from fishnet_cod.api.auth import SupportedChains, NotAuthorizedError
from fishnet_cod.api.main import app


@app.post("/auth/challenge")
async def create_challenge(
    pubkey: str, chain: SupportedChains
) -> TokenChallengeResponse:
    global auth_manager
    challenge = auth_manager.get_challenge(pubkey=pubkey, chain=chain)
    return TokenChallengeResponse(
        pubkey=challenge.pubkey,
        chain=challenge.chain,
        challenge=challenge.challenge,
        valid_til=challenge.valid_til,
    )


@app.post("/auth/solve")
async def solve_challenge(
    pubkey: str, chain: SupportedChains, signature: str
) -> BearerTokenResponse:
    global auth_manager
    try:
        auth = auth_manager.solve_challenge(
            pubkey=pubkey, chain=chain, signature=signature
        )
        return BearerTokenResponse(
            pubkey=auth.pubkey,
            chain=auth.chain,
            token=auth.token,
            valid_til=auth.valid_til,
        )
    except (BadSignatureError, ValueError):
        raise HTTPException(403, "Challenge failed")
    except TimeoutError:
        raise HTTPException(403, "Challenge timeout")


@app.post("/auth/refresh")
async def refresh_token(token: str) -> BearerTokenResponse:
    global auth_manager
    try:
        auth = auth_manager.refresh_token(token)
    except TimeoutError:
        raise HTTPException(403, "Token expired")
    except NotAuthorizedError:
        raise HTTPException(403, "Not authorized")
    return BearerTokenResponse(
        pubkey=auth.pubkey, chain=auth.chain, token=auth.token, valid_til=auth.valid_til
    )


@app.post("/auth/logout")
async def logout(token: str):
    global auth_manager
    auth_manager.remove_token(token)