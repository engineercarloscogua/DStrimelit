import streamlit as st
import pandas as pd # Importing Pandas for data handling http://pandas.pydata.org/pandas-docs/stable/
from utils.file_utils import cargar_archivo, guardar_archivo # Importing utility functions for file handling http://docs.streamlit.io/library/api-reference/utilities/st.file_uploader
from processing.data_processing import leer_pdf # Importing data processing functions for reading PDF files http://docs.python.org/3/library/os.path.html#os.path.join

def changes_files():
    st.title("Carga de archivos")
    # =====MENU FOR FILE SELECTION IN VERTICAL SIDEBAR======
    # Moved selectbox from sidebar to main page
    menu = ["Imagen", "EXCEL", "DOCUMENTOS"]  # List of file types
    eleccion = st.selectbox("Selecciona el tipo de archivo", menu)  # Variable to store user selection
    
    #=====IMAGE FILE UPLOAD===========
    if eleccion == "Imagen":
        st.subheader("Cargar una imagen")
        # File uploader for image files with allowed extensions jpg, jpeg, png
        archivo_imagen = st.file_uploader("Sube tu imagen", type=["jpg", "jpeg", "png"])
        #======Image upload validation===========
        if archivo_imagen is not None:  # If a file has been uploaded
            detalle_archivo = {"nombre_archivo": archivo_imagen.name,
                             "tipo_archivo": archivo_imagen.type,
                             "tamaño_archivo": archivo_imagen.size}
            st.write(detalle_archivo)  # Display file details
            st.image(cargar_archivo(archivo_imagen), caption="Imagen cargada", use_container_width=True)  # Display the uploaded image with a caption and adjust column width
            guardar_archivo(archivo_imagen)  # Call function to save the uploaded file
    
    #=====EXCEL FILE UPLOAD===========
    elif eleccion == "EXCEL":
        st.subheader("Cargar un archivo Excel")
        # File uploader for Excel files with allowed extensions CSV, xlsx, xls
        archivo_excel = st.file_uploader("Sube tu archivo Excel", type=["CSV", "xlsx", "xls"])
        # Validation to ensure an Excel file has been uploaded
        if archivo_excel is not None:
            detalle_archivo_excel = {"nombre_archivo": archivo_excel.name,
                                  "tipo_archivo": archivo_excel.type,
                                  "tamaño_archivo": archivo_excel.size}
            st.write(detalle_archivo_excel)  # Display file details
            #====Validating Excel file type and loading DataFrame========
            if archivo_excel.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                df = pd.read_excel(archivo_excel)  # Load xlsx Excel file into a DataFrame
            elif archivo_excel.type == "application/vnd.ms-excel":
                df = pd.read_excel(archivo_excel, engine='xlrd')
            elif archivo_excel.type == "text/csv":
                df = pd.read_csv(archivo_excel)
            else:
                df = pd.DataFrame()  # If the file type is not recognized, create an empty DataFrame
                st.error("Tipo de archivo no soportado. Por favor, sube un archivo Excel o CSV.")
            st.dataframe(df)  # Display the DataFrame in the application
            guardar_archivo(archivo_excel)  # Call function to save the uploaded file
    
    #=====DOCUMENT FILE UPLOAD===========
    elif eleccion == "DOCUMENTOS":
        st.subheader("Cargar un documento")
        # File uploader for document files with allowed extensions pdf, docx, txt
        archivo_doc = st.file_uploader("Sube tu documento", type=["pdf", "docx", "txt"])
        # Validation for document upload
        if st.button("Cargar documento"):  # If the user clicks the button to upload a document
            if archivo_doc is not None:  # If a file has been uploaded
                detalle_archivo_doc = {"nombre_archivo": archivo_doc.name,
                                     "tipo_archivo": archivo_doc.type,
                                     "tamaño_archivo": archivo_doc.size}
                st.write(detalle_archivo_doc)  # Display file details
                # Display the content of the uploaded document based on its type
                if archivo_doc.type == "application/pdf":
                    texto_pdf = leer_pdf(archivo_doc)  # Read PDF file and extract text
                    st.text_area("Contenido del PDF", value=texto_pdf, height=300)
                elif archivo_doc.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                    texto_docx = docx2txt.process(archivo_doc)  # Read DOCX file and extract text
                    st.text_area("Contenido del DOCX", value=texto_docx, height=300)
                elif archivo_doc.type == "text/plain":  # If the file is a TXT
                    texto_txt = archivo_doc.read().decode("utf-8")
                    st.text_area("Contenido del TXT", value=texto_txt, height=300)
                else:
                    st.error("Tipo de archivo no soportado. Por favor, sube un archivo PDF, DOCX o TXT.")
                guardar_archivo(archivo_doc)  # Call function to save the uploaded file
            else:
                st.error("Por favor, sube un archivo válido.")  # If no file has been uploaded