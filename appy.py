import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#Barra lateral
with st.sidebar:
 st.title("Datos Institucionales")
 st.write(""" 
 TEMA: ALIMENTOS

 INSTITUCIÓN 
 
 UNIVERSIDAD AUTÓNOMA DE CHIHUAHUA "FACULTAD DE CIENCIAS QUÍMICAS"

 MATERIA:PROGRAMACIÓN
 
GRUPO: 3L

INTEGRANTES:
* Sasha Torres Davidson 385944
* Victoria Izquierdo Navarrro 385983
* Ever Gibran García Martinez 385898
* Deyra Renata Herrera Juárez 385845
* Mayra Mariel Jimenez Navarrete 385869
""")

st.title("🍏 Reto Saludable Chihuahua")
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

# alimentos recomendados
st.subheader("🥗 Alimentos recomendados")

categoria_alimentos = st.radio(
    "Selecciona categoría:",
    ["Proteínas", "Carbohidratos", "Grasas saludables", "Frutas y Verduras"]
)

alimentos = {
    "Proteínas": [
        "Pechuga de pollo", "Salmón", "Huevos", "Legumbres", 
        "Tofu", "Yogur griego", "Atún", "Quinoa"
    ],
    "Carbohidratos": [
        "Avena", "Arroz integral", "Camote", "Pasta integral",
        "Pan integral", "Banana", "Maíz", "Lentejas"
    ],
    "Grasas saludables": [
        "Aguacate", "Nueces", "Aceite de oliva", "Semillas de chía",
        "Almendras", "Pescados azules", "Aceitunas"
    ],
    "Frutas y Verduras": [
        "Espinacas", "Brócoli", "Manzana", "Zanahoria",
        "Fresas", "Tomate", "Col rizada", "Arándanos"
    ]
}

if categoria_alimentos in alimentos:
    cols = st.columns(2)
    for i, alimento in enumerate(alimentos[categoria_alimentos]):
        cols[i % 2].write(f"• {alimento}")
     
# Meta del usuario
st.subheader("🏅 Tu Meta Personal")

