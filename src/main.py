import pandas as pd
from gestor_datos import GestorDatos
from visualizador import Visualizador

def main():
    """
    Función principal que inicializa la aplicación SNIES, carga los datos,
    muestra información de las columnas y genera gráficos de visualización.
    """
    print("Inicializando la aplicación SNIES...")

    # Ruta del directorio donde se encuentran los archivos de entrada
    ruta_directorio = "C:/Users/Lenovo/Desktop/GIT/proyecto-3-biosnies/docs/inputs"

    # Inicializa la instancia de GestorDatos con la ruta del directorio
    gestor = GestorDatos(ruta_directorio)

    # Carga los datos de los archivos Excel en el directorio especificado
    datos = gestor.load_data()

    # Consolida los datos cargados en un solo DataFrame
    datos_consolidados = pd.concat(datos.values(), ignore_index=True)

    # Muestra información de las columnas de los DataFrames cargados
    gestor.show_column_info(datos)

    # Inicializa la instancia de Visualizador
    visualizador = Visualizador()

    # Establece los datos analizados en la instancia de Visualizador
    visualizador.establecer_datos_analizados(datos_consolidados)

    print("Generando gráficos...")

    # Genera y muestra el gráfico de tendencias de inscripción
    visualizador.graficar_tendencias_inscripcion()

    # Genera y muestra el gráfico de comparación por género
    visualizador.graficar_comparacion_genero()

if __name__ == "__main__":
    main()