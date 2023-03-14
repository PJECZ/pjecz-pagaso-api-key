"""
Juzgados Extintos, modelos
"""
from sqlalchemy import Column, Integer, String

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class JuzgadoExtinto(Base, UniversalMixin):
    """Juzgado Extinto"""

    # Nombre de la tabla
    __tablename__ = "arc_juzgados_extintos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    clave = Column(String(16), nullable=False, unique=True)
    descripcion_corta = Column(String(64), nullable=False, default="")
    descripcion = Column(String(256), nullable=False)

    # Hijos
    # arc_documentos = relationship("Documento", back_populates="arc_juzgado_origen")

    @property
    def nombre(self):
        """Junta clave : descripcion_corta"""
        return self.clave + " : " + self.descripcion_corta

    def __repr__(self):
        """Representación"""
        return f"<Juzgado-Extinto> {self.id}"
