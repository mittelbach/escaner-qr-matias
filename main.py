import streamlit as st
from pyzbar.pyzbar import decode
from PIL import Image, ImageOps
import numpy as np

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Find Easy", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #fdfae7; }
    .res-block {
        background-color: #a8e094;
        padding: 18px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 12px;
        border: 1px solid #8ec67d;
        color: #1e3a15;
        font-weight: bold;
        text-decoration: none;
        display: block;
        font-size: 18px;
    }
    .res-block:hover { background-color: #92d07a; border-color: #2e4a25; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔍 Find Easy")

# --- NUEVA FUNCIÓN: INGRESO MANUAL ---
with st.expander("⌨️ Ingresar código manualmente"):
    ean_manual = st.text_input("Escribí los números del código de barras:")
    boton_manual = st.button("Buscar manualmente")

# --- FUNCIÓN DE ESCANEO (CÁMARA) ---
foto = st.camera_input("Scanner")

# Lógica para determinar qué código usar
ean_a_buscar = None

if boton_manual and ean_manual:
    ean_a_buscar = ean_manual
elif foto:
    img = Image.open(foto)
    img_gris = ImageOps.grayscale(img)
    resultado = decode(img_gris)
    if resultado:
        ean_a_buscar = resultado[0].data.decode('utf-8')
    else:
        st.warning("⚠️ No se detectó el código en la foto. Probá escribirlo arriba.")

# --- MOSTRAR RESULTADOS ---
if ean_a_buscar:
    st.markdown(f"""
        <div style="background-color: #a8e094; padding: 15px; border-radius: 8px; border-left: 10px solid #2e4a25; margin-bottom: 20px;">
            <span style="color: #2e4a25; font-size: 20px;">✅ <b>Código a buscar:</b> {ean_a_buscar}</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    tiendas = [
        {"n": "Cooperativa Obrera", "u": f"https://www.lacoopeencasa.coop/buscar?q={ean_a_buscar}"},
        {"n": "Carrefour", "u": f"https://www.google.com.ar/search?q=site:carrefour.com.ar+{ean_a_buscar}"},
        {"n": "Coto Digital", "u": f"https://www.cotodigital3.com.ar/sitios/cdigi/browse?question={ean_a_buscar}"},
        {"n": "Jumbo", "u": f"https://www.google.com.ar/search?q=site:jumbo.com.ar+{ean_a_buscar}"},
        {"n": "Vea", "u": f"https://www.google.com.ar/search?q=site:vea.com.ar+{ean_a_buscar}"},
        {"n": "Día", "u": f"https://www.google.com.ar/search?q=site:supermerca-dosdia.com.ar+{ean_a_buscar}"}
    ]
    
    for t in tiendas:
        st.markdown(f'<a href="{t["u"]}" target="_blank" class="res-block">{
