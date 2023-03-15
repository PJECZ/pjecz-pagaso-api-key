"""
Autentificaciones
"""
import re

from fastapi.security.api_key import APIKeyHeader
from fastapi import HTTPException, Depends
from starlette.status import HTTP_403_FORBIDDEN

from config.settings import get_settings
from lib.exceptions import PegasoAuthenticationError

API_KEY_REGEXP = r"^\w+\.\w+\.\w+$"
X_API_KEY = APIKeyHeader(name="X-Api-Key")


def authenticate_user(
    api_key: str,
) -> bool:
    """Autentificar por api_key"""

    # Configuracion
    settings = get_settings()

    # Validar con expresion regular
    if re.match(API_KEY_REGEXP, api_key) is None:
        raise PegasoAuthenticationError("No paso la validacion por expresion regular")

    # Validar que coincida el API Key
    if api_key != settings.usuario_api_key:
        raise PegasoAuthenticationError("No es igual la api_key")

    # Entregar verdadero si es valida
    return True


async def get_current_active_user(
    api_key: str = Depends(X_API_KEY),
) -> bool:
    """Obtener el usuario activo actual"""

    # Try-except
    try:
        resultado_autentificacion = authenticate_user(api_key)
    except PegasoAuthenticationError as error:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail=str(error)) from error

    # Entregar
    return resultado_autentificacion
