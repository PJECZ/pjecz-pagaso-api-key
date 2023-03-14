"""
Exceptions
"""


class PegasoAnyError(Exception):
    """Base exception class"""


class PegasoAuthenticationError(CitasAnyError):
    """Excepción porque fallo la autentificacion"""


class PegasoConnectionError(CitasAnyError):
    """Excepción porque no se pudo conectar"""


class PegasoEmptyError(CitasAnyError):
    """Excepción porque no hay resultados"""


class PegasoIsDeletedError(CitasAnyError):
    """Excepción porque esta eliminado"""


class PegasoMissingConfigurationError(CitasAnyError):
    """Excepción porque falta configuración"""


class PegasoNotExistsError(CitasAnyError):
    """Excepción porque no existe"""


class PegasoNotValidAnswerError(CitasAnyError):
    """Excepción porque la respuesta no es válida"""


class PegasoNotValidParamError(CitasAnyError):
    """Excepción porque un parámetro es inválido"""


class PegasoOutOfRangeParamError(CitasAnyError):
    """Excepción porque un parámetro esta fuera de rango"""


class PegasoRequestError(CitasAnyError):
    """Excepción porque falló el request"""


class PegasoTimeoutError(CitasAnyError):
    """Excepción porque se agoto el tiempo de espera"""


class PegasoUnknownError(CitasAnyError):
    """Excepción porque hubo un error desconocido"""
