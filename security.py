from fastapi import Security, HTTPException, status, Depends
from fastapi.security import HTTPBearer, OAuth2PasswordBearer, APIKeyHeader
import jwt

# Security Schemes
security_bearer = HTTPBearer() # For JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # For OAuth2
api_key_header = APIKeyHeader(name="X-API-KEY") # For API Keys

def verify_jwt(auth=Depends(security_bearer)):
    # Logic to decode JWT
    return "authorized_user"

def verify_oauth2(token: str = Depends(oauth2_scheme)):
    # Logic to verify OAuth2 token
    return "authorized_client"

def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != "secret-key-123":
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return True