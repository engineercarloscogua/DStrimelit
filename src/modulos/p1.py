import streamlit as st
from PIL import Image  # Importing the Image class from the PIL library to handle images

def dashboard():
    st.title("Dash Board Principal Capresoca EPS")  # Set the title of the page
    img = Image.open("img/logo.jpg")  # Open the image file
    st.image(img, caption="Logo de Capresoca EPS")  # Display the image with a caption
    st.write("Bienvenido al panel de control principal de Capresoca EPS.")  #