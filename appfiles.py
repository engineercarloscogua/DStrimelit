import streamlit as st # impostando la librería Streamlit
import pandas as pd # importando la librería Pandas para manejar datos
from PIL import Image # importando la librería PIL para manejar imágenes
import docx2txt # importando la librería docx2txt para manejar archivos DOCX
from PyPDF2 import PdfReader # importando la librería PyPDF2 para manejar archivos PDF
import os # importando la librería os para manejar el sistema de archivos

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
 
# =============guardar archivos dentro del proyecto ==============
def guardar_archivo(uploadedfile):
    # Extrae solo el nombre del archivo sin la ruta del directorio
    filename = os.path.basename(uploadedfile.name) # hhtps://docs.python.org/3/library/os.path.html#os.path.basename    
    # Crea el directorio temp si no existe
    os.makedirs("temp", exist_ok=True) # existt_ok =True evita un error si el directorio ya existe http://docs.python.org/3/library/os.html#os.makedirs
    # Guarda el archivo en el directorio temp
    with open(os.path.join("temp", filename), "wb") as f: # f escribe el archivo en modo binario, os.path.join combina el directorio y el nombre del archivo
        f.write(uploadedfile.getbuffer()) #getbuffer() obtiene el contenido del archivo subido http://docs.streamlit.io/library/api-reference/utilities/st.file_uploader#st.file_uploader.getbuffer    
    return st.success(f"El archivo {filename} se ha guardado correctamente") # Mensaje de éxito al guardar el archivo

# ////////////////////////////////FUNCONES PARA GARGES////////////////////////
def main(): #  Función principal del script
    st.title("Carga de archivos")    
    # =====MENÚ DE SELECCIÓN DE ARCHIVOS DEL NAVEGADOR VERTICAL======
    menu = ["Imagen","EXCEL", "DOCUMENTOS"] # Lista de tipos de archivos
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
            guardar_archivo(archivo_imagen) # Llama a la función para guardar el archivo subido
   
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
            guardar_archivo(archivo_excel) # Llama a la función para guardar el archivo subido
    
      
    #=====Validación de documentos ===========
    elif eleccion == "DOCUMENTOS": # Si el usuario selecciona "DOCUMENTOS"
        st.subheader("Cargar un documento") # Subtítulo para la sección de PDF
        archivo_doc = st.file_uploader("Sube tu documento", type=["pdf", "docx", "txt"]) # Permite al usuario subir un archivo PDF
        
        #crea el boton y valida para cargar el archivo
        if st.button("Cargar documento"): # Si el usuario hace clic en el botón "            
            # Validación para asegurarse de que se ha subido un archivo
            if archivo_doc is not None: # Si se ha subido un archivo    
                detalle_archivo_doc = {"nombre_archivo": archivo_doc.name, # Nombre del archivo
                                    "tipo_archivo": archivo_doc.type, # Tipo de archivo
                                    "tamaño_archivo": archivo_doc.size}
                st.write(detalle_archivo_doc) # Muestra los detalles del archivo subido
                
                #valida el tipo de archivo y extrae el texto
                if archivo_doc.type == "application/pdf": # Si el archivo es un PDF
                    texto_pdf = leer_pdf(archivo_doc) # Llama a la función para leer el PDF que hicimos al inicio
                    st.text_area("Contenido del PDF", value=texto_pdf, height=300)
                elif archivo_doc.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document": # Si el archivo es un DOCX
                    texto_docx = docx2txt.process(archivo_doc) # Llama a la función para leer el DOCX
                    st.text_area("Contenido del DOCX", value=texto_docx, height=300)
                elif archivo_doc.type == "text/plain": # Si el archivo es un TXT    
                    texto_txt = archivo_doc.read().decode("utf-8") # Lee el archivo TXT
                    st.text_area("Contenido del TXT", value=texto_txt, height=300)
                
                else:
                    st.error("Tipo de archivo no soportado. Por favor, sube un archivo PDF, DOCX o TXT.")
                # Muestra el contenido del archivo subido en un área de texto
                guardar_archivo(archivo_doc) # Llama a la función para guardar el archivo subido
            else: # Si no se ha subido un archivo
                st.error("Por favor, sube un archivo válido.")   
    
    
if __name__ == "__main__": # Punto de entrada del script
    main() # Llamando a la función principal
    
        

    