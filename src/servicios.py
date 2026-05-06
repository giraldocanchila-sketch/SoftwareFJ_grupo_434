# Este archivo contendrá la clase abstracta Servicio y sus clases derivadas: 
# ReservaSala, AlquilerEquipo y AsesoriaEspecializada. 
# Cada clase representará un servicio específico que ofrece la empresa y tendrá sus propios 
# métodos para calcular costos, describir el servicio y validar parámetros.
from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError, ServicioNoDisponibleError

class Servicio(ABC):
    """
    Clase abstracta para definir un servicio.
    """
    def __init__(self, nombre, tarifa_base, disponible=True):
        self._nombre = nombre
        self._tarifa_base = tarifa_base
        self._disponible = disponible
        self.validar_parametros()

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    def validar_parametros(self):
        if not self._nombre:
            raise DatosInvalidosError("El nombre del servicio no puede estar vacío.")

        if self._tarifa_base <= 0:
            raise DatosInvalidosError("La tarifa base debe ser mayor a cero.")

        if not self._disponible:
            raise ServicioNoDisponibleError("El servicio no está disponible.")

    def mostrar_info(self):
        estado = "Disponible" if self._disponible else "No disponible"
        return f"{self._nombre} | Costo: ${self._tarifa_base:.2f} | Estado: {estado}"


# Clase ReservaSala
class ReservaSala(Servicio):
    def __init__(self, tarifa_base, capacidad, disponible=True):
        self.__capacidad = capacidad
        super().__init__("Reserva de Sala", tarifa_base, disponible)

    def validar_parametros(self):
        super().validar_parametros()

        if self.__capacidad <= 0:
            raise DatosInvalidosError("La capacidad de la sala debe ser mayor a cero.")

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        subtotal = self._tarifa_base * duracion
        total = subtotal + (subtotal * impuesto) - descuento

        if total < 0:
            raise DatosInvalidosError("El costo calculado no puede ser negativo.")

        return total

    def describir_servicio(self):
        return f"Reserva de sala con capacidad para {self.__capacidad} personas."


# Clase AlquilerEquipo
class AlquilerEquipo(Servicio):
    def __init__(self, tarifa_base, cantidad_equipos, disponible=True):
        self.__cantidad_equipos = cantidad_equipos
        super().__init__("Alquiler de Equipos", tarifa_base, disponible)

    def validar_parametros(self):
        super().validar_parametros()

        if self.__cantidad_equipos <= 0:
            raise DatosInvalidosError("La cantidad de equipos debe ser mayor a cero.")

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        subtotal = self._tarifa_base * duracion * self.__cantidad_equipos
        total = subtotal + (subtotal * impuesto) - descuento

        if total < 0:
            raise DatosInvalidosError("El costo calculado no puede ser negativo.")

        return total

    def describir_servicio(self):
        # Ya no usamos 'duracion', solo describimos el servicio
        return f"Alquiler de {self.__cantidad_equipos} equipo(s)."


# Clase AsesoriaEspecializada
class AsesoriaEspecializada(Servicio):
    def __init__(self, tarifa_base, especialidad, disponible=True):
        self.__especialidad = especialidad.strip()
        super().__init__("Asesoría Especializada", tarifa_base, disponible)

    def validar_parametros(self):
        super().validar_parametros()

        if not self.__especialidad:
            raise DatosInvalidosError("La especialidad de la asesoría no puede estar vacía.")

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        subtotal = self._tarifa_base * duracion
        total = subtotal + (subtotal * impuesto) - descuento

        if total < 0:
            raise DatosInvalidosError("El costo calculado no puede ser negativo.")

        return total

    def describir_servicio(self):
        return f"Asesoría especializada en {self.__especialidad}."