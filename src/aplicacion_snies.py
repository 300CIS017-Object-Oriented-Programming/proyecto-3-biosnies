from gestor_datos import GestorDatos
from gestor_filtros import GestorFiltros
from analizador import Analizador
from visualizador import Visualizador
from manejador_excepciones import ManejadorExcepciones


class AplicacionSNIES:
    def __init__(self):
        self.gestor_datos = GestorDatos()
        self.gestor_filtros = GestorFiltros()
        self.analizador = Analizador()
        self.visualizador = Visualizador()
        self.manejador_excepciones = ManejadorExcepciones()

    def inicializar_aplicacion(self):
        print("Inicializando la aplicación SNIES...")

    def mostrar_archivos(self):
        try:
            archivos = self.gestor_datos.mostrar_archivos_disponibles()
            print("Archivos disponibles:", archivos)
        except Exception as e:
            self.manejador_excepciones.manejar_error(e)

    def cargar_archivos(self):
        try:
            self.gestor_datos.cargar_datos()
            print("Archivos cargados exitosamente.")
        except Exception as e:
            self.manejador_excepciones.manejar_error(e)

    def ejecutar_analisis(self):
        try:
            self.gestor_filtros.seleccionar_programas()
            resultados = self.analizador.calcular_estadisticas()
            self.visualizador.mostrar_resultados(resultados)
        except Exception as e:
            self.manejador_excepciones.manejar_error(e)

    def guardar_configuracion(self):
        print("Configuración guardada correctamente.")


if __name__ == "__main__":
    app = AplicacionSNIES()
    app.inicializar_aplicacion()
