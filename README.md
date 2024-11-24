# **Sistema SNIES - Análisis de Programas Académicos**

## **Descripción General**
Este sistema permite la carga, filtrado y análisis de datos de programas académicos de instituciones educativas con base en los datos del SNIES. Se ha desarrollado utilizando **Python** y **Streamlit**.

### **Características Principales**
1. **Carga de Archivos**:
   - Soporta múltiples archivos Excel.
   - Valida columnas mínimas requeridas para el análisis.
   - Renombra automáticamente las columnas utilizando un diccionario de sinónimos.
2. **Filtrado de Programas Académicos**:
   - Búsqueda por palabras clave (soporta múltiples palabras).
   - Resultados detallados con información relevante del programa.
3. **Selección y Análisis**:
   - Selección interactiva de programas desde los resultados.
   - Generación de estadísticas personalizadas.
   - Exportación de resultados en formatos `.xlsx`, `.csv` y `.json`.

---
## **Estructura del Proyecto**
| Archivo               | Descripción                                              |
|-----------------------|----------------------------------------------------------|
| `app.py`              | Interfaz principal del sistema con Streamlit.            |
| `gestor_datos.py`     | Manejo de datos: carga, validación y procesamiento.       |
| `analizador.py`       | Generación de estadísticas a partir de los datos.        |
| `visualizador.py`     | Visualización de datos: gráficos y tablas.               |
| `manejador_excepciones.py` | Decorador para el manejo de errores en tiempo de ejecución.|

### **Estructura de Carpetas**
```plaintext
proyecto-snies/
├── inputs/                  # Archivos Excel de entrada
├── outputs/                 # Resultados generados (descargables)
├── app.py                   # Archivo principal
├── gestor_datos.py          # Manejo de datos
├── analizador.py            # Lógica para análisis
├── visualizador.py          # Generación de visualizaciones
├── manejador_excepciones.py # Manejo de errores
├── README.md                # Manual técnico
```


### **Diagrama UML**
```mermaid
      classDiagram
          class Main {
              + run() : None
          }
      
          class AplicacionSNIES {
              + inicializar_aplicacion() : None
              + mostrar_archivos() : None
              + cargar_archivos() : None
              + ejecutar_analisis() : None
              + guardar_configuracion() : None
          }
      
          class GestorDatos {
              - ruta_directorio : str
              - min_required_columns : list
              - optional_columns : dict
              - column_synonyms : dict
              + normalizar_columnas(df) : DataFrame
              + load_data() : dict
              + rename_columns(df) : DataFrame
              + buscar_por_palabra_clave(palabras_clave, dataframes) : DataFrame
          }
      
          class GestorFiltros {
              - palabras_clave_busqueda : list
              - programas_seleccionados : list
              + buscar_por_palabra_clave(palabra_clave, dataframes) : DataFrame
              + seleccionar_programa(programa) : None
              + obtener_programas_seleccionados() : list
          }
      
          class Analizador {
              - rango_anios : tuple
              - programas_seleccionados : list
              - resultados_estadisticas : DataFrame
              + establecer_programas_seleccionados(df) : None
              + calcular_estadisticas(dataframes) : DataFrame
              + obtener_estadisticas() : DataFrame
          }
      
          class Visualizador {
              - configuracion_graficos : dict
              - datos_analizados : DataFrame
              + establecer_datos_analizados(datos) : None
              + graficar_tendencias_inscripcion() : Figure
              + graficar_comparacion_genero() : Figure
              + graficar_comparacion_modalidad() : Figure
              + exportar_excel(data) : file
              + exportar_csv(data) : file
              + exportar_json(data) : file
          }
      
          class Programa {
              - nombre : str
              - universidad : str
              - codigo_snies : int
              - nivel : str
              - campus : str
              + obtener_informacion() : str
          }
      
          class ManejadorExcepciones {
              + manejar_errores(func) : callable
              + manejar_error(error) : None
              + registrar_error(tipo_error, detalles) : None
              + mostrar_error_usuario(mensaje) : None
          }
      
          Main ..> AplicacionSNIES 
          AplicacionSNIES --> GestorDatos : "Carga datos"
          AplicacionSNIES --> GestorFiltros : "Filtra datos"
          AplicacionSNIES --> Analizador 
          AplicacionSNIES o-- Visualizador : "Genera gráficos"
          AplicacionSNIES ..> ManejadorExcepciones : "Maneja errores"
          GestorDatos --> GestorFiltros 
          Analizador *-- Programa : "Gestión de programas"
          Analizador --> Visualizador : "Entrega datos analizados"
```
