import pandas as pd

class GestorFiltros:
    """
    Clase para gestionar los filtros de búsqueda y selección de programas académicos.

    Atributos
    ----------
    palabras_clave_busqueda : list
        Lista de palabras clave utilizadas para la búsqueda.
    programas_seleccionados : list
        Lista de programas académicos seleccionados.

    """

    def __init__(self):
        """
        Inicializa la clase GestorFiltros con listas vacías para palabras clave y programas seleccionados.
        """
        self.palabras_clave_busqueda = []
        self.programas_seleccionados = []

    def buscar_por_palabra_clave(self, palabra_clave, dataframes):
        """
        Busca programas académicos por palabra clave en los DataFrames cargados.

        Parámetros
        ----------
        palabra_clave : str
            Palabra clave para buscar en los programas académicos.
        dataframes : dict
            Diccionario de DataFrames cargados.

        Devuelve
        -------
        DataFrame
            DataFrame con los programas académicos que coinciden con la palabra clave.

        Lanza
        -----
        KeyError
            Si la columna 'programa_academico' no se encuentra en los datos.
        """
        datos_combinados = pd.concat(dataframes.values(), ignore_index=True)

        if 'programa_academico' not in datos_combinados.columns:
            raise KeyError("La columna 'programa_academico' no se encuentra en los datos.")

        programas_filtrados = datos_combinados[datos_combinados['programa_academico']
        .str.contains(palabra_clave, case=False, na=False)]
        return programas_filtrados

    def seleccionar_programa(self, programa):
        """
        Selecciona un programa académico y lo añade a la lista de programas seleccionados.

        Parámetros
        ----------
        programa : object
            Objeto que representa un programa académico.
        """
        if programa not in self.programas_seleccionados:
            self.programas_seleccionados.append(programa)
            print(f"Programa '{programa.nombre}' seleccionado.")
        else:
            print(f"El programa '{programa.nombre}' ya ha sido seleccionado.")

    def obtener_programas_seleccionados(self):
        """
        Obtiene la lista de programas académicos seleccionados.

        Devuelve
        -------
        list
            Lista de programas académicos seleccionados.
        """
        return self.programas_seleccionados

    def validar_palabra_clave(self, palabra_clave):
        """
        Valida si una palabra clave es válida.

        Parámetros
        ----------
        palabra_clave : str
            Palabra clave a validar.

        Devuelve
        -------
        bool
            True si la palabra clave es válida, False en caso contrario.
        """
        es_valida = bool(palabra_clave and palabra_clave.strip())
        print(f"Palabra clave {'válida' if es_valida else 'inválida'}: '{palabra_clave}'")
        return es_valida