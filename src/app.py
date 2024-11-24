import streamlit as st
import pandas as pd
from gestor_datos import GestorDatos
from analizador import Analizador
from visualizador import Visualizador
import io

# Configura la página de Streamlit con un título y diseño
st.set_page_config(page_title="SNIES Visualizador", layout="wide")

# Inicializa instancias de GestorDatos, Analizador y Visualizador
gestor_datos = GestorDatos("C:/Users/Lenovo/Desktop/GIT/proyecto-3-biosnies/docs/inputs")
analizador = Analizador()
visualizador = Visualizador()

# Título de la barra lateral para la sección de carga de archivos
st.sidebar.title("Cargar Archivos")
# Widget de carga de archivos en la barra lateral para seleccionar múltiples archivos Excel
uploaded_files = st.sidebar.file_uploader("Selecciona archivos Excel", accept_multiple_files=True, type=["xlsx"])

# Diccionario para almacenar los dataframes cargados de los archivos subidos
dataframes = {}

# Si se suben archivos, procesa cada archivo
if uploaded_files:
    for uploaded_file in uploaded_files:
        try:
            # Lee el archivo Excel subido en un dataframe
            df = pd.read_excel(uploaded_file)
            # Renombra las columnas usando la instancia de gestor_datos y almacena en el diccionario de dataframes
            dataframes[uploaded_file.name] = gestor_datos.rename_columns(df)
            st.success(f"Archivo cargado: {uploaded_file.name}")

            # Muestra las columnas del dataframe cargado
            st.write(f"Columnas en {uploaded_file.name}: {list(dataframes[uploaded_file.name].columns)}")

        except Exception as e:
            # Muestra un mensaje de error si hay un problema al procesar el archivo
            st.error(f"Error al procesar {uploaded_file.name}: {e}")

    # Muestra los dataframes cargados
    st.write("Datos cargados:")
    st.write(dataframes)

# Mensaje de advertencia si no se cargan dataframes
if not dataframes:
    st.warning("Por favor, carga al menos un archivo para continuar.")

# Título de la barra lateral para la sección de filtrado de programas
st.sidebar.title("Filtrar Programas")

# Widget de entrada de texto en la barra lateral para introducir palabras clave separadas por comas
palabras_clave_input = st.sidebar.text_area(
    "Introduce palabras clave separadas por comas:",
    placeholder="Ejemplo: Ingeniería, Medicina, Derecho"
)

# Procesar palabras clave (remover espacios extra y duplicados)
palabras_clave = [palabra.strip() for palabra in palabras_clave_input.split(",") if palabra.strip()]
palabras_clave = list(set(palabras_clave))  # Eliminar duplicados

# DataFrame para almacenar los programas filtrados y lista para almacenar los programas seleccionados
programas_filtrados = pd.DataFrame()
programas_seleccionados = []

# Si se introducen palabras clave y se cargan dataframes, filtra los programas
if palabras_clave and dataframes:
    try:
        # Filtra los programas usando las palabras clave y almacena en programas_filtrados
        programas_filtrados = gestor_datos.buscar_por_palabras_clave(palabras_clave, dataframes)
        st.sidebar.write(f"Programas encontrados: {len(programas_filtrados)}")
    except KeyError as e:
        # Muestra un mensaje de error si hay un problema con las palabras clave
        st.error(f"Error: {e}")

# Mensaje de advertencia si no se encuentran programas con las palabras clave proporcionadas
if programas_filtrados.empty:
    st.warning("No se encontraron programas con las palabras clave proporcionadas.")
else:
    # Widget de selección múltiple para seleccionar programas para el análisis
    programas_seleccionados = st.multiselect(
        "Selecciona programas para el análisis",
        options=programas_filtrados['programa_academico'].unique()
    )

    # Muestra los programas seleccionados
    if programas_seleccionados:
        st.write("Programas seleccionados:", programas_seleccionados)

# DataFrame para almacenar los resultados del análisis
resultados = pd.DataFrame()


# Si se seleccionan programas, realiza el análisis
if programas_seleccionados:
    # Filtra los datos para los programas seleccionados
    programas_datos = programas_filtrados[programas_filtrados['programa_academico'].isin(programas_seleccionados)]
    analizador.establecer_programas_seleccionados(programas_datos)

    # Calcula las estadísticas y almacena en resultados
    resultados = analizador.calcular_estadisticas(dataframes)
    st.write("Resultados del análisis:")
    st.dataframe(resultados)
else:
    # Informa al usuario que seleccione al menos un programa
    st.info("Por favor selecciona al menos un programa para continuar.")

# Título para la sección de visualización de datos
st.title("Visualización de Datos")
if not resultados.empty:
    # Establece los datos analizados en la instancia de visualizador
    visualizador.establecer_datos_analizados(resultados)
    # Grafica y muestra las tendencias de inscripción
    tendencias_fig = visualizador.graficar_tendencias_inscripcion()
    if tendencias_fig:
        st.plotly_chart(tendencias_fig, use_container_width=True)
    # Agrega nuevas visualizaciones
    modalidad_fig = visualizador.graficar_comparacion_modalidad()
    if modalidad_fig:
        st.plotly_chart(modalidad_fig, use_container_width=True)

    genero_fig = visualizador.graficar_comparacion_genero()
    if genero_fig:
        st.plotly_chart(genero_fig, use_container_width=True)

# Si hay resultados disponibles, proporciona opciones de descarga
if not resultados.empty:
    buffer = io.BytesIO()  # Usa un buffer para manejar la conversión
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        resultados.to_excel(writer, index=False)
    buffer.seek(0)  # Resetea el puntero del buffer para que Streamlit pueda leerlo
    st.download_button(
        label="Descargar resultados en Excel",
        data=buffer,
        file_name="resultados.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    # Guardar como JSON
    resultados_json = resultados.to_json(orient="records", indent=4)
    st.download_button(
        label="Descargar resultados en JSON",
        data=resultados_json,
        file_name="resultados.json",
        mime="application/json"
    )
    # Guardar como CSV
    csv_data = resultados.to_csv(index=False).encode('utf-8')
    st.download_button(
    label="Descargar en formato CSV",
    data=csv_data,
    file_name="resultados.csv",
    mime="text/csv"
)
