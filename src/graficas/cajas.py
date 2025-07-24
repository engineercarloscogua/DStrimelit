import plotly.express as px
import streamlit as st
import pandas as pd

class BoxChart:
    """Clase para generar y mostrar gráficos de cajas y bigotes usando Plotly."""
    
    def __init__(self, df, y_column, title, color="#36A2EB"):
        """
        Inicializa el gráfico de cajas y bigotes.
        
        Args:
            df (pd.DataFrame): DataFrame con los datos.
            y_column (str): Columna para los valores.
            title (str): Título del gráfico.
            color (str): Color base para el gráfico.
        """
        self.df = df
        self.y_column = y_column
        self.title = title
        self.color = color

    def validate_data(self):
        """Valida los datos para el gráfico de cajas."""
        if self.df.empty:
            st.error("El DataFrame está vacío.")
            return False
        if self.y_column not in self.df.columns:
            st.error("La columna seleccionada no está en el DataFrame.")
            return False
        if not pd.api.types.is_numeric_dtype(self.df[self.y_column]):
            st.error("La columna debe ser numérica para el gráfico de cajas.")
            return False
        if self.df[self.y_column].isnull().any():
            st.error("La columna contiene valores nulos.")
            return False
        if self.df[self.y_column].isin([float('inf'), float('-inf')]).any():
            st.error("La columna contiene valores infinitos.")
            return False
        return True

    def plot_box_chart(self):
        """Genera y muestra el gráfico de cajas y bigotes."""
        if not self.validate_data():
            return
        fig = px.box(
            self.df,
            y=self.y_column,
            title=self.title,
            color_discrete_sequence=[self.color]
        )
        fig.update_layout(
            yaxis_title=self.y_column,
            title_x=0.5
        )
        st.plotly_chart(fig, use_container_width=True)