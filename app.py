import streamlit as st 

#function to run the app
def main():
    st.title("Hello World App") #titule of the app https://docs.streamlit.io/develop/api-reference/text/st.title
    st.header("Titulo de encabezado") # titulo encabezado https://docs.streamlit.io/develop/api-reference/text/st.header
    st.subheader("Subtitulo de encabezado") #subtitulo https://docs.streamlit.io/develop/api-reference/text/st.subheader
    st.text("Texto corriente") #text https://docs.streamlit.io/develop/api-reference/text/st.text
    st.markdown("# Texto con markdown") #markdown https://docs.streamlit.io/develop/api-reference/text/st.markdown
    st.markdown("## OtroTexto con markdown ") #markdown https://docs.streamlit.io/develop/api-reference/text/st.markdown
    st.write("Texto de modo escritura") #write https://docs.streamlit.io/develop/api-reference/text/st.write
    

# validate the app
if __name__ == "__main__":
    main() # run the app
    