meta = st.radio(
    "¿Cuál es tu objetivo?",
    ["📉Bajar peso", "⚖️ Mantener peso", "💪Ganar masa muscular"],
    horizontal=True
)
# Recomendaciones perzonalizadas
if st.button("📋 Ver Mi Plan Personalizado", key="plan_personalizado"):
    
    if meta == "💪Ganar masa muscular":
        st.success("**🎯 Estrategia: Superávit Calórico Inteligente**")
        
        st.subheader("🍽️ Plan de Alimentación")
        st.info("""
        **Distribución Diaria:**
        • Calorías: 300-500 kcal más que tu mantenimiento
        • Proteínas: 2.0-2.5g por kg de peso
        • Grasas: 25-30% del total calórico
        • Carbohidratos: 45-50% del total calórico
        
        **Timing Nutricional:**
        • Comer cada 3-4 horas
        • Carbohidratos alrededor del entrenamiento
        • Proteína post-entreno (30-60 min después)
        • Cena con proteína de digestión lenta (caseína)
        
        **Alimentos Clave:**
        • Carnes magras, pescados, huevos
        • Carbohidratos complejos (arroz, papa, avena)
        • Grasas saludables (aceite de oliva, frutos secos)
        • Lácteos (yogur griego, queso cottage)
        """)
        
        st.subheader("💪 Plan de Ejercicio")
        st.info("""
        **Rutina Semanal:**
        • Fuerza: 4-5 días/semana
        • Cardio: 2-3 días/semana (moderado, 20-30 min)
        • Descanso activo: 1-2 días/semana
        
        **Enfoque:**
        • Ejercicios compuestos principales
        • Progresión constante en pesos
        • Técnica perfecta antes de aumentar carga
        • Descanso entre series: 60-90 segundos
        """)
        
        st.subheader("💡 Consejos Específicos")
        st.info("""
        • Enfócate en la progresión, no solo en el dolor
        • Descansa 48 horas entre grupos musculares
        • Suplementa con proteína en polvo si es necesario
        • Toma creatina monohidrato
        • Objetivo realista: 0.5-1kg de músculo/mes
        """)
        
    elif meta == "📉Bajar peso":
        st.success("**🎯 Estrategia: Déficit Calórico Controlado**")
        
        st.subheader("🍽️ Plan de Alimentación")
        st.info("""
        **Distribución Diaria:**
        • Calorías: 300-500 kcal menos que tu mantenimiento
        • Proteínas: 1.8-2.2g por kg de peso
        • Grasas: 25-30% del total calórico
        • Carbohidratos: 40-45% del total calórico
        
        **Frecuencia de Comidas:**
        • 3 comidas principales + 2 snacks
        • Ayuno intermitente opcional (16:8)
        • Cena ligera 3 horas antes de dormir
        
        **Alimentos Clave:**
        • Verduras de hoja verde
        • Proteínas magras (pollo, pescado)
        • Grasas saludables (aguacate, nueces)
        • Fibra soluble (avena, manzana)
        """)
        
        st.subheader("💪 Plan de Ejercicio")
        st.info("""
        **Rutina Semanal:**
        • Cardio: 4-5 días/semana (30-45 min)
        • Fuerza: 3-4 días/semana
        • HIIT: 2 sesiones/semana
        • Actividad diaria: 10,000+ pasos
        
        **Enfoque:**
        • Mantener masa muscular mientras pierdes grasa
        • Ejercicios compuestos (sentadillas, press)
        • Progresión en cargas
        """)
        
        st.subheader("💡 Consejos Específicos")
        st.info("""
        • Toma 2-3 litros de agua al día
        • Duerme 7-8 horas de calidad
        • Controla el estrés (meditación, yoga)
        • Pésate 1 vez por semana, no diario
        • Paciencia - objetivo realista: 0.5-1kg/semana
        """)
        
    elif meta ==  "⚖️ Mantener peso":
        st.success("**🎯 Estrategia: Equilibrio y Consistencia**")
        
        st.subheader("🍽️ Plan de Alimentación")
        st.info("""
        **Distribución Diaria:**
        • Calorías: Mantenimiento (ni déficit ni superávit)
        • Proteínas: 1.2-1.6g por kg de peso
        • Grasas: 25-35% del total calórico
        • Carbohidratos: 45-55% del total calórico
        
        **Balance Nutricional:**
        • Variedad de todos los grupos alimenticios
        • Comidas regulares sin saltarse ninguna
        • Hidratación constante durante el día
        • Flexibilidad para ocasiones especiales
        
        **Alimentos Clave:**
        • Frutas y verduras de todos los colores
        • Proteínas variadas (animales y vegetales)
        • Granos enteros y legumbres
        • Grasas saludables en moderación
        """)
        
        st.subheader("💪 Plan de Ejercicio")
        st.info("""
        **Rutina Semanal:**
        • Ejercicio mixto: 4-5 días/semana
        • Fuerza: 2-3 días/semana
        • Cardio: 2-3 días/semana
        • Flexibilidad: 1-2 días/semana
        
        **Enfoque:**
        • Mantener condición física general
        • Prevenir pérdida muscular
        • Actividades que disfrutes
        • Variedad para evitar aburrimiento
        """)
        
        st.subheader("💡 Consejos Específicos")
        st.info("""
        • Monitorea tu peso 1-2 veces por mes
        • Mantén rutinas consistentes
        • Escucha las señales de hambre y saciedad
        • Permite flexibilidad en tu plan
        • Enfócate en salud a largo plazo, no solo peso
        • Disfruta del proceso y celebra tu consistencia
        """)

