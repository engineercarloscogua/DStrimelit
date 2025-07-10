import streamlit as st 
import pandas as pd

#deficion del dataframe 
df =pd.read_excel("mer_con_neg_2018_2024.xlsx") #read the excel file with pandas


#function to run the app
def main():
    #typeado de textos
    st.title("Manejo de DataFrames") #titule of the app https://docs.streamlit.io/develop/api-reference/text/st.title
    st.dataframe(df) #show the dataframe in the app https://docs.streamlit.io/develop/api-reference/data/st.dataframe
   
# validate the app
if __name__ == "__main__":
    main() # run the app
    