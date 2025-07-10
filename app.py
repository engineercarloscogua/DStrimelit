import streamlit as st 
from PIL import Image #importar la libreria PIL para manejar imagenes pill es una libreria de python para manejar imagenes y graficos https://pillow.readthedocs.io/en/stable/



#function to run the app
def main(): 
    # 1. ====Agregando Selectbox ===
    st.title("Manejo de multimedia") # titulo de la app
    img = Image.open("multimedia/imagen.png") # abrir la imagen con PIL
    st.image(img, caption="Imagen de ejemplo", use_container_width = True) # mostrar la imagen en la app con un caption y ajustando el ancho de la columna https://docs.streamlit.io/library/api-reference/layout/st.image
    
    #=====Mostrar imagen radom de internet====
    st.subheader("Imagen aleatoria de internet") # subtitulo de la seccion
    st.image("https://picsum.photos/150/150", caption="Imagen aleatoria de internet", use_container_width = True) # mostrar una imagen aleatoria de internet con un caption y ajustando el ancho de la columna https://docs.streamlit.io/library/api-reference/layout/st.image
    
    
# validate the app
if __name__ == "__main__": # esto asegura que el código se ejecute solo si este archivo es el principal https://docs.streamlit.io/library/api-reference/utilities/st.cache_data
    main() # run the app # esta es la funcion principal que se ejecuta al iniciar la app https://docs.streamlit.io/library/api-reference/utilities/st.main
    