import secrets

from fastapi import Security
from fastapi.security.api_key import APIKeyHeader
from starlette.exceptions import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_503_SERVICE_UNAVAILABLE

from app.core.config import (
    API_KEY,
    API_KEY_NAME,
)

api_key_header_auth = APIKeyHeader(name=API_KEY_NAME, auto_error=True)


async def authenticated(api_key_header: str = Security(api_key_header_auth)):
    if not API_KEY:
        # Fail closed: refuse to authorize when the server has no key configured,
        # rather than accepting any (or empty) header value.
        raise HTTPException(
            status_code=HTTP_503_SERVICE_UNAVAILABLE,
            detail="API key is not configured on the server",
        )
    # Use a constant-time comparison to avoid leaking information via timing.
    if not secrets.compare_digest(api_key_header, API_KEY):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
