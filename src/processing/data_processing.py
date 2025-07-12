from PyPDF2 import PdfReader # importando la librería PyPDF2 para manejar archivos PDF http://docs.python.org/3/library/os.path.html#os.path.basename
import docx2txt # importando la librería docx2txt para manejar archivos DOCX hhttp://docs.python.org/3/library/os.path.html#os.path.join

# ///////////////////////FUNCONES PARA GARGES/////////////////////
def leer_pdf(file): # función para leer un archivo PDF
    pdf_reader = PdfReader(file)# Creando un lector de PDF
    count = len(pdf_reader.pages) # Contando las páginas del PDF
    todo_el_texto = "" # Variable para almacenar todo el texto extraído
    for i in range(count): # Iterando sobre cada página
        pagina = pdf_reader.pages[i] # Obteniendo la página
        todo_el_texto += pagina.extract_text() # Extrayendo el texto de la página
    return todo_el_texto # Retornando el texto extraído