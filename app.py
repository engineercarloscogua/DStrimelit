import streamlit as st 

#function to run the app
def main():
    #typeado de textos
    st.title("Hello World App") #titule of the app https://docs.streamlit.io/develop/api-reference/text/st.title
    st.header("Titulo de encabezado") # titulo encabezado https://docs.streamlit.io/develop/api-reference/text/st.header
    st.subheader("Subtitulo de encabezado") #subtitulo https://docs.streamlit.io/develop/api-reference/text/st.subheader
    st.text("Texto corriente") #text https://docs.streamlit.io/develop/api-reference/text/st.text
    st.markdown("# Texto con markdown") #markdown https://docs.streamlit.io/develop/api-reference/text/st.markdown
    st.markdown("## OtroTexto con markdown ") #markdown https://docs.streamlit.io/develop/api-reference/text/st.markdown
    st.write("Texto de modo escritura") #write https://docs.streamlit.io/develop/api-reference/text/st.write
#-----------------Usar variables en texto -------------------------------------------
    st.title("--USAR VARAABLES EN TEXTO CON F STRING --")
    nombre = "Carlos" #variable para insertar en el texto
    st.write(f"escritura Hola {nombre}, estas aprendiendo bien")  #f-string para insertar variables en el texto https://docs.streamlit.io/develop/api-reference/text/st.write
    st.markdown(f"## markdown Hola {nombre}, estas aprendiendo bien")  #f-string para insertar variables en el texto https://docs.streamlit.io/develop/api-reference/text/st.markdown
    st.text(f" texto simple Hola {nombre}, estas aprendiendo bien")  #f-string para insertar variables en el texto https://docs.streamlit.io/develop/api-reference/text/st.text
    st.header(f" encabezado Hola {nombre}, estas aprendiendo bien")  #f-string para insertar variables en el texto https://docs.streamlit.io/develop/api-reference/text/st.header
    st.subheader(f" subencabezado Hola {nombre}, estas aprendiendo bien")  #f-string para insertar variables en el texto https://docs.streamlit.io/develop/api-reference/text/st.subheader
    st.title(f" titulo Hola {nombre}, estas aprendiendo bien")  #f-string para
    
# ---------------MENSAJES DE ALERTA Y ERROR -----------------------------------
    st.title("--MENSAJES DE ALERTA Y ERROR--")
    st.success("Mensaje de éxito")  #mensaje de éxito https://docs.streamlit.io/develop/api-reference/text/st.success
    st.info("Mensaje de información")  #mensaje de información https://docs.streamlit.io/develop/api-reference/text/st.info
    st.warning("Mensaje de advertencia")  #mensaje de advertencia https://docs.streamlit.io/develop/api-reference/text/st.warning
    st.error("Mensaje de error")  #mensaje de error https://docs.streamlit.io/develop/api-reference/text/st.error
    st.exception("Mensaje de excepción")  #mensaje de excepción https://docs.streamlit.io/develop/api-reference/text/st.exception
    st.help("Mensaje de ayuda")  #mensaje de ayuda https://docs.streamlit.io/develop/api-reference/text/st.help 
    st.balloons()  #mensaje de globos https://docs.streamlit.io/develop/api-reference/text/st.balloons
    st.snow()  #mensaje de nieve https://docs.streamlit.io/develop/api-reference/text/st.snow
    st.spinner("Cargando...")  #mensaje de cargando https://docs.streamlit.io/develop/api-reference/text/st.spinner 
# validate the app
if __name__ == "__main__":
    main() # run the app
    