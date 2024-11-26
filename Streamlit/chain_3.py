
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Análise de Sentimentos de The Simpsons")
st.write("Analisando os diálogos de um episódio!")

uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, index_col=0)
    st.write(data)

    sentiment_counts = data['sentiment'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)
