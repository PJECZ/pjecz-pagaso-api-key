"""
Documentos V1, esquemas de pydantic
"""
from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class DocumentoOut(BaseModel):
    """Esquema para entregar documentos"""

    expediente: str | None
    anio: int | None
    actor: str | None
    demandado: str | None
    juicio: str | None
    juzgado_id: int | None
    juzgado_origen_id: int | None
    fojas: int | None
    observaciones: str | None
    tipo: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneDocumentoOut(DocumentoOut, OneBaseOut):
    """Esquema para entregar un Documento"""
