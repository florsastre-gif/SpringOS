import streamlit as st
from google import genai
import os
import random

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="SPRING OS — Direction Engine", page_icon="🧠", layout="wide")

# Estilo visual
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BIENVENIDA ESTRATÉGICA ---
refranes_inicio = [
    "🚀 'Al que madruga, Dios lo ayuda; pero el que tiene estrategia, no se queda en la duda'.",
    "🧠 'Mucho ruido y pocas nueces'. Vamos a ponerle nueces a esa dirección.",
    "🛡️ 'Al pan, pan, y al vino, vino'. Acá no instalamos humo, instalamos sistema."
]
st.info(random.choice(refranes_inicio))

# --- 3. BARRA LATERAL (AUTENTICACIÓN) ---
with st.sidebar:
    st.title("🔐 Acceso SPRING")
    api_key = st.text_input("Ingresa tu Google API Key:", type="password")
    if api_key:
        client = genai.Client(api_key=api_key)
    st.info("Este es el motor de instalación estratégica. Sin humo, con rima y razón.")

# --- 4. INTERFAZ DE DECISIONES ---
st.title("🧠 SPRING OS — Direction Engine™")
st.markdown("### *Donde la IA no improvisa, aquí se instala dirección.*")

col1, col2 = st.columns(2)
with col1:
    movimiento = st.selectbox("¿A qué santo le rezamos este mes?", 
                             ["Venta (Plata en mano)", "Autoridad (Que sepan quién sos)", "Comunidad (Hacer amigos)"])
    energia = st.selectbox("Energía dominante", 
                          ["Precisión (Bisturí en mano)", "Sofisticación", "Cercanía", "Ambición"])
with col2:
    capacidad = st.select_slider("Capacidad real de ejecución", 
                                options=["Pantuflas (1-2 piezas)", "Zapatillas (3-4 piezas)", "Maratón (Diario)"])
    publico = st.radio("Sofisticación del público", ["Básico", "Intermedio", "Técnico"], horizontal=True)

# --- 5. MOTOR DE INSTALACIÓN (SYSTEM PROMPT) ---
SYSTEM_PROMPT = """
Eres el alma de SPRING OS. Tu voz es una mezcla entre estratega de élite y esa amiga 
que te dice las verdades de frente, con rimas sutiles y refranes letales.

REGLAS DE ORO:
1. ESTRUCTURA: Devuelve siempre 4 secciones numeradas: 1. [ESTRATEGIA], 2. [IDENTIDAD], 3. [EJECUCIÓN] y 4. [SPRING WHISPER].
2. LENGUAJE: Usa refranes (ej: 'Al pan, pan, y al vino, vino').
3. COHERENCIA: Calcula un 'Coherence Score' (1-100%).
4. WHISPER: Un susurro final corto, letal y estratégico.
"""

# --- 6. ACCIÓN ---
if st.button("🔌 INSTALAR DIRECCIÓN"):
    if not api_key:
        st.error("Poné la API Key en la barra lateral.")
    else:
        prompt_usuario = f"Instalar dirección: Movimiento {movimiento}, Energía {energia}, Capacidad {capacidad}, Público {publico}."
        with st.spinner("Acomodando los patitos en fila..."):
            try:
                response = client.models.generate_content(
                    model='gemini-2.0-flash',
                    contents=[SYSTEM_PROMPT, prompt_usuario]
                )
                st.session_state.resultado = response.text
                st.markdown("---")
                st.markdown(st.session_state.resultado)
                st.balloons()
            except Exception as e:
                st.error(f"Error técnico: {e}")

# --- 7. REALITY CHECK ---
if "resultado" in st.session_state:
    st.divider()
    st.subheader("🤔 Reality Check: Mirame a los ojos...")
    check = st.radio("¿Estás dispuesta a ejecutar esto?", ["Elegir...", "Sí", "No, bajame un cambio"])
    
    if check == "No, bajame un cambio":
        st.warning("Recalibrando...")
        recal_prompt = "Simplifica la estrategia al 50%. Menos es más."
        try:
            ajuste = client.models.generate_content(
                model='gemini-2.0-flash',
                contents=[SYSTEM_PROMPT, st.session_state.resultado, recal_prompt]
            )
            st.markdown(ajuste.text)
        except Exception as e:
            st.error(f"Error en recalibración: {e}")
