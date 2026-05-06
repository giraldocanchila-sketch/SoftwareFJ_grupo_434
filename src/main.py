# Este será el archivo principal que ejecutará el sistema. A través de este script, el usuario 
# podrá interactuar con el programa para registrar clientes, crear servicios y realizar reservas. 
# También manejará las excepciones y registrará los resultados de las operaciones.


# Comentario explicativo:
# - Este archivo **conecta todas las clases**: crea un "cliente", asigna un "servicio" y genera una "reserva" para el cliente.
# - Luego se confirma la reserva" y se imprime el estado antes y después de la confirmación.

from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva
from excepciones import ErrorSistema
import log


clientes = []
servicios = []
reservas = []
operaciones = []


def registrar_resultado(nombre_operacion, resultado, mensaje):
    operaciones.append({
        "operacion": nombre_operacion,
        "resultado": resultado,
        "mensaje": mensaje
    })

    if resultado == "Exitosa":
        log.registrar_evento(f"{nombre_operacion} - {mensaje}")
    else:
        log.registrar_error(f"{nombre_operacion} - {mensaje}")


def leer_entero(mensaje):
    valor = input(mensaje)

    try:
        return int(valor)
    except ValueError as error:
        raise ValueError("Debe ingresar un número entero válido.") from error


def leer_float(mensaje):
    valor = input(mensaje)

    try:
        return float(valor)
    except ValueError as error:
        raise ValueError("Debe ingresar un número válido.") from error


def registrar_cliente():
    print("\n--- REGISTRO DE CLIENTE ---")

    try:
        nombre = input("Nombre del cliente: ")
        email = input("Email del cliente: ")
        telefono = input("Teléfono del cliente: ")

        cliente = Cliente(nombre, email, telefono)
        clientes.append(cliente)

    except Exception as error:
        mensaje = f"Cliente fallido: {error}"
        print(mensaje)
        registrar_resultado("Registro de cliente", "Fallida", mensaje)

    else:
        mensaje = f"Cliente creado correctamente. {cliente.mostrar_info()}"
        print(mensaje)
        registrar_resultado("Registro de cliente", "Exitosa", mensaje)

    finally:
        print("Operación de cliente finalizada.")


def crear_servicio():
    print("\n--- CREACIÓN DE SERVICIO ---")
    print("Servicios disponibles:")
    print("1. Reserva de Sala")
    print("2. Alquiler de Equipos")
    print("3. Asesoría Especializada")

    try:
        opcion = input("Seleccione el número del servicio: ")

        tarifa_base = leer_float("Tarifa base del servicio: ")

        disponible_texto = input("¿El servicio está disponible? (s/n): ").lower()

        if disponible_texto == "s":
            disponible = True
        elif disponible_texto == "n":
            disponible = False
        else:
            raise ValueError("Debe responder 's' para sí o 'n' para no.")

        if opcion == "1":
            capacidad = leer_entero("Capacidad de la sala: ")
            servicio = ReservaSala(tarifa_base, capacidad, disponible)

        elif opcion == "2":
            cantidad_equipos = leer_entero("Cantidad de equipos a alquilar: ")
            servicio = AlquilerEquipo(tarifa_base, cantidad_equipos, disponible)

        elif opcion == "3":
            especialidad = input("Especialidad de la asesoría: ")
            servicio = AsesoriaEspecializada(tarifa_base, especialidad, disponible)

        else:
            raise ValueError("Opción de servicio inválida. Debe seleccionar 1, 2 o 3.")

        servicios.append(servicio)

    except Exception as error:
        mensaje = f"Servicio fallido: {error}"
        print(mensaje)
        registrar_resultado("Creación de servicio", "Fallida", mensaje)

    else:
        mensaje = f"Servicio creado correctamente. {servicio.mostrar_info()} | {servicio.describir_servicio()}"
        print(mensaje)
        registrar_resultado("Creación de servicio", "Exitosa", mensaje)

    finally:
        print("Operación de servicio finalizada.")


def crear_reserva():
    print("\n--- CREACIÓN DE RESERVA ---")

    try:
        if not clientes:
            raise ValueError("No hay clientes registrados.")

        if not servicios:
            raise ValueError("No hay servicios creados.")

        listar_clientes()
        indice_cliente = leer_entero("Seleccione el número del cliente: ") - 1

        if indice_cliente < 0 or indice_cliente >= len(clientes):
            raise ValueError("El cliente seleccionado no existe.")

        listar_servicios()
        indice_servicio = leer_entero("Seleccione el número del servicio: ") - 1

        if indice_servicio < 0 or indice_servicio >= len(servicios):
            raise ValueError("El servicio seleccionado no existe.")

        duracion = leer_entero("Duración de la reserva en horas: ")

        reserva = Reserva(clientes[indice_cliente], servicios[indice_servicio], duracion)
        reservas.append(reserva)

    except Exception as error:
        mensaje = f"Reserva fallida: {error}"
        print(mensaje)
        registrar_resultado("Creación de reserva", "Fallida", mensaje)

    else:
        mensaje = f"Reserva creada correctamente. {reserva.mostrar_info()}"
        print(mensaje)
        registrar_resultado("Creación de reserva", "Exitosa", mensaje)

    finally:
        print("Operación de reserva finalizada.")


