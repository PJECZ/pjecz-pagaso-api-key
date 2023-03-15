"""
Documentos V1, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.authentications import get_current_active_user
from lib.database import get_db
from lib.exceptions import PegasoAnyError

from .crud import get_documento_from_num_expediente
from .schemas import OneDocumentoOut

documentos = APIRouter(prefix="/v1/documentos", tags=["documentos"])


@documentos.get("", response_model=OneDocumentoOut)
async def detalle_documento_params(
    juzgado_id: int,
    num_expediente: str,
    current_user: bool = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Detalle de un documento a partir de su número de expediente y juzgado"""

    # Si current_user es False, entonces no se autentifico
    if not current_user:
        raise HTTPException(status_code=403, detail="No autentificado")

    # Obtener documento
    try:
        documento = get_documento_from_num_expediente(db=db, num_expediente=num_expediente, juzgado_id=juzgado_id)
    except PegasoAnyError as error:
        return OneDocumentoOut(success=False, message=str(error))

    # Entregar documento
    return OneDocumentoOut.from_orm(documento)
