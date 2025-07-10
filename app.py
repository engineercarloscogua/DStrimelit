import streamlit as st 

from PIL import Image # importar la libreria PIL para manejar imagenes

icono = Image.open("multimedia/icono.png") # abrir la imagen de streamlit
st.set_page_config(page_title="App Inge Carlos",
                   page_icon= icono, #icono de la app
                   layout="wide" # configurar el layout de la app https://docs.streamlit.io/library/api-reference/layout/st.set_page_config
                   ) # configurar la pagina de la app https://docs.streamlit.io/library/api-reference/layout/st.set_page_config


#function to run the app
def main():
     
    st.title("Hacer Inputs con números")
    st.write("Esta app permite hacer inputs con números y mostrar el resultado en pantalla.")
    numero = st.number_input("Ingrese un número", min_value=0, max_value=100, value=50, step=1) # crear un input de tipo numero https://docs.streamlit.io/library/api-reference/widgets/st.number_input
    st.write(f"El número ingresado es: {numero}") # mostrar el numero ingresado en pantalla
  
    
# validate the app
if __name__ == "__main__": # esto asegura que el código se ejecute solo si este archivo es el principal https://docs.streamlit.io/library/api-reference/utilities/st.cache_data
    main() # run the app # esta es la funcion principal que se ejecuta al iniciar la app https://docs.streamlit.io/library/api-reference/utilities/st.main
    