"""
Documentos, modelos
"""
from collections import OrderedDict
from sqlalchemy import Boolean, Column, Enum, Integer, String

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Documento(Base, UniversalMixin):
    """Documento SIBED"""

    TIPOS = OrderedDict(  # varchar(16)
        [
            ("NO DEFINIDO", "No Definido"),
            ("CUADERNILLO", "Cuadernillo"),
            ("ENCOMIENDA", "Encomienda"),
            ("EXHORTO", "Exhorto"),
            ("EXPEDIENTE", "Expediente"),
            ("EXPEDIENTILLO", "Expedientillo"),
            ("FOLIO", "Folio"),
            ("LIBRO", "Libro"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "sibed_documentos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    actor = Column(String(256), nullable=False)
    anio = Column(Integer, nullable=False)
    demandado = Column(String(256))
    expediente = Column(String(16), index=True, nullable=False)  # dígitos/YYYY-XXX
    juicio = Column(String(128))
    juzgado_id = Column(Integer, nullable=False)
    juzgado_origen_id = Column(Integer)
    fojas = Column(Integer, nullable=False)
    observaciones = Column(String(256))
    tipo = Column(
        Enum(*TIPOS, name="tipos", native_enum=False),
        index=True,
        nullable=False,
        default="NO DEFINIDO",
        server_default="NO DEFINIDO",
    )

    def __repr__(self):
        """Representación"""
        return f"<Documento SIBED> {self.id}"
