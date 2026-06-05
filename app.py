import streamlit as st

from src.topics.linear_nonhomogeneous import render


TOPICS = {
    "Sistemas lineales no homogéneos": render,
}


st.set_page_config(
    page_title="Modelado y Simulación",
    page_icon="📈",
    layout="wide",
)

st.title("Calculadoras de Modelado y Simulación")
st.caption("Herramientas con pasos, análisis cualitativo y simulaciones.")

topic_name = st.sidebar.selectbox("Tema", list(TOPICS))
st.sidebar.info("La app está organizada para sumar nuevos temas en `src/topics`.")

TOPICS[topic_name]()

