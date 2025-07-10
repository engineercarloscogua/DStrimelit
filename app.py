import streamlit as st 
import pandas as pd
import requests # Para hacer solicitudes HTTP a la API
#Lectura de datos desde api  
#df =pd.read_excel("mer_con_neg_2018_2024.xlsx") #read the excel file with pandas
# URL de la API
url = "https://www.datos.gov.co/resource/v534-yr4y.json"
# Realizar la solicitud GET
response = requests.get(url)

#function to run the app
def main():
    # Validar que la solicitud fue exitosa
    if response.status_code == 200: #200 es el codigo de estado HTTP para una solicitud exitosa
        st.header("Datos de la API")
        data = response.json()  # Convertir respuesta a JSON
        df = pd.DataFrame(data)  # Convertir JSON a DataFrame
        st.dataframe(df)# muestra dataframe en la app
        #---- mostrar primeros 5 registros del dataframe
        st.subheader("Primeros 5 registros")       
        st.dataframe(df.head())              
    else:
        print("Error al consultar la API:", response.status_code)
        
    # ======Mostrar datos Json en la app
    st.subheader("Datos JSON")  
    st.json({'nombre': 'Carlos'}) # muestra un objeto JSON en la app https://docs.streamlit.io/library/api-reference/data/st.json
    
    # ====== Mostrar codigos de programacion
    st.subheader("Codigo de programacion")  
    
    codigo = """
        print("Hola, mundo!")
        for i in range(5):
            print(i)
    """
    st.code(codigo, language='python') #muestra el codigo en la app https://docs.streamlit.io/library/api-reference/data/st.code
    
# validate the app
if __name__ == "__main__": # esto asegura que el código se ejecute solo si este archivo es el principal https://docs.streamlit.io/library/api-reference/utilities/st.cache_data
    main() # run the app # esta es la funcion principal que se ejecuta al iniciar la app https://docs.streamlit.io/library/api-reference/utilities/st.main
    