"""
Autentificacion V1, rutas (paths)
"""
import os
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import APIKeyHeader

autentificacion = APIRouter(prefix="/v1/autentificacion", tags=["autentificacion"])

X_API_KEY = APIKeyHeader(name="X-Api-Key")


async def api_key_auth(api_key: str = Depends(X_API_KEY)):
    """Toma el header X-API-Key y lo valida con el valor de la variable de entorno"""
    API_KEY_ENV = os.environ.get("API_KEY", "")
    if API_KEY_ENV == "" or api_key != API_KEY_ENV:
        raise HTTPException(status_code=401, detail="No se puede autentificar")
