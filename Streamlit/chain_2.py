
import streamlit as st
import pandas as pd

st.title("Minha Aplicação Streamlit")
st.write("Olá, mundo!")

uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)
