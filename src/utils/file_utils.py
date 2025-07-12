import os # Importing the os module to handle file paths and directories http://docs.python.org/3/library/os.html
import streamlit as st # Importing Streamlit for building the web application http://docs.streamlit.io/library/api-reference/utilities/st.file_uploader
from PIL import Image # Importing PIL for image processing http://pillow.readthedocs.io/en/stable/reference/Image.html

# Function to load an image file
def cargar_archivo(image_file): # Function to load an image file
    img = Image.open(image_file) # Open the image file using PIL http://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open
    return img # Return the opened image

# Function to read a PDF file and extract text
def guardar_archivo(uploadedfile):
    filename = os.path.basename(uploadedfile.name)# Extract only the file name without the directory path http://docs.python.org/3/library/os.path.html#os.path.basename
    os.makedirs("temp", exist_ok=True) # Create the temp directory if it does not exist, exist_ok=True avoids an error if the directory already exists http://docs.python.org/3/library/os.html#os.makedirs
    with open(os.path.join("temp", filename), "wb") as f: # Open the file in write-binary mode, os.path.join combines the directory and the file name
        # f is the opened file object
        f.write(uploadedfile.getbuffer())# getbuffer() gets the content of the uploaded file http://docs.streamlit.io/library/api-reference/utilities/st.file_uploader#st.file_uploader.getbuffer
    return st.success(f"El archivo {filename} se ha guardado correctamente")# Success message after saving the file