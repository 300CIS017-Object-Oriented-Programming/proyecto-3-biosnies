import logging
import os

class ManejadorExcepciones:
    """
    Clase para manejar excepciones y registrar errores en un archivo de log.

    Atributos
    ----------
    log_path : str
        Ruta del archivo de log donde se registrarán los errores.

    """

    def __init__(self, log_path="../docs/outputs/error_log.txt"):
        """
        Inicializa la clase ManejadorExcepciones y configura el archivo de log.

        Parámetros
        ----------
        log_path : str, opcional
            Ruta del archivo de log (por defecto es "../docs/outputs/error_log.txt").
        """
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        self.log_path = log_path
        logging.basicConfig(
            filename=self.log_path,
            level=logging.ERROR,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    @staticmethod
    def manejar_errores(func):
        """
        Decorador para manejar errores en funciones.

        Parámetros
        ----------
        func : function
            Función a la que se aplicará el decorador.

        Devuelve
        -------
        function
            Función decorada que maneja errores.
        """
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.error(f"Error en {func.__name__}: {e}")
                print(f"Error: {e}")
                raise e
        return wrapper

    def manejar_error(self, error):
        """
        Maneja un error específico y lo registra.

        Parámetros
        ----------
        error : Exception
            Excepción que será manejada y registrada.
        """
        error_mensaje = f"Ocurrió un error: {str(error)}"
        print(error_mensaje)
        self.registrar_error("Error", error_mensaje)

    def validar_entrada_usuario(self, entrada, tipo_dato):
        """
        Valida que la entrada del usuario sea del tipo de dato esperado.

        Parámetros
        ----------
        entrada : any
            Entrada del usuario a validar.
        tipo_dato : type
            Tipo de dato esperado para la entrada.

        Devuelve
        -------
        bool
            True si la entrada es del tipo de dato esperado, False en caso contrario.
        """
        if not isinstance(entrada, tipo_dato):
            error_mensaje = f"Entrada inválida: Se esperaba {tipo_dato}, pero se recibió {type(entrada)}"
            self.manejar_error(ValueError(error_mensaje))
            return False
        return True

    def registrar_error(self, tipo_error, detalles):
        """
        Registra un error en el archivo de log.

        Parámetros
        ----------
        tipo_error : str
            Tipo de error ocurrido.
        detalles : str
            Detalles del error.
        """
        mensaje_log = f"{tipo_error}: {detalles}"
        logging.error(mensaje_log)
        print("Error registrado en el log.")

    def mostrar_error_usuario(self, mensaje):
        """
        Muestra un mensaje de advertencia al usuario.

        Parámetros
        ----------
        mensaje : str
            Mensaje de advertencia a mostrar al usuario.
        """
        print(f"Advertencia: {mensaje}")