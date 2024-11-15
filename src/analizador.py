import pandas as pd

class Analizador:
    def __init__(self, rango_anios=(2020, 2023)):
        self.rango_anios = rango_anios
        self.programas_seleccionados = []
        self.resultados_estadisticas = pd.DataFrame()

    def establecer_programas_seleccionados(self, programas_datos):
        self.programas_seleccionados = programas_datos

    def calcular_estadisticas(self, dataframes):
        estadisticas = []
        for _, programa in self.programas_seleccionados.iterrows():  # Itera sobre las filas de programas seleccionados
            for _, datos in dataframes.items():
                if "anio" in datos.columns:
                    datos["anio"] = pd.to_numeric(datos["anio"], errors="coerce").fillna(0).astype(int)

                datos_programa = datos[(datos["codigo_snies"] == programa["codigo_snies"]) &
                                       (datos["anio"].between(*self.rango_anios))]
                for anio in range(self.rango_anios[0], self.rango_anios[1] + 1):
                    datos_anio = datos_programa[datos_programa["anio"] == anio]
                    estadisticas.append({
                        "programa": programa["programa_academico"],
                        "anio": anio,
                        "inscritos": datos_anio["inscritos"].sum() if "inscritos" in datos_anio else 0,
                        "admitidos": datos_anio["admitidos"].sum() if "admitidos" in datos_anio else 0,
                        "nuevos_matriculados": datos_anio[
                            "nuevos_matriculados"].sum() if "nuevos_matriculados" in datos_anio else 0,
                        "total_matriculados": datos_anio[
                            "total_matriculados"].sum() if "total_matriculados" in datos_anio else 0,
                        "graduados": datos_anio["graduados"].sum() if "graduados" in datos_anio else 0,
                    })
        self.resultados_estadisticas = pd.DataFrame(estadisticas)
        return self.resultados_estadisticas

    def obtener_estadisticas(self):
        return self.resultados_estadisticas
