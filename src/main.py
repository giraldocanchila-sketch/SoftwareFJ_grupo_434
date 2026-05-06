# Este será el archivo principal que ejecutará el sistema. A través de este script, el usuario 
# podrá interactuar con el programa para registrar clientes, crear servicios y realizar reservas. 
# También manejará las excepciones y registrará los resultados de las operaciones.

from clientes import Cliente  # Importamos la clase Cliente
from servicios import ReservaSala  # Importamos el servicio ReservaSala
from reservas import Reserva  # Importamos la clase Reserva

def main():
    cliente = Cliente("Juan Pérez", "juan@example.com", "123456789")  # Creamos un cliente con datos ficticios
    servicio = ReservaSala()  # Creamos un servicio de tipo ReservaSala
    reserva = Reserva(cliente, servicio, 2)  # Creamos una reserva para el cliente y el servicio con duración 2 horas
    
    print(f"Estado de la reserva: {reserva.estado}")  # Imprimimos el estado inicial de la reserva
    reserva.confirmar()  # Confirmamos la reserva
    print(f"Estado de la reserva después de confirmación: {reserva.estado}")  # Imprimimos el nuevo estado de la reserva

if __name__ == "__main__":  # Este bloque se ejecuta si el archivo es ejecutado directamente
    main()  # Llamamos a la función principal

# Comentario explicativo:
# - Este archivo **conecta todas las clases**: crea un "cliente", asigna un "servicio" y genera una "reserva" para el cliente.
# - Luego se confirma la reserva" y se imprime el estado antes y después de la confirmación.