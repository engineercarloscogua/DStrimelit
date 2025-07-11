import streamlit as st # impostando la librería Streamlit
import pandas as pd # importando la librería Pandas para manejar datos
from PIL import Image # importando la librería PIL para manejar imágenes
import docx2txt # importando la librería docx2txt para manejar archivos DOCX
from PyPDF2 import PdfReader # importando la librería PyPDF2 para manejar archivos PDF

#  ///////////////////////FUNCONES PARA GARGES/////////////////////
@st.cache_data # Decorador para cachear los datos y mejorar el rendimiento
def cargar_archivo(image_file):# función para cargar un archivo de imagen
    img = Image.open(image_file) # Abriendo la imagen
    return img # Retornando la imagen abierta

# leer pdf
def leer_pdf(file):
    pdf_reader = PdfReader(file) # Creando un lector de PDF
    count = len(pdf_reader.pages) # Contando las páginas del PDF
    todo_el_texto ="" # Variable para almacenar todo el texto extraído
    for i in range(count): # Iterando sobre cada página  
        pagina = pdf_reader.pages[i] # Obteniendo la página
        todo_el_texto += pagina.extract_text() # Extrayendo el texto de la página
    return todo_el_texto # Retornando el texto extraído    

# ////////////////////////////////FUNCONES PARA GARGES////////////////////////
def main(): #  Función principal del script
    st.title("Carga de archivos")    
    # =====MENÚ DE SELECCIÓN DE ARCHIVOS DEL NAVEGADOR VERTICAL======
    menu = ["Imagen", "PDF","EXCEL", "DOCX"] # Lista de tipos de archivos
    #sidebar.selectbox permite al usuario seleccionar un tipo de archivo en un menú desplegable
    eleccion = st.sidebar.selectbox("Selecciona el tipo de archivo", menu)# variable para almacenar la selección del usuario
    
    #=====CARGUE DE ARCHIVOS DE IMAGEN============
    if eleccion == "Imagen":# Si el usuario selecciona "Imagen"
        st.subheader("Cargar una imagen") # Subtítulo para la sección de imágenes
        archivo_imagen = st.file_uploader("Sube tu imagen", type=["jpg", "jpeg", "png"]) # Permite al usuario subir una imagen con extensiones jpg, jpeg o png
        
        #======Validación de la imagen subida=========== si no hay imagen omita esto
        if archivo_imagen is not None: # Si se ha subido un archivo
            detalle_archivo = {"nombre_archivo": archivo_imagen.name, # Nombre del archivo
                            "tipo_archivo": archivo_imagen.type, # Tipo de archivo
                            "tamaño_archivo": archivo_imagen.size} # Tamaño del archivo
            st.write(detalle_archivo) # Muestra los detalles del archivo subido
            # Muestra la imagen cargada con un título y ajusta el ancho de la columna
            st.image(cargar_archivo(archivo_imagen), caption="Imagen cargada", use_container_width=True) 
   
    #=====CARGUE DE ARCHIVOS EXCEL ===========
    elif eleccion == "EXCEL": # Si el usuario selecciona "EXCEL"
        st.subheader("Cargar un archivo Excel") # Subtítulo para la sección de Excel
        # Permite al usuario subir un archivo Excel con extensiones CSV, xlsx o xls
        archivo_excel = st.file_uploader("Sube tu archivo Excel", type=["CSV","xlsx", "xls"])
        # Validación para asegurarse de que se ha subido un archivo Excel
        if archivo_excel is not None: # Si se ha subido un archivo Excel
            detalle_archivo_excel = {"nombre_archivo": archivo_excel.name, # Nombre del archivo
                                    "tipo_archivo": archivo_excel.type, # Tipo de archivo
                                    "tamaño_archivo": archivo_excel.size} # Tamaño del archivo
            st.write(detalle_archivo_excel) # Muestra los detalles del archivo subido
            
            #====validando el tipo de archivo Excel y cargando el DataFrame========
            if archivo_excel.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": # Si el archivo es un Excel xlsx
                df = pd.read_excel(archivo_excel) # Carga el archivo Excel en un DataFrame
            elif archivo_excel.type == "application/vnd.ms-excel": # Si el archivo es un Excel xls
                df = pd.read_excel(archivo_excel, engine='xlrd') # Carga el archivo Excel en un DataFrame usando el motor xlrd
            elif archivo_excel.type == "text/csv": # Si el archivo es un CSV  
                df = pd.read_csv(archivo_excel) # Carga el archivo CSV en un DataFrame
            else:
                df = pd.DataFrame() # Si el tipo de archivo no es reconocido, crea un DataFrame vacío
                st.error("Tipo de archivo no soportado. Por favor, sube un archivo Excel o CSV.") 
            st.dataframe(df) # Muestra el DataFrame en la aplicación 
    
    """    
    #=====Validación de PDF ===========
    elif eleccion == "PDF": # Si el usuario selecciona "PDF"
        st.subheader("Cargar un archivo PDF") # Subtítulo para la sección de PDF
        archivo_pdf = st.file_uploader("Sube tu PDF", type=["pdf"]) # Permite al usuario subir un archivo PDF
        
    #=====Validación de DOCX ===========
    elif eleccion == "DOCX": # Si el usuario selecciona "DOCX"
        st.subheader("Cargar un archivo DOCX") # Subtítulo para la sección
    """
    
    
    
if __name__ == "__main__": # Punto de entrada del script
    main() # Llamando a la función principal
    
        

    