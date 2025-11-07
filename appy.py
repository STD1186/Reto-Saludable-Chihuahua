import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("⚖️ Calculadora de IMC")
st.write("Calcula tu Índice de Masa Corporal y recibe consejos personalizados")

#datos
st.subheader("Tus datos")

altura = st.slider("Altura (cm)", 0, 220, 170)
peso = st.slider("Peso (kg)", 0, 220, 70)
edad = st.slider("Edad", 0, 100, 30)

genero = st.radio("Género", ["Masculino", "Femenino", "Otro"])

#calclulo dle IMC
if st.button("Calcular IMC"):
    # Cálculo del IMC
    altura_m = altura / 100
    imc = peso / (altura_m ** 2)
    
    # Mostrar resultado
    st.subheader(f"Tu IMC: {imc:.1f}")

if imc < 18.5:
        st.warning("Categoría: Bajo peso")
        st.info("""
        **Consejos:**
        • Aumenta tus porciones poco a poco. Tu cuerpo necesita más combustible.
        • Incluye alimentos nutritivos como frutos secos y aguacate.
        • Realiza ejercicio de fuerza.
        • Agrega proteína en cada comida.
        """)

elif imc < 24.9:
    st.writing("categoría: peso normal")
    st.info("""
    **consejos:**
    • ¡Excelente! Mantén tus hábitos saludables. 
    • Hidrátate y duerme bien. Eso marca la diferencia.
    • Pequeños hábitos diarios = grandes resultados a largo plazo.
    • COntinua con ejercicio de forma regular.

elif imc < 29.9:
    st.writing("categoría: sobre peso")
    st.info("""
    **consejos:**
    • Comienza con pasos simples: más agua, menos bebidas azucaradas.
    • Camina y has ejercico 30 minutos diarios.
    • Las verduras deben cubrir 1/3 de tu plato.
    • Controla el tamaño de las porciones.

else:
    st.writing("categoría: obesidad")
    st.info("""
    **consejos:**
    • Consulta con un profesional de la salud. 
    • No se trata de rapidez, sino de constancia. Empieza hoy.
    • EStablece metas pequeñas y alcansables.
    • Comienza con ejercicios suabes como la caminata o la natación.
    
