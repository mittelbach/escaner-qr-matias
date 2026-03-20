import streamlit as st
from pyzbar.pyzbar import decode
from PIL import Image, ImageOps
import numpy as np

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Find Easy", layout="centered", initial_sidebar_state="collapsed")

# Estilo CSS para replicar tu diseño de bloques verdes
st.markdown("""
    <style>
    .stApp {
        background-color: #fdfae7;
    }
    .res-block {
        background-color: #a8e094;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 10px;
        border: 1px solid #8ec67d;
        color: #1e3a15;
        font-weight: bold;
        text-decoration: none;
        display: block;
    }
    .res-block:hover {
        background-color: #92d07a;
        border-color: #2e4a25;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔍 Find Easy")

# 2. ENTRADA DE CÁMARA
foto = st.camera_input("Scanner")

if foto:
    # Abrir la imagen
    img = Image.open(foto)
    
    # PRE-PROCESAMIENTO PARA MEJORAR LECTURA EN CASA
    # Convertimos a escala de grises y aumentamos contraste
    img_gris = ImageOps.grayscale(img)
    img_array = np.array(img_gris)
    # Normalización básica para resaltar las barras negras
    img_procesada = Image.fromarray(img_array)
    
    # Decodificar
    resultado = decode(img_procesada)

    if resultado:
        for codigo in resultado:
            ean = codigo.data.decode('utf-8')
            
            # Bloque de éxito (Diseño Matías)
            st.markdown(f"""
                <div style="background-color: #a8e094; padding: 15px; border-radius: 5px; border-left: 10px solid #2e4a25; margin-bottom: 20px;">
                    <span style="color: #2e4a25; font-size: 18px;">✅ <b>!Código detectado:</b> {ean}</span>
                </div>
            """, unsafe_allow_html=True)
            
            st.write("---")
            
            # 3. DEFINICIÓN DE TIENDAS (Evitando 504 con Google Bridge)
            tiendas = [
                {"n": "Cooperativa Obrera", "u": f"https://www.lacoopeencasa.coop/buscar?q={ean}"},
                {"n": "Carrefour
