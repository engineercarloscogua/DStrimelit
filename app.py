import streamlit as st 
from PIL import Image #importar la libreria PIL para manejar imagenes pill es una libreria de python para manejar imagenes y graficos https://pillow.readthedocs.io/en/stable/



#function to run the app
def main(): 
    
    st.title("Videos")
    with open("multimedia/video.mp4", "rb") as file: # abre el archivo de video en modo lectura binaria https://docs.python.org/3/library/functions.html#open
       st.video(file.read(), start_time=0) # lee el archivo los muestra en el tiempo 0 segundos https://docs.streamlit.io/library/api-reference/media/st.video
    
    # ====Audio ====
    st.title("Audio")
    with open("multimedia/audio.mp3", "rb") as file: # abre el archivo de audio en modo lectura binaria https://docs.python.org/3/library/functions.html#open
        st.audio(file.read(), format="audio/mp3") # lee el archivo y lo muestra en formato mp3 https://docs.streamlit.io/library/api-reference/media/st.audio
    
# validate the app
if __name__ == "__main__": # esto asegura que el código se ejecute solo si este archivo es el principal https://docs.streamlit.io/library/api-reference/utilities/st.cache_data
    main() # run the app # esta es la funcion principal que se ejecuta al iniciar la app https://docs.streamlit.io/library/api-reference/utilities/st.main
    