# Platillos recomendados
if st.button("Ver Platillos Personalizados"):
    
    st.subheader(f"🍽️ Platillos Recomendados para {meta}")
    
    if meta == "💪Ganar masa muscular":
        
        st.info("""
        **🍗 Pechuga de Pollo a la Plancha con Boniato y Brócoli**
        · Porción: 1 pechuga (200g), 1 boniato (200g), 1 taza de brócoli
        · Calorías: ~480-550 kcal
        · Proteínas: ~45-50g | Grasas: ~8-12g | Carbohidratos: ~55-60g
        · Puntos Fuertes: Proteína magra de alta calidad para reparar músculo
        """)
        
        st.info("""
        **🐟 Salmón al Horno con Quinoa y Espárragos**
        · Porción: 1 filete de salmón (180g), 1 taza de quinoa, 10-12 espárragos
        · Calorías: ~580-650 kcal
        · Proteínas: ~40-45g | Grasas: ~25-30g | Carbohidratos: ~45-50g
        · Puntos Fuertes: Combinación excelente de proteína y grasas antiinflamatorias
        """)
        
        st.info("""
        **🍚 Bowl de Arroz Integral, Lentejas y Huevo Duro**
        · Porción: 1 taza de arroz, 1 taza de lentejas, 2 huevos duros
        · Calorías: ~550-620 kcal
        · Proteínas: ~30-35g | Grasas: ~12-15g | Carbohidratos: ~80-90g
        · Puntos Fuertes: Fuente de energía sostenible y fibra
        """)
        
        st.info("""
        **🥤 Batido 'Volumen Sano'**
        · Porción: 300ml leche, 1 plátano, 40g avena, 1 cda. mantequilla de cacahuete
        · Calorías: ~550-650 kcal
        · Proteínas: ~35-40g | Grasas: ~18-22g | Carbohidratos: ~70-80g
        · Puntos Fuertes: Ideal para post-entreno o para quienes tienen poco apetito
        """)
        
    elif meta == "📉Bajar peso":
        
        st.info("""
        **🥗 Ensalada de Lentejas con Verduras y Salmón/Pollo**
        · Porción: 1 taza de lentejas, 2 tazas de verduras, 120g de salmón o pollo
        · Calorías: ~380-450 kcal
        · Proteínas: ~35-40g | Grasas: ~10-15g | Carbohidratos: ~45-50g
        · Puntos Fuertes: Altísimo contenido en fibra y proteína, gran saciedad
        """)
        
        st.info("""
        **🌯 Wrap de Lechuga con Pavo/Pollo y Aguacate**
        · Porción: 2-3 hojas de lechuga, 120g de pavo/pollo, 1/4 de aguacate
        · Calorías: ~250-300 kcal
        · Proteínas: ~25-30g | Grasas: ~10-12g | Carbohidratos: ~10-15g
        · Puntos Fuertes: Bajo en carbohidratos y calorías, controla el hambre
        """)
        
        st.info("""
        **🍲 Caldo de Pescado o Pollo con Verduras y Pechuga**
        · Porción: 1 plato de caldo, 1 taza de verduras, 120g de pechuga
        · Calorías: ~200-280 kcal
        · Proteínas: ~25-30g | Grasas: ~5-8g | Carbohidratos: ~15-20g
        · Puntos Fuertes: Muy bajo en calorías pero alto en volumen y proteína
        """)
        
        st.info("""
        **🥣 Bowl de Quinoa con Garbanzos y Verduras**
        · Porción: 3/4 taza de quinoa, 1/2 taza de garbanzos, 1.5 tazas de verduras
        · Calorías: ~320-380 kcal
        · Proteínas: ~15-18g | Grasas: ~8-10g | Carbohidratos: ~55-60g
        · Puntos Fuertes: Plato vegetariano saciante con proteína vegetal y fibra
        """)
        
        st.info("""
        **🍳 Revuelto de 1 Huevo Entero + 2 Claras con Espinacas y Champiñones**
        · Porción: 1 huevo entero, 2 claras, 2 tazas de espinacas y champiñones
        · Calorías: ~150-180 kcal
        · Proteínas: ~20-22g | Grasas: ~6-8g | Carbohidratos: ~5-7g
        · Puntos Fuertes: Muy bajo en calorías y alto en proteína, perfecto para cena
        """)
        
    elif meta == "⚖️ Mantener peso":
        
        st.info("""
        **🍝 Pasta Integral con Salsa de Carne Molida y Queso**
        · Porción: 100g pasta integral, 120g carne molida, 30g queso
        · Calorías: ~650-750 kcal
        · Proteínas: ~40-45g | Grasas: ~20-25g | Carbohidratos: ~80-90g
        · Puntos Fuertes: Alta densidad calórica y de carbohidratos
        """)
        
        st.info("""
        **🥤 Batido 'Hipercalórico Natural'**
        · Porción: 400ml leche, 1.5 plátanos, 60g avena, 1.5 cda. mantequilla de cacahuete
        · Calorías: ~750-900 kcal
        · Proteínas: ~25-30g | Grasas: ~30-35g | Carbohidratos: ~100-110g
        · Puntos Fuertes: Forma eficiente de consumir muchas calorías de calidad
        """)
        
        st.info("""
        **🍛 Arroz Frito con Ternera, Verduras y Huevo**
        · Porción: 1.5 tazas de arroz, 120g de ternera, 1 huevo, 1 taza de verduras
        · Calorías: ~700-800 kcal
        · Proteínas: ~35-40g | Grasas: ~25-30g | Carbohidratos: ~90-100g
        · Puntos Fuertes: Plato muy calórico y sabroso, excelente post-entreno
        """)
        
        st.info("""
        **🥪 Sándwich de Pan Integral con Pollo, Aguacate y Mayonesa de Yogur**
        · Porción: 2 rebanadas de pan, 120g de pollo, 1/2 aguacate
        · Calorías: ~500-600 kcal
        · Proteínas: ~35-40g | Grasas: ~20-25g | Carbohidratos: ~45-55g
        · Puntos Fuertes: Forma sencilla y portable de añadir calorías buenas
        """)
        
        st.info("""
        **🥩 Filete de Ternera con Puré de Patatas y Maíz**
        · Porción: 1 filete de ternera (180g), 1.5 tazas de puré, 1/2 taza de maíz
        · Calorías: ~750-850 kcal
        · Proteínas: ~45-50g | Grasas: ~30-35g | Carbohidratos: ~70-80g
        · Puntos Fuertes: Plato muy denso y tradicional, rico en hierro y proteína
        """)