def confirmar_reserva():
    print("\n--- CONFIRMACIÓN DE RESERVA ---")

    try:
        if not reservas:
            raise ValueError("No hay reservas registradas.")

        listar_reservas()
        indice_reserva = leer_entero("Seleccione el número de la reserva a confirmar: ") - 1

        if indice_reserva < 0 or indice_reserva >= len(reservas):
            raise ValueError("La reserva seleccionada no existe.")

        mensaje = reservas[indice_reserva].confirmar()

    except Exception as error:
        mensaje = f"Confirmación fallida: {error}"
        print(mensaje)
        registrar_resultado("Confirmación de reserva", "Fallida", mensaje)

    else:
        print(mensaje)
        registrar_resultado("Confirmación de reserva", "Exitosa", mensaje)

    finally:
        print("Operación de confirmación finalizada.")


def cancelar_reserva():
    print("\n--- CANCELACIÓN DE RESERVA ---")

    try:
        if not reservas:
            raise ValueError("No hay reservas registradas.")

        listar_reservas()
        indice_reserva = leer_entero("Seleccione el número de la reserva a cancelar: ") - 1

        if indice_reserva < 0 or indice_reserva >= len(reservas):
            raise ValueError("La reserva seleccionada no existe.")

        mensaje = reservas[indice_reserva].cancelar()

    except Exception as error:
        mensaje = f"Cancelación fallida: {error}"
        print(mensaje)
        registrar_resultado("Cancelación de reserva", "Fallida", mensaje)

    else:
        print(mensaje)
        registrar_resultado("Cancelación de reserva", "Exitosa", mensaje)

    finally:
        print("Operación de cancelación finalizada.")


def procesar_reserva():
    print("\n--- PROCESAMIENTO DE RESERVA ---")

    try:
        if not reservas:
            raise ValueError("No hay reservas registradas.")

        listar_reservas()
        indice_reserva = leer_entero("Seleccione el número de la reserva a procesar: ") - 1

        if indice_reserva < 0 or indice_reserva >= len(reservas):
            raise ValueError("La reserva seleccionada no existe.")

        mensaje = reservas[indice_reserva].procesar()

    except Exception as error:
        mensaje = f"Procesamiento fallido: {error}"
        print(mensaje)
        registrar_resultado("Procesamiento de reserva", "Fallida", mensaje)

    else:
        print(mensaje)
        registrar_resultado("Procesamiento de reserva", "Exitosa", mensaje)

    finally:
        print("Operación de procesamiento finalizada.")


def listar_clientes():
    print("\n--- CLIENTES REGISTRADOS ---")

    if not clientes:
        print("No hay clientes registrados.")
        return

    for i, cliente in enumerate(clientes, start=1):
        print(f"{i}. {cliente.mostrar_info()}")


def listar_servicios():
    print("\n--- SERVICIOS CREADOS ---")

    if not servicios:
        print("No hay servicios creados.")
        return

    for i, servicio in enumerate(servicios, start=1):
        print(f"{i}. {servicio.mostrar_info()} | {servicio.describir_servicio()}")


def listar_reservas():
    print("\n--- RESERVAS REGISTRADAS ---")

    if not reservas:
        print("No hay reservas registradas.")
        return

    for i, reserva in enumerate(reservas, start=1):
        print(f"{i}. {reserva.mostrar_info()}")


def mostrar_resumen():
    print("\n========== RESUMEN DE OPERACIONES ==========")

    if not operaciones:
        print("No se registraron operaciones.")
        return

    for i, operacion in enumerate(operaciones, start=1):
        print(
            f"{i}. {operacion['operacion']} | "
            f"Resultado: {operacion['resultado']} | "
            f"{operacion['mensaje']}"
        )

    exitosas = sum(1 for op in operaciones if op["resultado"] == "Exitosa")
    fallidas = sum(1 for op in operaciones if op["resultado"] == "Fallida")

    print("--------------------------------------------")
    print(f"Total de operaciones realizadas: {len(operaciones)}")
    print(f"Operaciones exitosas: {exitosas}")
    print(f"Operaciones fallidas: {fallidas}")


def mostrar_menu():
    print("\n========== SOFTWARE FJ ==========")
    print("Operaciones realizadas:", len(operaciones), "/ 10")
    print("1. Registrar cliente")
    print("2. Crear servicio")
    print("3. Crear reserva")
    print("4. Confirmar reserva")
    print("5. Cancelar reserva")
    print("6. Procesar reserva")
    print("7. Listar clientes")
    print("8. Listar servicios")
    print("9. Listar reservas")
    print("0. Salir")


def ejecutar():
    print("Sistema Integral de Gestión de Clientes, Servicios y Reservas")
    print("Debe realizar mínimo 10 operaciones.")
    print("Los errores solo aparecerán si usted ingresa datos inválidos.")

    while len(operaciones) < 10:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            crear_servicio()
        elif opcion == "3":
            crear_reserva()
        elif opcion == "4":
            confirmar_reserva()
        elif opcion == "5":
            cancelar_reserva()
        elif opcion == "6":
            procesar_reserva()
        elif opcion == "7":
            listar_clientes()
        elif opcion == "8":
            listar_servicios()
        elif opcion == "9":
            listar_reservas()
        elif opcion == "0":
            break
        else:
            mensaje = "Opción de menú inválida."
            print(mensaje)
            registrar_resultado("Selección de menú", "Fallida", mensaje)

    mostrar_resumen()
    print("\nPrograma finalizado sin interrupciones.")


if __name__ == "__main__":
    ejecutar()