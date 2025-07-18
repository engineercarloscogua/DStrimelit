import plotly.express as px
import streamlit as st
import pandas as pd

class PieChart:
    """Clase para generar y mostrar gráficos de pastel usando Plotly."""
    
    def __init__(self, df, x_column, y_column, title, color="#36A2EB", limit=200):
        """
        Inicializa el gráfico de pastel.
        
        Args:
            df (pd.DataFrame): DataFrame con los datos.
            x_column (str): Nombre de la columna para las etiquetas (categórica o numérica).
            y_column (str): Nombre de la columna para los valores (numérica).
            title (str): Título del gráfico.
            color (str): Color base para el gráfico.
            limit (int): Número máximo de registros a usar.
        """
        self.df = df
        self.x_column = x_column
        self.y_column = y_column
        self.title = title
        self.color = color
        self.limit = limit

    def validate_data(self):
        """Valida los datos para el gráfico de pastel."""
        if self.df.empty:
            st.error("El DataFrame está vacío.")
            return False
        
        if self.x_column not in self.df.columns or self.y_column not in self.df.columns:
            st.error("Las columnas seleccionadas no están en el DataFrame.")
            return False
        
        if not pd.api.types.is_numeric_dtype(self.df[self.y_column]):
            st.error("La columna de valores (Y) debe ser numérica.")
            return False
        
        if self.df[self.y_column].lt(0).any():
            st.error("Los valores en la columna Y no pueden ser negativos para un gráfico de pastel.")
            return False
        
        if self.df[self.x_column].isnull().any() or self.df[self.y_column].isnull().any():
            st.error("Las columnas contienen valores nulos. Por favor, limpia los datos.")
            return False
        
        if self.df[self.y_column].isin([float('inf'), float('-inf')]).any():
            st.error("La columna de valores contiene valores infinitos.")
            return False
        
        return True

    def plot_pie_chart(self):
        """Genera y muestra el gráfico de pastel."""
        if not self.validate_data():
            return
        
        # Limitar los datos
        df_limited = self.df[[self.x_column, self.y_column]].head(self.limit)
        
        # Crear el gráfico de pastel con Plotly
        fig = px.pie(
            df_limited,
            names=self.x_column,
            values=self.y_column,
            title=self.title,
            color_discrete_sequence=[self.color]
        )
        
        # Configurar el diseño
        fig.update_traces(textinfo='percent+label')
        fig.update_layout(
            showlegend=True,
            title_x=0.5,
            margin=dict(t=50, b=50, l=50, r=50)
        )
        
        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig, use_container_width=True)