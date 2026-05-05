# En este módulo se definirán las excepciones personalizadas, como DatosInvalidosError y 
# ServicioNoDisponibleError, que se lanzarán en situaciones donde los datos no sean válidos o un servicio no esté disponible. 
# Estas excepciones permitirán manejar errores específicos de una manera más controlada y eficiente.

# Aquí definimos nuestras propias excepciones para casos específicos en el sistema
class ErrorSistema(Exception):
    """Excepción base del sistema Software FJ."""
    pass # Esta clase es la base para todas las excepciones personalizadas en nuestro sistema.


class DatosInvalidosError(ErrorSistema):
    """Se lanza cuando los datos ingresados no cumplen las validaciones."""
    pass # Esta excepción se utiliza para indicar que los datos proporcionados no son válidos, como un formato incorrecto o valores fuera de rango.


class ServicioNoDisponibleError(ErrorSistema):
    """Se lanza cuando un servicio no está disponible."""
    pass # Esta excepción se utiliza para indicar que un servicio o recurso no está disponible, como un servidor caído o una función que no puede ser ejecutada en ese momento.


class OperacionNoPermitidaError(ErrorSistema):
    """Se lanza cuando una operación no puede ejecutarse por el estado actual."""
    pass # Esta excepción se utiliza para indicar que una operación no puede realizarse debido a las condiciones actuales del sistema, como intentar acceder a un recurso que está bloqueado o realizar una acción que no está permitida en el estado actual.
#Comentario explicativo:
# Aquí creamos excepciones propias para manejar errores específicos de nuestro sistema. 
# Son como mensajes personalizados que nos ayudan a identificar qué salió mal.