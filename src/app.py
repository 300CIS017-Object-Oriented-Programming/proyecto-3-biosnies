import streamlit as st
import pandas as pd
from gestor_datos import GestorDatos
from analizador import Analizador
from visualizador import Visualizador
import io

st.set_page_config(page_title="SNIES Visualizador", layout="wide")

gestor_datos = GestorDatos("C:/Users/Lenovo/Desktop/GIT/proyecto-3-biosnies/docs/inputs")
analizador = Analizador()
visualizador = Visualizador()

st.sidebar.title("Cargar Archivos")
uploaded_files = st.sidebar.file_uploader("Selecciona archivos Excel", accept_multiple_files=True, type=["xlsx"])

dataframes = {}

if uploaded_files:
    for uploaded_file in uploaded_files:
        try:
            df = pd.read_excel(uploaded_file)
            dataframes[uploaded_file.name] = gestor_datos.rename_columns(df)
            st.success(f"Archivo cargado: {uploaded_file.name}")

            st.write(f"Columnas en {uploaded_file.name}: {list(dataframes[uploaded_file.name].columns)}")

        except Exception as e:
            st.error(f"Error al procesar {uploaded_file.name}: {e}")

    st.write("Datos cargados:")
    st.write(dataframes)

if not dataframes:
    st.warning("Por favor, carga al menos un archivo para continuar.")

st.sidebar.title("Filtrar Programas")
palabra_clave = st.sidebar.text_input("Introduce una palabra clave para filtrar programas:")

programas_filtrados = pd.DataFrame()
programas_seleccionados = []

if palabra_clave and dataframes:
    try:
        programas_filtrados = gestor_datos.buscar_por_palabra_clave(palabra_clave, dataframes)
        st.sidebar.write(f"Programas encontrados: {len(programas_filtrados)}")
    except KeyError as e:
        st.error(f"Error: {e}")

if programas_filtrados.empty:
    st.warning("No se encontraron programas con la palabra clave proporcionada.")
else:
    programas_seleccionados = st.multiselect(
        "Selecciona programas para el análisis",
        options=programas_filtrados['programa_academico'].unique()
    )

    if programas_seleccionados:
        st.write("Programas seleccionados:", programas_seleccionados)

resultados = pd.DataFrame()

if programas_seleccionados:
    programas_datos = programas_filtrados[programas_filtrados['programa_academico'].isin(programas_seleccionados)]
    analizador.establecer_programas_seleccionados(programas_datos)

    resultados = analizador.calcular_estadisticas(dataframes)
    st.write("Resultados del análisis:")
    st.dataframe(resultados)
else:
    st.info("Por favor selecciona al menos un programa para continuar.")

st.title("Visualización de Datos")
if not resultados.empty:
    visualizador.establecer_datos_analizados(resultados)
    tendencias_fig = visualizador.graficar_tendencias_inscripcion()
    if tendencias_fig:
        st.plotly_chart(tendencias_fig, use_container_width=True)
    # Agregar nuevas visualizaciones
    modalidad_fig = visualizador.graficar_comparacion_modalidad()
    if modalidad_fig:
        st.plotly_chart(modalidad_fig, use_container_width=True)

    genero_fig = visualizador.graficar_comparacion_genero()
    if genero_fig:
        st.plotly_chart(genero_fig, use_container_width=True)

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
