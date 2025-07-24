import plotly.express as px
import streamlit as st
import pandas as pd

class ScatterChart:
    """Clase para generar y mostrar gráficos de dispersión usando Plotly."""
    
    def __init__(self, df, x_column, y_column, title, color="#36A2EB"):
        """
        Inicializa el gráfico de dispersión.
        
        Args:
            df (pd.DataFrame): DataFrame con los datos.
            x_column (str): Columna para el eje X.
            y_column (str): Columna para el eje Y.
            title (str): Título del gráfico.
            color (str): Color base para el gráfico.
        """
        self.df = df
        self.x_column = x_column
        self.y_column = y_column
        self.title = title
        self.color = color

    def validate_data(self):
        """Valida los datos para el gráfico de dispersión."""
        if self.df.empty:
            st.error("El DataFrame está vacío.")
            return False
        if self.x_column not in self.df.columns or self.y_column not in self.df.columns:
            st.error("Las columnas seleccionadas no están en el DataFrame.")
            return False
        if not pd.api.types.is_numeric_dtype(self.df[self.x_column]) or not pd.api.types.is_numeric_dtype(self.df[self.y_column]):
            st.error("Ambas columnas deben ser numéricas para el gráfico de dispersión.")
            return False
        if self.df[self.x_column].isnull().any() or self.df[self.y_column].isnull().any():
            st.error("Las columnas contienen valores nulos.")
            return False
        if self.df[self.y_column].isin([float('inf'), float('-inf')]).any() or self.df[self.x_column].isin([float('inf'), float('-inf')]).any():
            st.error("Las columnas contienen valores infinitos.")
            return False
        return True

    def plot_scatter_chart(self):
        """Genera y muestra el gráfico de dispersión."""
        if not self.validate_data():
            return
        fig = px.scatter(
            self.df,
            x=self.x_column,
            y=self.y_column,
            title=self.title,
            color_discrete_sequence=[self.color]
        )
        fig.update_layout(
            xaxis_title=self.x_column,
            yaxis_title=self.y_column,
            title_x=0.5
        )
        st.plotly_chart(fig, use_container_width=True)