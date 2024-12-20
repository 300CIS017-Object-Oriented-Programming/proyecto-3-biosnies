import pandas as pd
import os
from manejador_excepciones import ManejadorExcepciones

class GestorDatos:
    """
    Clase para gestionar los datos de los archivos Excel.

    Métodos
    -------
    normalizar_columnas(df)
        Normaliza los nombres de las columnas de un DataFrame.
    load_data()
        Carga los datos de los archivos Excel en el directorio especificado.
    rename_columns(df)
        Renombra las columnas de un DataFrame según los sinónimos definidos.
    get_optional_columns(file_name)
        Obtiene las columnas opcionales basadas en el nombre del archivo.
    get_available_columns(data)
        Obtiene todas las columnas disponibles en los datos cargados.
    show_column_info(data)
        Muestra información de las columnas de los DataFrames cargados.
    buscar_por_palabra_clave(palabra_clave, dataframes)
        Busca programas académicos por palabra clave en los DataFrames cargados.
    """

    def __init__(self, ruta_directorio):

        self.ruta_directorio = ruta_directorio

        self.min_required_columns = [
            "codigo_institucion", "institucion", "codigo_snies", "programa_academico",
            "anio", "semestre"
        ]

        self.optional_columns = {
            "admitidos": ["admitidos"],
            "graduados": ["graduados"],
            "inscritos": ["inscritos"],
            "total_matriculados": ["matriculados"],
            "nuevos_matriculados": ["primer_curso"]
        }

        # Diccionario de sinónimos
        self.column_synonyms = {
            "codigo_institucion": ["CÓDIGO DE LA INSTITUCIÓN"],
            "ies_padre": ["IES PADRE", "IES_PADRE"],
            "institucion": ["INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)"],
            "tipo_ies": ["TIPO IES", "PRINCIPAL O SECCIONAL"],
            "id_sector": ["ID SECTOR IES"],
            "sector_ies": ["SECTOR IES"],
            "id_caracter": ["ID CARÁCTER IES", "ID CARACTER"],
            "caracter_ies": ["CARÁCTER IES", "CARACTER IES"],
            "codigo_departamento_ies": ["CÓDIGO DEL DEPARTAMENTO (IES)"],
            "departamento_domicilio_ies": ["DEPARTAMENTO DE DOMICILIO DE LA IES"],
            "codigo_municipio_ies": ["CÓDIGO DEL MUNICIPIO IES", "CÓDIGO DEL MUNICIPIO (IES)"],
            "municipio_domicilio_ies": ["MUNICIPIO DE DOMICILIO DE LA IES"],
            "codigo_snies": ["CÓDIGO SNIES DEL PROGRAMA"],
            "programa_academico": ["PROGRAMA ACADÉMICO", "programa académico"],
            "id_nivel_academico": ["ID NIVEL ACADÉMICO"],
            "nivel_academico": ["NIVEL ACADÉMICO"],
            "id_nivel_formacion": ["ID NIVEL DE FORMACIÓN"],
            "nivel_formacion": ["NIVEL DE FORMACIÓN"],
            "id_metodologia": ["ID METODOLOGÍA", "ID MODALIDAD"],
            "metodologia": ["METODOLOGÍA", "MODALIDAD"],
            "id_area": ["ID ÁREA", "ID ÁREA DE CONOCIMIENTO"],
            "area_conocimiento": ["ÁREA DE CONOCIMIENTO"],
            "id_nucleo": ["ID NÚCLEO"],
            "nucleo_basico_conocimiento": ["NÚCLEO BÁSICO DEL CONOCIMIENTO (NBC)"],
            "id_cine_campo_amplio": ["ID CINE CAMPO AMPLIO"],
            "desc_cine_campo_amplio": ["DESC CINE CAMPO AMPLIO"],
            "id_cine_campo_especifico": ["ID CINE CAMPO ESPECIFICO"],
            "desc_cine_campo_especifico": ["DESC CINE CAMPO ESPECIFICO"],
            "id_cine_campo_detallado": ["ID CINE CODIGO DETALLADO", "ID CINE CAMPO DETALLADO"],
            "desc_cine_campo_detallado": ["DESC CINE CODIGO DETALLADO", "DESC CINE CAMPO DETALLADO"],
            "codigo_departamento_programa": ["CÓDIGO DEL DEPARTAMENTO (PROGRAMA)"],
            "departamento_oferta_programa": ["DEPARTAMENTO DE OFERTA DEL PROGRAMA"],
            "codigo_municipio_programa": ["CÓDIGO DEL MUNICIPIO (PROGRAMA)"],
            "municipio_oferta_programa": ["MUNICIPIO DE OFERTA DEL PROGRAMA"],
            "id_sexo": ["ID SEXO"],
            "sexo": ["SEXO"],
            "anio": ["AÑO"],
            "semestre": ["SEMESTRE"],
            "total_matriculados": ["MATRICULADOS"],
            "inscritos": ["INSCRITOS"],
            "graduados": ["GRADUADOS"],
            "admitidos": ["ADMITIDOS"],
            "nuevos_matriculados": ["MATRICULADOS PRIMER CURSO","PRIMER CURSO"],
        }

    def normalizar_columnas(self, df):
        """
        Normaliza los nombres de las columnas de un DataFrame.

        Parámetros
        ----------
        df : DataFrame
            DataFrame cuyas columnas serán normalizadas.

        Devuelve
        -------
        DataFrame
            DataFrame con los nombres de las columnas normalizados.
        """
        df.columns = df.columns.str.lower().str.replace(" ", "_")
        return df

    @ManejadorExcepciones.manejar_errores
    def load_data(self):
        """
        Carga los datos de los archivos Excel en el directorio especificado.

        Devuelve
        -------
        dict
            Diccionario donde las claves son los nombres de los archivos y los valores son los DataFrames cargados.
        """
        data = {}
        for file in os.listdir(self.ruta_directorio):
            if file.endswith('.xlsx'):
                file_path = os.path.join(self.ruta_directorio, file)
                try:
                    df = pd.read_excel(file_path, header=0)
                    df = self.rename_columns(df)
                    missing_min_columns = [col for col in self.min_required_columns if col not in df.columns]

                    optional_columns = self.get_optional_columns(file)
                    missing_optional_columns = [col for col in optional_columns if col not in df.columns]

                    if missing_min_columns:
                        print(f"Error: {file} no contiene las columnas mínimas requeridas: {missing_min_columns}")
                    else:
                        data[file] = df
                        if missing_optional_columns:
                            print(
                                f"Advertencia: {file} no contiene todas las columnas opcionales: {missing_optional_columns}")
                        print(f"Datos cargados exitosamente desde {file}.")
                except Exception as e:
                    print(f"Error al cargar {file}: {e}")
        return data

    def rename_columns(self, df):
        """
        Renombra las columnas de un DataFrame según los sinónimos definidos.

        Parámetros
        ----------
        df : DataFrame
            DataFrame cuyas columnas serán renombradas.

        Devuelve
        -------
        DataFrame
            DataFrame con las columnas renombradas.
        """
        new_columns = {}
        for col in df.columns:
            col_lower = col.lower().strip().replace(" ", "_")
            for standard_name, synonyms in self.column_synonyms.items():
                if col in synonyms:
                    new_columns[col] = standard_name
                    break
            else:
                new_columns[col] = col_lower
        return df.rename(columns=new_columns)

    def get_optional_columns(self, file_name):
        """
        Obtiene las columnas opcionales basadas en el nombre del archivo.

        Parámetros
        ----------
        file_name : str
            Nombre del archivo.

        Devuelve
        -------
        list
            Lista de columnas opcionales.
        """
        for key, cols in self.optional_columns.items():
            if key in file_name.lower():
                return cols
        return []

    def get_available_columns(self, data):
        """
        Obtiene todas las columnas disponibles en los datos cargados.

        Parámetros
        ----------
        data : dict
            Diccionario de DataFrames cargados.

        Devuelve
        -------
        set
            Conjunto de todas las columnas disponibles.
        """
        columns = set()
        for _, df in data.items():
            columns.update(df.columns)
        return columns

    def show_column_info(self, data):
        """
        Muestra información de las columnas de los DataFrames cargados.

        Parámetros
        ----------
        data : dict
            Diccionario de DataFrames cargados.
        """
        for name, df in data.items():
            print(f"\nColumnas en {name}:")
            for column in df.columns:
                print(f"- {column}")

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
        """
        datos_combinados = pd.concat(dataframes.values(), ignore_index=True)

        if 'programa_academico' not in datos_combinados.columns:
            raise KeyError("La columna 'programa_academico' no se encuentra en los datos.")

        programas_filtrados = datos_combinados[datos_combinados['programa_academico']
        .str.contains(palabra_clave, case=False, na=False)]
        return programas_filtrados