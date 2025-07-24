import plotly.figure_factory as ff
import streamlit as st
import pandas as pd
import numpy as np

class HeatmapChart:
    """Clase para generar y mostrar mapas de calor usando Plotly."""
    
    def __init__(self, df, columns, title):
        """
        Inicializa el mapa de calor.
        
        Args:
            df (pd.DataFrame): DataFrame con los datos.
            columns (list): Lista de columnas numéricas para la correlación.
            title (str): Título del gráfico.
        """
        self.df = df
        self.columns = columns
        self.title = title

    def validate_data(self):
        """Valida los datos para el mapa de calor."""
        if self.df.empty:
            st.error("El DataFrame está vacío.")
            return False
        if not all(col in self.df.columns for col in self.columns):
            st.error("Algunas columnas seleccionadas no están en el DataFrame.")
            return False
        if not all(pd.api.types.is_numeric_dtype(self.df[col]) for col in self.columns):
            st.error("Todas las columnas deben ser numéricas para el mapa de calor.")
            return False
        if self.df[self.columns].isnull().any().any():
            st.error("Las columnas contienen valores nulos.")
            return False
        if self.df[self.columns].isin([float('inf'), float('-inf')]).any().any():
            st.error("Las columnas contienen valores infinitos.")
            return False
        if len(self.columns) < 2:
            st.error("Se requieren al menos dos columnas para el mapa de calor.")
            return False
        return True

    def plot_heatmap(self):
        """Genera y muestra el mapa de calor."""
        if not self.validate_data():
            return
        # Calcular la matriz de correlación
        corr_matrix = self.df[self.columns].corr()
        # Crear mapa de calor con Plotly
        fig = ff.create_annotated_heatmap(
            z=np.round(corr_matrix.values, 2),
            x=self.columns,
            y=self.columns,
            colorscale='Viridis',
            showscale=True,
            annotation_text=np.round(corr_matrix.values, 2)
        )
        fig.update_layout(
            title=self.title,
            title_x=0.5,
            xaxis=dict(tickangle=45),
            yaxis=dict(tickangle=0),
            margin=dict(t=100, b=100, l=100, r=100)
        )
        st.plotly_chart(fig, use_container_width=True)