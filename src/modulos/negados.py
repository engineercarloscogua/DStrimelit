# ========================
# IMPORTACIÓN DE LIBRERÍAS
# ========================
import streamlit as st               # Streamlit: para crear interfaces web fáciles de usar
import pandas as pd                 # pandas: para manejar y analizar datos tabulares
import os                           # os: para trabajar con archivos y rutas del sistema operativo
# ========================
# IMPORTACIÓN DE MÓDULOS DE GRÁFICAS
# ========================
from graficas.barras import Barras #as #ara generar gráficos de barras
from graficas.pastel import PieChart    # Clase para generar gráficos de pastel
from graficas.dispersion import ScatterChart  # Clase para generar gráficos de dispersión
from graficas.cajas import BoxChart     # Clase para generar gráficos de cajas y bigotes
from graficas.calor import HeatmapChart # Clase para generar mapas de calor
from graficas.barras import  plot_bar_chart #nerar gráficos de barras
from processing.upload_data import FileLoader  # Clase para cargar y validar archivos Excel o CSV

def negados():
    """Función principal de la aplicación Streamlit para análisis de datos."""
    st.title("Análisis Automático de Datos - Gráficos Múltiples")

    # Instancia del cargador de archivos
    file_loader = FileLoader()

    # Botón para limpiar la caché
    if st.button("Limpiar caché"):
        st.cache_data.clear()
        st.experimental_rerun()

    # Carga del archivo
    archivo_excel = st.file_uploader("Sube tu archivo Excel o CSV", type=["csv", "xlsx", "xls"])
    
    if archivo_excel is not None:
        # Cargar el archivo usando la clase FileLoader
        df = file_loader.load_file(archivo_excel)
        
        # Mostrar detalles del archivo
        detalles = file_loader.get_file_details(archivo_excel)
        if detalles:
            st.write("Detalles del archivo:", detalles)
        
        # Mostrar vista previa de los datos
        if not df.empty:
            st.write("Vista previa de los datos (primeras 5 filas):", df.head())
        else:
            st.error("El archivo cargado está vacío o no contiene datos válidos.")
            return

        # Validar columnas
        columnas_numericas = df.select_dtypes(include=['number']).columns.tolist()
        columnas_categoricas = df.select_dtypes(include=['object', 'category']).columns.tolist()
        columnas_disponibles = columnas_numericas + columnas_categoricas

        if not columnas_numericas:
            st.error("No se encontraron columnas numéricas en el archivo.")
            return

        st.write("Columnas disponibles:", ", ".join(columnas_disponibles))

        # Slider para número de registros
        max_records = len(df)
        limit = st.slider("Selecciona el número de registros", 0, max_records, min(200, max_records))
        df_limited = df.head(limit) if limit > 0 else df

        # Secciones contraíbles para cada gráfico con botones independientes
        # Gráfico de barras
        with st.expander("**Gráfico de Barras** (Requiere 2 columnas numéricas)"):
            bar_options = ["Seleccione columna"] + columnas_numericas
            bar_x = st.selectbox("Columna para el eje X (Barras)", bar_options, key="bar_x")
            bar_y = st.selectbox("Columna para el eje Y (Barras)", [opt for opt in bar_options if opt != bar_x], key="bar_y")
            if st.button("Generar Gráfico de Barras"):
                if bar_x != "Seleccione columna" and bar_y != "Seleccione columna" and bar_x != bar_y:
                    if pd.api.types.is_numeric_dtype(df[bar_x]) and pd.api.types.is_numeric_dtype(df[bar_y]):
                        bar_chart = Barras(df_limited, x_column=bar_x, y_column=bar_y, title=f"Barras: {bar_x} vs {bar_y}")
                        bar_chart.plot_bar_chart()
                    else:
                        st.error("Para el gráfico de barras, ambas columnas deben ser numéricas.")
                else:
                    st.error("Seleccione dos columnas numéricas diferentes.")

        # Gráfico de pastel
        with st.expander("**Gráfico de Pastel** (1 columna categórica para etiquetas, 1 numérica para valores)"):
            pie_x = st.selectbox("Columna para etiquetas (Pastel)", ["Seleccione columna"] + columnas_categoricas, key="pie_x")
            pie_y = st.selectbox("Columna para valores (Pastel)", ["Seleccione columna"] + columnas_numericas, key="pie_y")
            if st.button("Generar Gráfico de Pastel"):
                if pie_x != "Seleccione columna" and pie_y != "Seleccione columna" and pie_x != pie_y:
                    if pie_x in columnas_categoricas and pd.api.types.is_numeric_dtype(df[pie_y]) and not df_limited[pie_y].lt(0).any():
                        pie_chart = PieChart(df_limited, x_column=pie_x, y_column=pie_y, title=f"Pastel: {pie_x} vs {pie_y}")
                        pie_chart.plot_pie_chart()
                    else:
                        st.error("Para el gráfico de pastel, la columna de etiquetas debe ser categórica y la de valores numérica sin negativos.")
                else:
                    st.error("Seleccione una columna categórica y una numérica diferentes.")

        # Gráfico de dispersión
        with st.expander("**Gráfico de Dispersión** (Requiere 2 columnas numéricas)"):
            scatter_options = ["Seleccione columna"] + columnas_numericas
            scatter_x = st.selectbox("Columna para el eje X (Dispersión)", scatter_options, key="scatter_x")
            scatter_y = st.selectbox("Columna para el eje Y (Dispersión)", [opt for opt in scatter_options if opt != scatter_x], key="scatter_y")
            if st.button("Generar Gráfico de Dispersión"):
                if scatter_x != "Seleccione columna" and scatter_y != "Seleccione columna" and scatter_x != scatter_y:
                    if pd.api.types.is_numeric_dtype(df[scatter_x]) and pd.api.types.is_numeric_dtype(df[scatter_y]):
                        scatter_chart = ScatterChart(df_limited, x_column=scatter_x, y_column=scatter_y, title=f"Dispersión: {scatter_x} vs {scatter_y}")
                        scatter_chart.plot_scatter_chart()
                    else:
                        st.error("Para el gráfico de dispersión, ambas columnas deben ser numéricas.")
                else:
                    st.error("Seleccione dos columnas numéricas diferentes.")

        # Gráfico de cajas y bigotes
        with st.expander("**Gráfico de Cajas y Bigotes** (Requiere 1 columna numérica)"):
            box_y = st.selectbox("Columna para valores (Cajas)", ["Seleccione columna"] + columnas_numericas, key="box_y")
            if st.button("Generar Gráfico de Cajas"):
                if box_y != "Seleccione columna":
                    if pd.api.types.is_numeric_dtype(df[box_y]):
                        box_chart = BoxChart(df_limited, y_column=box_y, title=f"Cajas: {box_y}")
                        box_chart.plot_box_chart()
                    else:
                        st.error("Para el gráfico de cajas, la columna debe ser numérica.")
                else:
                    st.error("Seleccione una columna numérica.")

        # Mapa de calor
        with st.expander("**Mapa de Calor** (Requiere al menos 2 columnas numéricas)"):
            heatmap_cols = st.multiselect("Columnas para el mapa de calor", columnas_numericas, key="heatmap_cols")
            if st.button("Generar Mapa de Calor"):
                if len(heatmap_cols) >= 2:
                    heatmap_chart = HeatmapChart(df_limited, columns=heatmap_cols, title="Mapa de Calor: Correlaciones")
                    heatmap_chart.plot_heatmap()
                else:
                    st.error("Selecciona al menos dos columnas numéricas para el mapa de calor.")

    else:
        st.warning("Aún no hay archivos cargados. Por favor, sube un archivo Excel o CSV.")

if __name__ == "__main__":
    negados()