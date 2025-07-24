import streamlit as st  # Streamlit: para crear interfaces web fáciles de usar
import pandas as pd  # pandas: para manejar y analizar datos tabulares
import os  # os: para trabajar con archivos y rutas del sistema operativo

# ========================
# CLASE PARA CARGAR ARCHIVOS
# ========================
class FileLoader:
    """Clase para cargar y validar archivos Excel o CSV en un DataFrame de pandas."""
    
    @staticmethod
    @st.cache_data
    def load_file(archivo_excel):
        """Carga un archivo Excel o CSV y lo convierte en un DataFrame.
        
        Args:
            archivo_excel: Archivo subido por el usuario (Excel o CSV).
        
        Returns:
            pd.DataFrame: DataFrame con los datos del archivo o DataFrame vacío si hay error.
        """
        if archivo_excel is None:
            return pd.DataFrame()
        
        extension = os.path.splitext(archivo_excel.name)[1].lower()
        try:
            if extension in ['.xlsx', '.xls']:
                return pd.read_excel(archivo_excel, engine='openpyxl')
            elif extension == '.csv':
                return pd.read_csv(archivo_excel, encoding='utf-8')
        except UnicodeDecodeError:
            st.error("Error de codificación en el archivo CSV. Intenta con una codificación diferente.")
            return pd.DataFrame()
        except Exception as e:
            st.error(f"Error al cargar el archivo: {str(e)}")
            return pd.DataFrame()
        
    @staticmethod
    def get_file_details(archivo_excel):
        """Devuelve detalles del archivo cargado.
        
        Args:
            archivo_excel: Archivo subido por el usuario.
        
        Returns:
            dict: Diccionario con nombre y tamaño del archivo.
        """
        if archivo_excel is None:
            return {}
        return {
            "nombre_archivo": archivo_excel.name,
            "tamaño_archivo": f"{archivo_excel.size / 1024:.2f} KB"
        }