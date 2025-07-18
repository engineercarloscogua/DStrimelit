# ========================
# IMPORTACIÓN DE LIBRERÍAS
# ========================
import streamlit as st               # Streamlit: para crear interfaces web fáciles de usar
import pandas as pd                 # pandas: para manejar y analizar datos tabulares
import os                           # os: para trabajar con archivos y rutas del sistema operativo
from graficas.barras import plot_bar_chart  # Función personalizada para generar un gráfico de barras
from graficas.pastel import PieChart  # Clase para generar gráficos de pastel

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
def negados():
    st.title("Carga de archivos - Análisis Temporal de Excel")  # Título principal de la app

    # Botón para limpiar la memoria caché
    if st.button("Limpiar caché"):
        st.cache_data.clear()
        st.experimental_rerun()  # Recarga la página automáticamente

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
        # VALIDAR COLUMNAS
        # ========================
        columnas_numericas = df.select_dtypes(include=['number']).columns.tolist()
        columnas_categoricas = df.select_dtypes(include=['object', 'category']).columns.tolist()
        columnas_disponibles = columnas_numericas + columnas_categoricas

        if not columnas_numericas:
            st.error("No se encontraron columnas numéricas en el archivo.")
            return

        st.write("Columnas disponibles:", ", ".join(columnas_disponibles))

        # Menús para seleccionar tipo de gráfico y columnas
        chart_type = st.selectbox("Tipo de gráfico", ["Barras", "Pastel"], index=0)
        opciones = ["Seleccione columna"] + columnas_disponibles
        x = st.selectbox("Selecciona la columna para el eje X (o etiquetas)", opciones, index=0)
        y = st.selectbox("Selecciona la columna para el eje Y (o valores)", opciones, index=0)

        # Validaciones de selección
        if x == "Seleccione columna" or y == "Seleccione columna":
            st.error("Por favor, seleccione una columna para el eje X y el eje Y.")
            return
        if x == y:
            st.error("Debe seleccionar columnas diferentes para el eje X y el eje Y.")
            return

        # Validaciones específicas por tipo de gráfico
        if chart_type == "Barras":
            if not pd.api.types.is_numeric_dtype(df[x]) or not pd.api.types.is_numeric_dtype(df[y]):
                st.error("Para gráficos de barras, ambas columnas deben ser numéricas.")
                return
        elif chart_type == "Pastel":
            if not pd.api.types.is_numeric_dtype(df[y]):
                st.error("Para gráficos de pastel, la columna de valores (Y) debe ser numérica.")
                return
            if df[y].lt(0).any():
                st.error("Los valores en la columna Y no pueden ser negativos para un gráfico de pastel.")
                return

        # =============================
        # VALIDACIÓN Y PREPARACIÓN DE DATOS
        # =============================
        if df.empty:
            st.error("El archivo cargado está vacío o no contiene datos válidos.")
            return

        max_records = len(df)  # Número total de filas en el archivo

        # Slider para elegir cuántos registros usar en el gráfico
        limit = st.slider("Selecciona el número de registros", 1, max_records, min(200, max_records))

        df_limited = df[[x, y]].head(limit)  # Tomar solo las columnas seleccionadas y las primeras N filas

        if df_limited.empty or x not in df_limited.columns or y not in df_limited.columns:
            st.error("No hay datos válidos en el rango seleccionado o las columnas no están disponibles.")
            return

        # Validar valores nulos
        if df_limited[x].isnull().any() or df_limited[y].isnull().any():
            st.error("Las columnas seleccionadas contienen valores vacíos (nulos). Por favor, limpia los datos.")
            return

        # Validar si hay valores infinitos
        if df_limited[y].isin([float('inf'), float('-inf')]).any():
            st.error("Las columnas seleccionadas contienen valores infinitos. Revisa y corrige los datos.")
            return

        # Advertencia si hay datos duplicados (solo para barras)
        if chart_type == "Barras" and df_limited[x].duplicated().any() and not df_limited[x].is_monotonic_increasing:
            st.warning("La columna del eje X tiene valores repetidos. Esto puede afectar la visualización.")

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
            if chart_type == "Barras":
                plot_bar_chart(
                    df,
                    x_column=x,
                    y_column=y,
                    title=f"Gráfico de {x} vs {y}",
                    color="#36A2EB",
                    limit=limit
                )
            elif chart_type == "Pastel":
                pie_chart = PieChart(
                    df,
                    x_column=x,
                    y_column=y,
                    title=f"Gráfico de {x} vs {y}",
                    color="#36A2EB",
                    limit=limit
                )
                pie_chart.plot_pie_chart()

    else:
        # Si no se ha subido ningún archivo
        st.warning("Aún no hay archivos cargados. Por favor, sube un archivo Excel para continuar.")