"""
Exceptions
"""


class PegasoAnyError(Exception):
    """Base exception class"""


class PegasoAuthenticationError(PegasoAnyError):
    """Excepción porque fallo la autentificacion"""


class PegasoConnectionError(PegasoAnyError):
    """Excepción porque no se pudo conectar"""


class PegasoEmptyError(PegasoAnyError):
    """Excepción porque no hay resultados"""


class PegasoIsDeletedError(PegasoAnyError):
    """Excepción porque esta eliminado"""


class PegasoMissingConfigurationError(PegasoAnyError):
    """Excepción porque falta configuración"""


class PegasoNotExistsError(PegasoAnyError):
    """Excepción porque no existe"""


class PegasoNotValidAnswerError(PegasoAnyError):
    """Excepción porque la respuesta no es válida"""


class PegasoNotValidParamError(PegasoAnyError):
    """Excepción porque un parámetro es inválido"""


class PegasoOutOfRangeParamError(PegasoAnyError):
    """Excepción porque un parámetro esta fuera de rango"""


class PegasoRequestError(PegasoAnyError):
    """Excepción porque falló el request"""


class PegasoTimeoutError(PegasoAnyError):
    """Excepción porque se agoto el tiempo de espera"""


class PegasoUnknownError(PegasoAnyError):
    """Excepción porque hubo un error desconocido"""
