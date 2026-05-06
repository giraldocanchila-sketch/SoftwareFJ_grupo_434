# En este módulo se incluirá la clase Reserva, que gestionará la relación entre los clientes 
# y los servicios, así como la duración y estado de cada reserva. 
# Esta clase también implementará los métodos para confirmar, cancelar y procesar reservas.

# src/reservas.py
from excepciones import DatosInvalidosError, OperacionNoPermitidaError
from servicios import Servicio
from clientes import Cliente

class Reserva:
    """
    Clase Reserva.
    Integra cliente, servicio, duración y estado.
    """

    def __init__(self, cliente, servicio, duracion):
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__validar_reserva()

    def __validar_reserva(self):
        if not isinstance(self.__cliente, Cliente):
            raise DatosInvalidosError("La reserva debe tener un cliente válido.")

        if not isinstance(self.__servicio, Servicio):
            raise DatosInvalidosError("La reserva debe tener un servicio válido.")

        if self.__duracion <= 0:
            raise DatosInvalidosError("La duración de la reserva debe ser mayor a cero.")

    def confirmar(self):
        if self.__estado != "Pendiente":
            raise OperacionNoPermitidaError("Solo se pueden confirmar reservas pendientes.")
        self.__estado = "Confirmada"
        return "Reserva confirmada correctamente."

    def cancelar(self):
        if self.__estado == "Procesada":
            raise OperacionNoPermitidaError("No se puede cancelar una reserva ya procesada.")
        if self.__estado == "Cancelada":
            raise OperacionNoPermitidaError("La reserva ya se encuentra cancelada.")
        self.__estado = "Cancelada"
        return "Reserva cancelada correctamente."

    def procesar(self):
        if self.__estado == "Cancelada":
            raise OperacionNoPermitidaError("No se puede procesar una reserva cancelada.")
        if self.__estado == "Pendiente":
            raise OperacionNoPermitidaError("La reserva debe estar confirmada antes de procesarse.")
        self.__estado = "Procesada"
        costo = self.__servicio.calcular_costo(self.__duracion, impuesto=0.19, descuento=0)
        return f"Reserva procesada correctamente. Costo total con IVA: ${costo:,.0f}"

    def mostrar_info(self):
        """
        Método para mostrar la información de la reserva.
        """
        return (
            f"Cliente: {self.__cliente.get_nombre()} | "
            f"Servicio: {self.__servicio.mostrar_info()} | "
            f"Duración: {self.__duracion} hora(s) | "
            f"Estado: {self.__estado}"
        )
