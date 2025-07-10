import streamlit as st 
import pandas as pd


#function to run the app
def main(): 
    # 1. ====Agregando Selectbox ===
    st.title("Selección") # titulo de la app
    opcion = st.selectbox(
        'Selecciona una opción',
        ['Coco', 'Piña', 'Avocado']
    )
    #mostrar la opción seleccionada
    st.write(f'Has seleccionado:{opcion}')
    
    # 2.=====MULTIPLE SELECTBOX=====
    st.title("Selección Múltiple") # titulo de la app
    opciones2 = st.multiselect(
        'Selecciona una o más opciones',
        ['Coco', 'Piña', 'Avocado']
    )
    #mostrar las opciones seleccionadas
    st.write(f'Has seleccionado: {opciones2}')
    
    # 3. =====SLIDER=====
    st.title("Slider") # titulo de la app
    valor = st.slider(
        'Seleccione su edad',
        0, 100, 25 # min, max, default        
    )
    #mostrar el valor seleccionado
    st.write(f'Has seleccionado: {valor}')
    
# validate the app
if __name__ == "__main__": # esto asegura que el código se ejecute solo si este archivo es el principal https://docs.streamlit.io/library/api-reference/utilities/st.cache_data
    main() # run the app # esta es la funcion principal que se ejecuta al iniciar la app https://docs.streamlit.io/library/api-reference/utilities/st.main
    