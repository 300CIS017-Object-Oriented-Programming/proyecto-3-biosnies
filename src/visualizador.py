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
        if 'anio' not in self.datos_analizados or 'inscritos' not in self.datos_analizados or 'programa' not in self.datos_analizados:
            print("Advertencia: Faltan columnas necesarias para la gráfica.")
            return None

        # Agrupar datos por año y programa
        datos_agrupados = self.datos_analizados.groupby(['anio', 'programa'], as_index=False)['inscritos'].sum()

        # Crear la gráfica
        fig = px.line(
            datos_agrupados,
            x="anio",
            y="inscritos",
            color="programa",  # Esto genera una línea por programa
            title="Tendencias de Inscripción por Programa y Año",
            labels={"anio": "Año", "inscritos": "Número de Inscritos", "programa": "Programa"}
        )
        return fig

    def graficar_comparacion_genero(self):
        if "programa" not in self.datos_analizados.columns or "graduados" not in self.datos_analizados.columns:
            print("Advertencia: Las columnas necesarias para la gráfica no están disponibles.")
            return None

        fig = px.bar(
            self.datos_analizados,
            x="programa",
            y="graduados",
            title="Comparación de Graduados por Programa",
            labels={"programa": "Programa", "graduados": "Número de Graduados"}
        )
        return fig

    def graficar_comparacion_modalidad(self):
        if "modalidad" not in self.datos_analizados.columns or "graduados" not in self.datos_analizados.columns:
            print("Advertencia: Las columnas necesarias para la gráfica no están disponibles.")
            return None

        fig = px.bar(
            self.datos_analizados,
            x="modalidad",
            y="graduados",
            color="modalidad",
            title="Comparación de Graduados por Modalidad (Virtual/Presencial)",
            labels={"modalidad": "Modalidad", "graduados": "Número de Graduados"}
        )
        return fig
