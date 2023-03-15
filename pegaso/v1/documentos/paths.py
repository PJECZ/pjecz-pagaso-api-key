"""
Documentos V1, rutas (paths)
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.exceptions import PegasoAnyError

from .crud import get_documento_from_num_expediente
from .schemas import OneDocumentoOut

documentos = APIRouter(prefix="/v1/documentos", tags=["documentos"])


@documentos.get("/{juzgado_id}/{num_expediente}", response_model=OneDocumentoOut)
async def detalle_documento(juzgado_id: int, num_expediente: str, db: Session = Depends(get_db)):
    """Detalle de un documento a partir de su número de expediente y juzgado"""
    try:
        documento = get_documento_from_num_expediente(db=db, num_expediente=num_expediente, juzgado_id=juzgado_id)
    except PegasoAnyError as error:
        return OneDocumentoOut(success=False, message=str(error))
    return OneDocumentoOut.from_orm(documento)
