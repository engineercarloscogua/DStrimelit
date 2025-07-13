# ========================
# IMPORTACIÓN DE LIBRERÍAS
# ========================
import streamlit as st               # Streamlit: para crear interfaces web fáciles de usar
import pandas as pd                 # pandas: para manejar y analizar datos tabulares
import os                           # os: para trabajar con archivos y rutas del sistema operativo
from graficas.barras import plot_bar_chart  # Función personalizada para generar un gráfico de barras

# ===============================
# FUNCIÓN PARA CARGAR EL ARCHIVO
# ===============================
@st.cache_data  # Guarda en memoria los resultados para evitar cargar el archivo muchas veces
def load_file(archivo_excel):
    """Carga un archivo Excel o CSV y lo convierte en una tabla (DataFrame)"""
    extension = os.path.splitext(archivo_excel.name)[1].lower()  # Extrae la extensión del archivo (ej: .csv)

    if extension in ['.xlsx', '.xls']:
        # Si es un archivo Excel
        return pd.read_excel(archivo_excel, engine='openpyxl')

    elif extension == '.csv':
        try:
            # Si es un archivo CSV
            return pd.read_csv(archivo_excel, encoding='utf-8')
        except UnicodeDecodeError:
            # Si hay problemas con el idioma (acentos, ñ), muestra error
            st.error("Error de codificación en el archivo CSV. Intenta con una codificación diferente.")
            return pd.DataFrame()  # Devuelve tabla vacía si hay error

    return pd.DataFrame()  # Si el archivo no es válido, devuelve tabla vacía

# ==============================
# FUNCIÓN PRINCIPAL DE LA APP
# ==============================
def ingresos():
    st.title("Carga de archivos - Análisis Temporal de Excel")  # Título principal de la app

    # Botón para limpiar la memoria caché
    if st.button("Limpiar caché"):
        st.cache_data.clear()
        st.success("Caché limpiada. Por favor, recarga la página.")

    # Botón para que el usuario suba su archivo
    archivo_excel = st.file_uploader("Sube tu archivo Excel", type=["csv", "xlsx", "xls"])

    if archivo_excel is not None:
        df = load_file(archivo_excel)  # Cargar el archivo

        # Mostrar detalles del archivo subido
        detalle_archivo = {
            "nombre_archivo": archivo_excel.name,
            "tamaño_archivo": f"{archivo_excel.size / 1024:.2f} KB"
        }
        st.write("Detalles del archivo:", detalle_archivo)
        st.write("Vista previa de los datos (primeras 5 filas):", df.head())

        # ========================
        # VALIDAR COLUMNAS NUMÉRICAS
        # ========================
        columnas_numericas = df.select_dtypes(include=['number']).columns.tolist()
        if not columnas_numericas:
            st.error("No se encontraron columnas numéricas en el archivo.")
            return

        st.write("Columnas numéricas disponibles:", ", ".join(columnas_numericas))

        # Menús para seleccionar columnas del gráfico
        opciones = ["Seleccione columna"] + columnas_numericas
        x = st.selectbox("Selecciona la columna para el eje X", opciones, index=0)
        y = st.selectbox("Selecciona la columna para el eje Y", opciones, index=0)

        # Validaciones de selección
        if x == "Seleccione columna" or y == "Seleccione columna":
            st.error("Por favor, seleccione una columna para el eje X y el eje Y.")
            return
        if x == y:
            st.error("Debe seleccionar columnas diferentes para el eje X y el eje Y.")
            return

        if not pd.api.types.is_numeric_dtype(df[x]) or not pd.api.types.is_numeric_dtype(df[y]):
            st.error("Las columnas seleccionadas deben ser numéricas.")
            return

        # =============================
        # VALIDACIÓN Y PREPARACIÓN DE DATOS
        # =============================
        if df.empty:
            st.error("El archivo cargado está vacío o no contiene datos válidos.")
            return

        max_records = len(df)  # Número total de filas en el archivo

        # Slider para elegir cuántos registros usar en el gráfico
        limit = st.slider("Selecciona el número de registros", 1, max_records, 200)

        df_limited = df[[x, y]].head(limit)  # Tomar solo las columnas seleccionadas y las primeras N filas

        if df_limited.empty or x not in df_limited.columns or y not in df_limited.columns:
            st.error("No hay datos válidos en el rango seleccionado o las columnas no están disponibles.")
            return

        # Validar valores nulos
        if df_limited[x].isnull().any() or df_limited[y].isnull().any():
            st.error("Las columnas seleccionadas contienen valores vacíos (nulos). Por favor, limpia los datos.")
            return

        # Advertencia si hay datos duplicados o no ordenados
        if df_limited[x].duplicated().any() and not df_limited[x].is_monotonic_increasing:
            st.warning("La columna del eje X tiene valores repetidos. Esto puede afectar la visualización.")

        # Validar si hay valores infinitos
        if df_limited[x].isin([float('inf'), float('-inf')]).any() or df_limited[y].isin([float('inf'), float('-inf')]).any():
            st.error("Las columnas seleccionadas contienen valores infinitos. Revisa y corrige los datos.")
            return

        # Advertencias adicionales
        if limit > max_records:
            st.error("El número de registros seleccionado excede los datos disponibles.")
            return
        if limit > 1000:
            st.warning("Seleccionaste más de 1000 registros. Esto puede hacer más lenta la visualización.")

        # =============================
        # BOTÓN PARA GENERAR EL GRÁFICO
        # =============================
        if st.button("Generar Gráfico"):
            st.info(f"El gráfico se generará con {limit} registros.")
            plot_bar_chart(
                df,
                x_column=x,
                y_column=y,
                title=f"Gráfico de {x} vs {y}",
                color="#36A2EB",
                limit=limit
            )

    else:
        # Si no se ha subido ningún archivo
        st.warning("Aún no hay archivos cargados. Por favor, sube un archivo Excel para continuar.")
