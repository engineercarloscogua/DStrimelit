import plotly.express as px #esta libreria se utiliza para crear gráficos interactivos de manera sencilla.
import streamlit as st # Streamlit se utiliza para crear aplicaciones web interactivas de ciencia de datos.
import pandas as pd # Pandas se utiliza para la manipulación y análisis de datos.
import numpy as np # NumPy se utiliza para operaciones numéricas y manejo de arreglos.


class Barras: #clase que se encarga dede generar y mostrar gráficos de barras usando Plotly.
    """Clase para generar y mostrar gráficos de barras usando Plotly."""

    def __init__( # Constructor de la clase Barras
                 
        # define los parámetros de inicialización
        self, # Inicializa el gráfico de barras.
        df: pd.DataFrame, # DataFrame con los datos.
        x_column: str, # Columna para el eje X.
        y_column: str, # Columna para el eje Y.
        title: str, # Título del gráfico.
        color: str = "#36A2EB", # Color base para el gráfico (hex o nombre CSS).
    ) -> None: # -> hace referencia al tipo de retorno de la función.
        """
        Inicializa el gráfico de barras.

        Args:
            df: DataFrame con los datos.
            x_column: Columna para el eje X.
            y_column: Columna para el eje Y.
            title: Título del gráfico.
            color: Color base para el gráfico (hex o nombre CSS).
        """
        # Asignación de atributos de instancia, que son enviados al constructor
        self.df = df # DataFrame con los datos
        self.x_column = x_column # Columna para el eje X
        self.y_column = y_column # Columna para el eje Y
        self.title = title # Título del gráfico
        self.color = color # Color base para el gráfico (hex o nombre CSS)

    # Método para validar los datos antes de generar el gráfico
    def validate_data(self) -> bool:  #función que valida los datos para el gráfico de barras. 
        """Valida los datos para el gráfico de barras."""
        if self.df.empty: # Verifica si el DataFrame está vacío
            st.error("El DataFrame está vacío.") # manejo de errores en Streamlit
            return False # Retorna False si el DataFrame está vacío
        # Verificar si las columnas existen en el DataFrame
        if self.x_column not in self.df.columns or self.y_column not in self.df.columns:
            st.error("Las columnas seleccionadas no están en el DataFrame.") #
            return False # Retorna False si alguna columna no está en el DataFrame

        # Verificar nulos
        # Verifica si las columnas seleccionadas contienen valores nulos
        if self.df[self.x_column].isnull().any() or self.df[self.y_column].isnull().any():
            st.error("Las columnas contienen valores nulos.") 
            return False

        # Verificar valores finitos en Y
        if not np.isfinite(self.df[self.y_column]).all():
            st.error("La columna de valores contiene valores no finitos (inf o NaN).")
            return False

        return True

    def plot_bar_chart(self) -> None:
        """Genera y muestra el gráfico de barras en Streamlit."""
        if not self.validate_data():
            return

        fig = px.bar(
            self.df,
            x=self.x_column,
            y=self.y_column,
            title=self.title,
            color_discrete_sequence=[self.color],
        )
        fig.update_layout(
            xaxis_title=self.x_column,
            yaxis_title=self.y_column,
            title_x=0.5,
        )
        st.plotly_chart(fig, use_container_width=True)


# --- Wrapper funcional para compatibilidad con importación existente ---
def plot_bar_chart(df, x_column, y_column, title, color="#36A2EB"):
    """
    Wrapper que permite importar directamente plot_bar_chart
    desde modulos.ingresos sin cambiar el código existente.
    """
    grafico = Barras(df, x_column, y_column, title, color=color)
    grafico.plot_bar_chart()
