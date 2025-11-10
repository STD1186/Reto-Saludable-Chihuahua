import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("⚖️ Reto Saludable Chihuahua")
st.write("Calcula tu Índice de Masa Corporal y recibe consejos personalizados")

# Datos
st.subheader("📋 Tus datos")

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

# Meta del usuario
st.subheader("🏅 Tu Meta Personal")

meta = st.radio(
    "¿Cuál es tu objetivo?",
    ["Bajar peso", "Mantener peso", "Ganar masa muscular"],
    horizontal=True
)

if st.button("Ver Recomendaciones Personalizadas"):
    
    st.subheader(f"Plan para: {meta}")
    
    if meta == "Bajar peso":
        st.info("""
        **Plan de alimentación:**
        • Déficit calórico de 300-500 kcal diarias
        • Proteínas: 1.6-2.2g por kg de peso
        • Reduce carbohidratos simples
        • Aumenta fibra y verduras
        
        **Plan de ejercicio:**
        • Cardio: 150-300 min/semana
        • Entrenamiento de fuerza 3 veces/semana
        • Actividad diaria: 10,000 pasos
        
        **Consejos adicionales:**
        • Come lento y conscientemente
        • Duerme 7-8 horas
        • Controla porciones
        """)
        
    elif meta == "Mantener peso":
        st.info("""
        **Plan de alimentación:**
        • Mantén equilibrio calórico
        • Proteínas: 1.2-1.6g por kg de peso
        • Variedad de alimentos
        • Hidratación constante
        
        **Plan de ejercicio:**
        • Ejercicio mixto 4-5 veces/semana
        • Cardio y fuerza equilibrados
        • Actividades recreativas
        
        **Consejos adicionales:**
        • Monitorea tu peso semanalmente
        • Mantén rutinas consistentes
        • Escucha las señales de tu cuerpo
        """)
        
    else:  # Ganar masa muscular
        st.info("""
        **Plan de alimentación:**
        • Superávit calórico de 300-500 kcal
        • Proteínas: 1.8-2.5g por kg de peso
        • Carbohidratos complejos
        • Grasas saludables
        
        **Plan de ejercicio:**
        • Fuerza 4-5 veces/semana
        • Ejercicios compuestos
        • Descanso entre sesiones
        • Cardio moderado 2 veces/semana
        
        **Consejos adicionales:**
        • Enfócate en progresión
        • Descansa 48h entre grupos musculares
        • Suplementa con proteína si es necesario
        """)

# Cálculo del IMC
st.subheader("📊 Calculadora de Indice de Masa Corporal")
if st.button("Calcular IMC", type="primary", use_container_width=True):
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

    elif imc < 25:
        st.success("Categoría: Peso normal")
        st.info("""
        **Consejos:**
        • ¡Excelente! Mantén tus hábitos saludables. 
        • Hidrátate y duerme bien. Eso marca la diferencia.
        • Pequeños hábitos diarios = grandes resultados a largo plazo.
        • Continúa con ejercicio de forma regular.
        """)

    elif imc < 30:
        st.warning("Categoría: Sobrepeso")
        st.info("""
        **Consejos:**
         • Comienza con pasos simples: más agua, menos bebidas azucaradas.
         • Camina y haz ejercicio 30 minutos diarios.
         • Las verduras deben cubrir 1/3 de tu plato.
         • Controla el tamaño de las porciones.
         """)

    else:
        st.error("Categoría: Obesidad")
        st.info("""
        **Consejos:**
        • Consulta con un profesional de la salud. 
        • No se trata de rapidez, sino de constancia. Empieza hoy.
        • Establece metas pequeñas y alcanzables.
        • Comienza con ejercicios suaves como la caminata o la natación.
        """)

# Cálculo de peso ideal
st.subheader("📊 Calculadora de Peso Ideal")

if st.button("Calcular Mi Peso Ideal", type="primary", use_container_width=True):
    
    if genero == "Masculino":
        peso_ideal_min = 20 * (altura/100)**2
        peso_ideal_max = 25 * (altura/100)**2
    else:
        peso_ideal_min = 19 * (altura/100)**2  
        peso_ideal_max = 24 * (altura/100)**2

    # Mostrar resultados
    st.success("**Tu rango de peso ideal:**")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Peso Actual", f"{peso} kg")
    with col2:
        st.metric("Mínimo Ideal", f"{peso_ideal_min:.1f} kg")
    with col3:
        st.metric("Máximo Ideal", f"{peso_ideal_max:.1f} kg")

    fig, ax = plt.subplots()
    
    categorias = ['Peso Actual', 'Mínimo', 'Máximo']
    pesos = [peso, peso_ideal_min, peso_ideal_max]
    
    ax.bar(categorias, pesos, color=['blue', 'green', 'green'])
    ax.set_ylabel('Peso (kg)')
    
    for i, v in enumerate(pesos):
        ax.text(i, v + 0.5, f'{v:.1f}kg', ha='center')
    
    st.pyplot(fig)

    if peso_ideal_min <= peso <= peso_ideal_max:
        st.balloons()
        st.success(" **¡Perfecto! Estás dentro de tu rango de peso ideal**")
    elif peso < peso_ideal_min:
        diferencia = peso_ideal_min - peso
        st.warning(f" **Recomendación:** Aumenta {diferencia:.1f} kg para llegar al mínimo ideal")
    else:
        diferencia = peso - peso_ideal_max
        st.warning(f" **Recomendación:** Reduce {diferencia:.1f} kg para llegar al máximo ideal")

# Recomendaciones de alimentos por categoría
st.subheader("🥗 Alimentos recomendados")

categoria_alimentos = st.radio(
    "Selecciona categoría:",
    ["Proteínas", "Carbohidratos", "Grasas saludables", "Frutas y Verduras"]
)

alimentos = {
    "Proteínas": ["Pechuga de pollo", "Carnes rojas", "Salmón", "Huevos", "Legumbres", "Tofu", "Yogur griego", "Atún", "Quinoa"],
    "Carbohidratos": ["Avena", "Arroz integral", "Camote", "Pasta integral", "Pan integral", "Platano", "Maíz", "Legumbres"],
    "Grasas saludables": ["Aguacate", "Nueces", "Aceite de oliva", "Semillas de chía", "Almendras", "Pescados azules", "Aceitunas"],
    "Frutas y Verduras": ["Espinacas", "Brócoli", "Manzana", "Zanahoria", "Fresas", "Tomate", "Col rizada", "Arándanos"]
}

if categoria_alimentos in alimentos:
    cols = st.columns(2)
    for i, alimento in enumerate(alimentos[categoria_alimentos]):
        cols[i % 2].write(f"• {alimento}")
