import pandas as pd
from gestor_datos import GestorDatos
from visualizador import Visualizador

def main():
    print("Inicializando la aplicación SNIES...")
    ruta_directorio = "C:/Users/Lenovo/Desktop/GIT/proyecto-3-biosnies/docs/inputs"
    gestor = GestorDatos(ruta_directorio)
    datos = gestor.load_data()

    datos_consolidados = pd.concat(datos.values(), ignore_index=True)
    gestor.show_column_info(datos)

    visualizador = Visualizador()
    visualizador.establecer_datos_analizados(datos_consolidados)

    print("Generando gráficos...")
    visualizador.graficar_tendencias_inscripcion()
    visualizador.graficar_comparacion_genero()

if __name__ == "__main__":
    main()
