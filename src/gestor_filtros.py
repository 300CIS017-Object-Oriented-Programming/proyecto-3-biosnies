import pandas as pd

class GestorFiltros:
    def __init__(self):
        self.palabras_clave_busqueda = []
        self.programas_seleccionados = []

    def buscar_por_palabra_clave(self, palabra_clave, dataframes):
        datos_combinados = pd.concat(dataframes.values(), ignore_index=True)

        if 'programa_academico' not in datos_combinados.columns:
            raise KeyError("La columna 'programa_academico' no se encuentra en los datos.")

        programas_filtrados = datos_combinados[datos_combinados['programa_academico']
        .str.contains(palabra_clave, case=False, na=False)]
        return programas_filtrados

    def seleccionar_programa(self, programa):
        if programa not in self.programas_seleccionados:
            self.programas_seleccionados.append(programa)
            print(f"Programa '{programa.nombre}' seleccionado.")
        else:
            print(f"El programa '{programa.nombre}' ya ha sido seleccionado.")

    def obtener_programas_seleccionados(self):
        return self.programas_seleccionados

    def validar_palabra_clave(self, palabra_clave):
        es_valida = bool(palabra_clave and palabra_clave.strip())
        print(f"Palabra clave {'válida' if es_valida else 'inválida'}: '{palabra_clave}'")
        return es_valida
