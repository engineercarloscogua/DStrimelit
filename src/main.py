import streamlit as st # Importing Streamlit for building the web application
from modulos.p1 import dashboard # Importing the title function from the first page module
from modulos.changes import changes_files # Importing the changes_files function from the changes module
from modulos.ingresos import ingresos # Importing the ingresos function from the ingresos module
from modulos.negados import negados # Importing the negados function from the negados module
from modulos.retiros import retiros # Importing the retiros function from the retiros module


from PIL import Image # Importing the Image class from the PIL library to handle images



# icono 
icono = Image.open("img/iccono.png")  # Abrir la imagen de streamlit
st.set_page_config(page_title="Aseguramiento",
                   page_icon=icono,  # Icono de la app
                   layout="wide",
                   initial_sidebar_state="collapsed"  # Menú contraído https://docs.streamlit.io/library/api-reference/layout/st.sidebar
                   )  # Configurar la página de la app https://docs.streamlit.io/library/api-reference/layout/st.set_page_config

# Inyectar CSS para ocultar el sidebar automático
st.markdown(
    """
    <style>
    [data-testid="collapsedControl"] {
        display: none;
    }
    .css-1aumxhk {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ///////////////////////FUNCTIONS FOR FILE HANDLING/////////////////////
def main():
    # =====MENU FOR FILE SELECTION IN VERTICAL SIDEBAR======
    menu = ["Dashboard Principal", "Ingresos", "Negados", "Retiros", "cargues"]  # List of file types
    pagina = st.sidebar.selectbox("Selecciona el tipo de archivo", menu)  # Variable to store user selection
    
    if pagina == "Dashboard Principal":  # If the user selects "Dashboard Principal"
        dashboard()  # Call the dashboard function to set the page title
    elif pagina == "cargues":  # If the user selects "cargues"
        changes_files()  # Call the changes_files function to display the changes in files   
    elif pagina == "Ingresos":  # If the user selects "Ingresos"
        ingresos()  # Call the ingresos function to display the ingresos page    
    elif pagina == "Negados":  # If the user selects "Negados"
        negados()  # Call the negados function to display the negados page
    elif pagina == "Retiros":  # If the user selects "Retiros"
        retiros()  # Call the retiros function to display the retiros page
    else:
        st.write("Por favor, selecciona una opción válida.")  # If no valid option is selected, prompt the user to select a valid option
    
if __name__ == "__main__":  # Run the main function when the script is executed
    main()  # End of the main function