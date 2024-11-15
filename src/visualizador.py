import plotly.express as px
import pandas as pd

class Visualizador:
    def __init__(self, configuracion_graficos=None):
        self.configuracion_graficos = configuracion_graficos or {}
        self.datos_analizados = pd.DataFrame()

    def establecer_datos_analizados(self, datos):
        self.datos_analizados = datos
        print("Datos analizados configurados para visualización.")

    def graficar_tendencias_inscripcion(self):
        if 'anio' not in self.datos_analizados or 'inscritos' not in self.datos_analizados:
            return None
        return px.line(self.datos_analizados, x="anio", y="inscritos", title="Tendencias de Inscripción por Año")

    def graficar_comparacion_genero(self):
        if "programa" not in self.datos_analizados.columns or "graduados" not in self.datos_analizados.columns:
            print("Advertencia: Las columnas necesarias para la gráfica no están disponibles.")
            return None

        fig = px.bar(
            self.datos_analizados,
            x="programa",  # Cambia 'programa_academico' por 'programa'
            y="graduados",
            title="Comparación de Graduados por Programa",
            labels={"programa": "Programa", "graduados": "Número de Graduados"}
        )
        return fig
