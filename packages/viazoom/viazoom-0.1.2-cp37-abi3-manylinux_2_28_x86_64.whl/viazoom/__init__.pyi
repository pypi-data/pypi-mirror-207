from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class AccessTokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    scope: str

class AccessTokenErrorResponse(BaseModel):
    status: bool
    error_code: str
    error_message: str
    result: str

class ZoomOAuthClient:
    def __init__(self, account_id: str, client_id: str, client_secret: str) -> None:
        self.account_id = account_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.expires_in: Optional[int] = None
        self.expires_at: Optional[datetime] = None

    def get_access_token(self) -> str:
        """
        Gets a new access token from the Zoom OAuth API.

        Returns:
            The new access token as a string.
        """
        ...

    def __repr__(self) -> str:
        """
        Gets a string representation of the `ZoomOAuthClient` instance.

        Returns:
            The string representation of the instance.
        """
        ...
