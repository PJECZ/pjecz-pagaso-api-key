"""
Documentos, CRUD (read)
"""
from sqlalchemy.orm import Session

from lib.exceptions import PegasoNotExistsError, PegasoNotValidParamError, PegasoIsDeletedError
from lib.safe_string import safe_expediente

from ...core.documentos.models import Documento


def get_documento_from_num_expediente(
    db: Session,
    juzgado_id: int,
    num_expediente: str,
) -> Documento:
    """Consultar un documento por su número de expediente"""

    # Validar el juzgado_id
    if juzgado_id <= 0:
        raise PegasoNotValidParamError("No es válido el número del juzgado")

    # Validar el número de expediente
    try:
        num_expediente = safe_expediente(num_expediente)
    except (ValueError, IndexError) as err:
        raise PegasoNotValidParamError("No es válido el número de expediente")
    if num_expediente is None or num_expediente == "":
        raise PegasoNotValidParamError("No es válido el número de expediente")

    # Consultar el documento
    documento = db.query(Documento).filter_by(expediente=num_expediente).filter_by(juzgado_id=juzgado_id).first()
    if documento is None:
        raise PegasoNotExistsError("No existe ese documento")
    if documento.estatus != "A":
        raise PegasoIsDeletedError("No es un documento activo, está eliminado")

    # Entregar
    return documento
