# Aquí se definirá una clase abstracta Entidad que servirá como base para otras clases importantes como 
# Cliente, Reserva, y cualquier otra entidad que se pueda agregar en el futuro.
# Esta clase abstracta no tendrá una implementación directa, sino que definirá la estructura general que deben seguir sus clases hijas.

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta general del sistema.
    Representa cualquier entidad principal: cliente, servicio o reserva.
    """

    @abstractmethod
    def mostrar_info(self):
        pass
    
# Comentario explicativo:
# Entidad es una base común que todas las demás clases (como Cliente o Reserva) deben seguir. 
# Los métodos descripcion y validar se definen en esta clase, pero se completan en las clases hijas.