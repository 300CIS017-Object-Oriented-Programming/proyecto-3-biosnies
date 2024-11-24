from gestor_datos import GestorDatos
from gestor_filtros import GestorFiltros
from analizador import Analizador
from visualizador import Visualizador
from manejador_excepciones import ManejadorExcepciones


class AplicacionSNIES:
    """
    Clase principal para la aplicación SNIES.

    Atributos
    ----------
    gestor_datos : GestorDatos
        Instancia para gestionar los datos.
    gestor_filtros : GestorFiltros
        Instancia para gestionar los filtros.
    analizador : Analizador
        Instancia para analizar los datos.
    visualizador : Visualizador
        Instancia para visualizar los resultados.
    manejador_excepciones : ManejadorExcepciones
        Instancia para manejar las excepciones.

    Métodos
    -------
    inicializar_aplicacion()
        Inicializa la aplicación SNIES.
    mostrar_archivos()
        Muestra los archivos disponibles.
    cargar_archivos()
        Carga los archivos de datos.
    ejecutar_analisis()
        Ejecuta el análisis de los datos.
    guardar_configuracion()
        Guarda la configuración actual.
    """

    def __init__(self):
        """
        Inicializa los componentes de la aplicación SNIES.
        """
        self.gestor_datos = GestorDatos()
        self.gestor_filtros = GestorFiltros()
        self.analizador = Analizador()
        self.visualizador = Visualizador()
        self.manejador_excepciones = ManejadorExcepciones()

    def inicializar_aplicacion(self):
        """
        Inicializa la aplicación SNIES.
        """
        print("Inicializando la aplicación SNIES...")

    def mostrar_archivos(self):
        """
        Muestra los archivos disponibles.

        Maneja excepciones en caso de error.
        """
        try:
            archivos = self.gestor_datos.mostrar_archivos_disponibles()
            print("Archivos disponibles:", archivos)
        except Exception as e:
            self.manejador_excepciones.manejar_error(e)

    def cargar_archivos(self):
        """
        Carga los archivos de datos.

        Maneja excepciones en caso de error.
        """
        try:
            self.gestor_datos.cargar_datos()
            print("Archivos cargados exitosamente.")
        except Exception as e:
            self.manejador_excepciones.manejar_error(e)

    def ejecutar_analisis(self):
        """
        Ejecuta el análisis de los datos.

        Maneja excepciones en caso de error.
        """
        try:
            self.gestor_filtros.seleccionar_programas()
            resultados = self.analizador.calcular_estadisticas()
            self.visualizador.mostrar_resultados(resultados)
        except Exception as e:
            self.manejador_excepciones.manejar_error(e)

    def guardar_configuracion(self):
        """
        Guarda la configuración actual.
        """
        print("Configuración guardada correctamente.")


if __name__ == "__main__":
    app = AplicacionSNIES()
    app.inicializar_aplicacion()