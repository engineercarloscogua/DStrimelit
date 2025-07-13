# ========================
# IMPORTACIÓN DE LIBRERÍAS
# ========================
import streamlit as st   # Para construir interfaces web interactivas
import pandas as pd      # Para manejar datos en forma de tablas

# ========================
# FUNCIÓN PARA GRAFICAR
# ========================
@st.cache_data  # Guarda el resultado del gráfico en memoria (para que se cargue más rápido si no ha cambiado)
def plot_bar_chart(df, x_column, y_column, title="Diagrama de Barras", color="#36A2EB", limit=200):
    """
    Esta función genera un gráfico de barras a partir de una tabla (DataFrame).
    
    Parámetros:
    - df (pd.DataFrame): La tabla de datos.
    - x_column (str): Nombre de la columna que se mostrará en el eje X (categorías).
    - y_column (str): Nombre de la columna que se mostrará en el eje Y (valores).
    - title (str): Título del gráfico (opcional).
    - color (str): Color de las barras (opcional, valor por defecto es azul).
    - limit (int): Número máximo de registros a mostrar en el gráfico (opcional).
    """

    # =========================
    # VALIDACIÓN DE LOS DATOS
    # =========================
    if df.empty or x_column not in df.columns or y_column not in df.columns:
        st.error("DataFrame vacío o columnas no válidas.")
        return  # Sale de la función si no hay datos válidos

    # ==========================
    # PREPARAR LOS DATOS A USAR
    # ==========================
    df_limited = df[[x_column, y_column]].head(limit)  # Toma solo las dos columnas necesarias y los primeros N registros

    # ====================
    # MOSTRAR EL GRÁFICO
    # ====================
    st.write(f"### {title}")  # Muestra el título del gráfico en la página

    # Crea un gráfico de barras:
    # - Establece la columna del eje X como índice
    # - Muestra los valores de la columna del eje Y como altura de las barras
    st.bar_chart(df_limited.set_index(x_column)[y_column])
