import streamlit as st 

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
  
    
# validate the app
if __name__ == "__main__": # esto asegura que el código se ejecute solo si este archivo es el principal https://docs.streamlit.io/library/api-reference/utilities/st.cache_data
    main() # run the app # esta es la funcion principal que se ejecuta al iniciar la app https://docs.streamlit.io/library/api-reference/utilities/st.main
    