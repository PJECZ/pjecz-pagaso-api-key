"""
Pegaso API OAuth2
"""
from fastapi import FastAPI

from config.settings import get_settings

from .v1.documentos.paths import documentos

settings = get_settings()


# FastAPI
app = FastAPI(
    title="Pegaso V1",
    description="API de consulta de la BD SIBED para brindar información de los documentos encontrados a otros sistemas.",
)

# Paths
app.include_router(documentos)


@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "Bienvenido a Pegaso API de consulta de BD de SIBED del Poder Judicial del Estado de Coahuila de Zaragoza."}
