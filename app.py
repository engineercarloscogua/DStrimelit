import streamlit as st 
import plotly.express as px # importar la libreria plotly para graficos interactivos
import pandas as pd # importar la libreria pandas para manejar datos

from PIL import Image # importar la libreria PIL para manejar imagenes

icono = Image.open("multimedia/icono.png") # abrir la imagen de streamlit
st.set_page_config(page_title="App Inge Carlos",
                   page_icon= icono, #icono de la app
                   layout="wide",
                   initial_sidebar_state="collapsed" # menu contraido https://docs.streamlit.io/library/api-reference/layout/st.sidebar
                   ) # configurar la pagina de la app https://docs.streamlit.io/library/api-reference/layout/st.set_page_config


#function to run the app
def main():
     
    st.title("Dashboard del Inge Carlos") # titulo de la app https://docs.streamlit.io/library/api-reference/layout/st.title    
    #menu de navegacion
    st.sidebar.header("Navegacion") # encabezado del menu de navegacion https://docs.streamlit.io/library/api-reference/layout/st.sidebar.header
    #creando dataframe 
    df = pd.read_excel("mer_con_neg_2018_2024.xlsx")
    st.dataframe(df) # mostrar el dataframe en la app https://docs.streamlit.io/library/api-reference/data/st.dataframe
    
    # =====Agrupación por NOV ====
    st.header("Agrupación por tipo de documento") # encabezado de la seccion de agrupacion por NOV    
    # Agrupar por tip_doc y contar cuántos registros hay por cada uno en un nuevo df
    df_nov = df.groupby("tip_doc").size().reset_index(name="total") #reset index para que el resultado sea un dataframe y no una serie, name = "total" para renombrar la columna de conteo https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
    st.dataframe(df_nov) # mostrar el dataframe agrupado en la app
    
    # ====Crear la gráfica de pastel=====
    fig = px.pie(df_nov, 
                values="total", # valores a graficar
                names="tip_doc", # nombres de las categorías
                title="Total por Novedades", # título de la gráfica
                color_discrete_sequence=px.colors.qualitative.Pastel)# https://plotly.com/python/pie-charts/

    # Mostrar la gráfica en Streamlit
    st.plotly_chart(fig, use_container_width=True)
# validate the app
if __name__ == "__main__": # esto asegura que el código se ejecute solo si este archivo es el principal https://docs.streamlit.io/library/api-reference/utilities/st.cache_data
    main() # run the app # esta es la funcion principal que se ejecuta al iniciar la app https://docs.streamlit.io/library/api-reference/utilities/st.main
    