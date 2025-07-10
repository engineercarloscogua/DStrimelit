import streamlit as st 
from PIL import Image #importar la libreria PIL para manejar imagenes pill es una libreria de python para manejar imagenes y graficos https://pillow.readthedocs.io/en/stable/



#function to run the app
def main():
     
    st.title("Hacer Inputs con números")
    st.write("Esta app permite hacer inputs con números y mostrar el resultado en pantalla.")
    numero = st.number_input("Ingrese un número", min_value=0, max_value=100, value=50, step=1) # crear un input de tipo numero https://docs.streamlit.io/library/api-reference/widgets/st.number_input
    st.write(f"El número ingresado es: {numero}") # mostrar el numero ingresado en pantalla
    
    # =====HACER INPOUT CON FECHAS===
    st.write("Hacer Inputs con Fechas")
    fecha = st.date_input("Ingrese una fecha", value=None, min_value=None, max_value=None, key=None) # crear un input de tipo fecha https://docs.streamlit.io/library/api-reference/widgets/st.date_input
    st.write(f"La fecha ingresada es: {fecha}") # mostrar la fecha ingresada
   
   #======seleccionar hora ==========
    st.write("Hacer Inputs con Hora")
    hora = st.time_input("Ingrese una hora", value=None, key=None) # crear un input de tipo hora https://docs.streamlit.io/library/api-reference/widgets/st.time_input
    st.write(f"La hora ingresada es: {hora}") # mostrar la hora ingresada
    
    # ======seleccionar color=========
    st.write("Hacer Inputs con Color")
    color = st.color_picker("Seleccione un color", "#00f900") # crear un input de tipo color https://docs.streamlit.io/library/api-reference/widgets/st.color_picker
    st.write(f"El color seleccionado es: {color}") # mostrar el color seleccionado
    
# validate the app
if __name__ == "__main__": # esto asegura que el código se ejecute solo si este archivo es el principal https://docs.streamlit.io/library/api-reference/utilities/st.cache_data
    main() # run the app # esta es la funcion principal que se ejecuta al iniciar la app https://docs.streamlit.io/library/api-reference/utilities/st.main
    