### pip install google-genai streamlit pandas python-dotenv
import streamlit as st
import pandas as pd
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

### 1- Cargar variables de entorno locales
load_dotenv()


### Configuración visual 
st.set_page_config(page_title="Asistente E-commerce", page_icon="🛍️", layout="centered")
st.title("🛍️ Asistente Virtual de la Tienda")
st.write("Hazme cualquier pregunta sobre envíos, devoluciones o políticas de la tienda.")


### 2- Cargar el contexto (Caché para optimizar el rendimiento)
@st.cache_data
def cargar_contexto():
    ruta_archivo = "documentacion_tienda.csv"
    if not os.path.exists(ruta_archivo):
        return "Error: No se encontró el archivo de documentación."
    
    try:
        df = pd.read_csv(ruta_archivo, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(ruta_archivo, encoding="latin-1")
        
    df.columns = df.columns.str.strip()
    contexto = "\n\n".join(
        f"--- {row['Documento']} ---\n{row['Contenido']}"
        for _, row in df.iterrows()
    )
    return contexto

contexto_completo = cargar_contexto()


### 3 - Inicializar el cliente Gemini
### Busca la clave en el .env (local) o en los secrets de Streamlit (producción)
api_key = os.environ.get("AluraChallenge") or st.secrets.get("AluraChallenge")
client = genai.Client(api_key=api_key)

def generar_respuesta(pregunta):
    instrucciones = f"""Eres el agente de atención al cliente de una tienda online de ropa y accesorios.
Responde ÚNICAMENTE basándote en la documentación oficial proporcionada.
Si la respuesta no está en el contexto, di: 'No tengo esa información, por favor contacta a soporte.'
Responde de forma amable, clara y concisa.

Documentación:
{contexto_completo}"""

    configuracion = types.GenerateContentConfig(
        system_instruction=instrucciones,
        temperature=0.2,
    )

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=pregunta,
        config=configuracion
    )
    return response.text


### 4- Manejo del estado de la sesión (Historial de chat)
if "mensajes" not in st.session_state:
    st.session_state.mensajes = [
        {"role": "assistant", "content": "¡Hola! Soy el asistente virtual de la tienda. ¿En qué te puedo ayudar hoy?"}
    ]


### Mostrar los mensajes anteriores en la interfaz
for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])


### 5- Capturar la entrada del usuario
if prompt := st.chat_input("Escribe tu pregunta aquí... (ej. ¿Cuánto demoran los envíos?)"):
    
    # Mostrar la pregunta del usuario en pantalla y guardarla
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.mensajes.append({"role": "user", "content": prompt})

    # Mostrar "Pensando..." mientras la API responde, luego imprimir y guardar la respuesta
    with st.chat_message("assistant"):
        with st.spinner("Buscando en la documentación..."):
            respuesta = generar_respuesta(prompt)
            st.markdown(respuesta)
    st.session_state.mensajes.append({"role": "assistant", "content": respuesta})