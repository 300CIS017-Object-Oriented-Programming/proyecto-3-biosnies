import plotly.express as px
import pandas as pd

class Visualizador:
    """
    Clase para visualizar datos analizados utilizando gráficos.

    Atributos
    ----------
    configuracion_graficos : dict
        Configuración opcional para los gráficos.
    datos_analizados : DataFrame
        DataFrame que contiene los datos analizados para la visualización.

    """

    def __init__(self, configuracion_graficos=None):

        self.configuracion_graficos = configuracion_graficos or {}
        self.datos_analizados = pd.DataFrame()

    def establecer_datos_analizados(self, datos):
        """
        Establece los datos analizados para la visualización.

        Parámetros
        ----------
        datos : DataFrame
            DataFrame que contiene los datos analizados.
        """
        self.datos_analizados = datos
        print("Datos analizados configurados para visualización.")

    def graficar_tendencias_inscripcion(self):
        """
        Genera un gráfico de líneas para mostrar las tendencias de inscripción por programa y año.

        Devuelve
        -------
        fig : plotly.graph_objs._figure.Figure or None
            Objeto de la figura de Plotly o None si faltan columnas necesarias.
        """
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
        """
        Genera un gráfico de barras para comparar el número de graduados por programa.

        Devuelve
        -------
        fig : plotly.graph_objs._figure.Figure or None
            Objeto de la figura de Plotly o None si faltan columnas necesarias.
        """
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
        """
        Genera un gráfico de barras para comparar el número de graduados por modalidad (virtual/presencial).

        Devuelve
        -------
        fig : plotly.graph_objs._figure.Figure or None
            Objeto de la figura de Plotly o None si faltan columnas necesarias.
        """
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