import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("⚖️ Calculadora de IMC")
st.write("Calcula tu Índice de Masa Corporal y recibe consejos personalizados")

# Datos
st.subheader("Tus datos")

altura = st.slider("Altura (cm)", 0, 220, 170)
peso = st.slider("Peso (kg)", 0, 220, 70)
edad = st.slider("Edad", 0, 100, 30)

actividad = st.selectbox(
    "Nivel de actividad física",
    [
        "Sedentaria (poco o ningún ejercicio)",
        "Moderada (ejercicio 1-3 veces por semana)", 
        "Activa (ejercicio 3-5 veces por semana)",
        "Muy activa (ejercicio 6-7 veces por semana)"
    ])

genero = st.radio("Género", ["Masculino", "Femenino", "Otro"])

# Cálculo del IMC
if st.button("Calcular IMC"):
    # Cálculo del IMC
    altura_m = altura / 100
    imc = peso / (altura_m ** 2)
    
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

    elif imc < 25:  # Cambiado a 25 (estándar)
        st.success("Categoría: Peso normal")  # Cambiado a st.success
        st.info("""
        **Consejos:**
        • ¡Excelente! Mantén tus hábitos saludables. 
        • Hidrátate y duerme bien. Eso marca la diferencia.
        • Pequeños hábitos diarios = grandes resultados a largo plazo.
        • Continúa con ejercicio de forma regular.
        """)

    elif imc < 30:
        st.warning("Categoría: Sobrepeso")  # Corregido "sobre peso"
        st.info("""
        **Consejos:**
         • Comienza con pasos simples: más agua, menos bebidas azucaradas.
         • Camina y haz ejercicio 30 minutos diarios.  # "has" -> "haz"
         • Las verduras deben cubrir 1/3 de tu plato.
         • Controla el tamaño de las porciones.
         """)

    else:
        st.error("Categoría: Obesidad")
        st.info("""
        **Consejos:**
        • Consulta con un profesional de la salud. 
        • No se trata de rapidez, sino de constancia. Empieza hoy.
        • Establece metas pequeñas y alcanzables.  # "alcansables" -> "alcanzables"
        • Comienza con ejercicios suaves como la caminata o la natación.  # "suabes" -> "suaves"
        """)



# Cálculo de peso ideal
st.subheader("Calculadora de Peso Ideal")

if st.button("Calcular Mi Peso Ideal"):
    
    if genero == "Masculino":
        peso_ideal = 0.75 * altura - 62.5
    else:
        peso_ideal = 0.675 * altura - 56.25

    st.success(f"**¡Tu peso ideal es:** {peso_ideal:.1f} kg")

if calcular_peso_ideal:
    if genero == "Masculino":
        peso_ideal = 0.75 * altura - 62.5
    else:
        peso_ideal = 0.675 * altura - 56.25
    
    diferencia = peso - peso_ideal
    
    if diferencia == 0:
        st.balloons()
        st.success("🎉 ¡Felicidades! Estás EXACTAMENTE en tu peso ideal")
    else:
        st.info(f"**Peso ideal calculado:** {peso_ideal:.1f} kg")
