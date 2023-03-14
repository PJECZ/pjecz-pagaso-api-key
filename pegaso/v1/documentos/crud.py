"""
Documentos, CRUD (read)
"""
from sqlalchemy.orm import Session

from lib.exceptions import PegasoNotExistsError, PegasoNotValidParamError, PegasoIsDeletedError
from lib.safe_string import safe_expediente

from .models import Documento


def get_documento_from_num_expediente(
    db: Session,
    num_expediente: str,
    juzgado_id: int,
) -> Documento:
    """Consultar un documento por su número de expediente"""
    num_expediente = safe_expediente(num_expediente)
    if num_expediente is None or num_expediente == "":
        raise PegasoNotValidParamError("No es válido el número de expediente")
    documento = db.query(Documento).filter_by(expediente=num_expediente).filter_by(auutoridad=juzgado_id).first()
    if documento is None:
        raise PegasoNotExistsError("No existe ese documento")
    if documento.estatus != "A":
        raise PegasoIsDeletedError("No es un documento activo, está eliminado")
    return documento
