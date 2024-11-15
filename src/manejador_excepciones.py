import logging
import os


class ManejadorExcepciones:
    def __init__(self, log_path="../docs/outputs/error_log.txt"):
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        self.log_path = log_path
        logging.basicConfig(
            filename=self.log_path,
            level=logging.ERROR,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    @staticmethod
    def manejar_errores(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.error(f"Error en {func.__name__}: {e}")
                print(f"Error: {e}")
                raise e
        return wrapper

    def manejar_error(self, error):
        error_mensaje = f"Ocurrió un error: {str(error)}"
        print(error_mensaje)
        self.registrar_error("Error", error_mensaje)

    def validar_entrada_usuario(self, entrada, tipo_dato):
        if not isinstance(entrada, tipo_dato):
            error_mensaje = f"Entrada inválida: Se esperaba {tipo_dato}, pero se recibió {type(entrada)}"
            self.manejar_error(ValueError(error_mensaje))
            return False
        return True

    def registrar_error(self, tipo_error, detalles):
        mensaje_log = f"{tipo_error}: {detalles}"
        logging.error(mensaje_log)
        print("Error registrado en el log.")

    def mostrar_error_usuario(self, mensaje):
        print(f"Advertencia: {mensaje}")
