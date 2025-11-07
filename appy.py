import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("⚖️ Calculadora de IMC")
st.write("Calcula tu Índice de Masa Corporal y recibe consejos personalizados")

#datos
st.subheader("Tus datos")

altura = st.slider("Altura (cm)", 100, 220, 170)
peso = st.slider("Peso (kg)", 40, 150, 70)
edad = st.slider("Edad", 0, 100, 30)

genero = st.radio("Género", ["Masculino", "Femenino", "Otro"])
