# Este archivo tendrá funciones que gestionan el registro de eventos y errores. 
# Utilizando el módulo logging, se grabarán eventos de éxito (como el registro de clientes y servicios) 
# y errores (como entradas de datos inválidos). Los registros se guardarán en el archivo error_logs.txt dentro de la carpeta logs/.

# Comentario explicativo:
# logging.basicConfig configura el sistema para que todo lo que pase importante (como errores o eventos) se guarde en un archivo llamado error_logs.txt.
# registrar_log es una forma simple de añadir mensajes al archivo para tener un historial de lo que pasa en el sistema.

# src/log.py
import logging
from pathlib import Path

# Definir el directorio y archivo de logs
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)  # Crear el directorio de logs si no existe

LOG_FILE = LOG_DIR / "error_logs.txt"  # Archivo donde se registrarán los logs

# Configuración básica de logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,  # Nivel de logging (INFO para registrar eventos)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato del mensaje de log
    encoding="utf-8",
    filemode='w'  # Esto asegura que el archivo se sobreescriba cada vez (en lugar de acumular entradas de logs viejos)
)

# Función para forzar el guardado inmediato del log
def _forzar_guardado():
    for handler in logging.getLogger().handlers:
        handler.flush()  # Esto asegura que los logs se escriban de inmediato

# Función para registrar eventos (operaciones exitosas)
def registrar_evento(mensaje):
    """
    Registra eventos (éxitos, confirmaciones, etc.) en el log.
    """
    logging.info(f"Evento exitoso: {mensaje}")  # Registra evento con nivel INFO
    _forzar_guardado()  # Forzar la escritura inmediata en el archivo de log

# Función para registrar errores
def registrar_error(mensaje):
    """
    Registra errores (fallos, excepciones, etc.) en el log.
    """
    logging.error(f"Error: {mensaje}")  # Registra error con nivel ERROR
    _forzar_guardado()  # Forzar la escritura inmediata en el archivo de log