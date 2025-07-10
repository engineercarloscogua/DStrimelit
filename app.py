import streamlit as st 
from PIL import Image #importar la libreria PIL para manejar imagenes pill es una libreria de python para manejar imagenes y graficos https://pillow.readthedocs.io/en/stable/



#function to run the app
def main():
     
    st.title("Hacer Inputs")
    nombre = st.text_input("Ingresa tu nombre") # crear un input de texto para ingresar el nombre https://docs.streamlit.io/library/api-reference/widgets/st.text_input
    st.write(f"Hola {nombre}, bienvenido a la app!") # mostrar un mensaje de bienvenida con el nombre ingresado https://docs.streamlit.io/library/api-reference/text/st.write

    #======Area de texto======
    st.subheader("Area de texto") # subtitulo de la seccion
    descripcion = st.text_area("Ingresa una descripcion", height= 90) # crear un area de texto para ingresar una descripcion con 90 px de altura el mensaje https://docs.streamlit.io/library/api-reference/widgets/st.text_area
    st.write(f"Descripcion: {descripcion}") # mostrar la descripcion ingresada

# validate the app
if __name__ == "__main__": # esto asegura que el código se ejecute solo si este archivo es el principal https://docs.streamlit.io/library/api-reference/utilities/st.cache_data
    main() # run the app # esta es la funcion principal que se ejecuta al iniciar la app https://docs.streamlit.io/library/api-reference/utilities/st.main
    