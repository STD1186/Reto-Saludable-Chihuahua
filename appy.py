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
    
    # Mostrar resultado
    st.subheader(f"Tu IMC: {imc:.1f}")

    # TODAS las condiciones deben estar DENTRO del bloque del botón
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
st.subheader("Tu peso ideal")

if genero == "Masculino":
    peso_ideal_min = 20 * (altura/100)**2
    peso_ideal_max = 25 * (altura/100)**2
else:
    peso_ideal_min = 19 * (altura/100)**2  
    peso_ideal_max = 24 * (altura/100)**2

st.write(f"**Rango de peso ideal:**")
st.info(f"Entre **{peso_ideal_min:.1f}kg** y **{peso_ideal_max:.1f}kg**")

diferencia = peso - peso_ideal_max
if peso > peso_ideal_max:
    st.warning(f"Te encuentras {diferencia:.1f}kg por encima de tu peso ideal")
elif peso < peso_ideal_min:
    st.warning(f"Te encuentras {abs(diferencia):.1f}kg por debajo de tu peso ideal")
else:
    st.success("¡Estás en tu peso ideal!")
