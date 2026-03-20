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
    </style>
    """, unsafe_allow_html=True)

st.title("🔍 Find Easy")

foto = st.camera_input("Scanner")

if foto:
    img = Image.open(foto)
    img_gris = ImageOps.grayscale(img)
    resultado = decode(img_gris)

    if resultado:
        for codigo in resultado:
            ean = codigo.data.decode('utf-8')
            
            st.markdown(f"""
                <div style="background-color: #a8e094; padding: 15px; border-radius: 8px; border-left: 10px solid #2e4a25; margin-bottom: 20px;">
                    <span style="color: #2e4a25; font-size: 20px;">✅ <b>!Código detectado:</b> {ean}</span>
                </div>
            """, unsafe_allow_html=True)
            
            st.write("---")
            
            # 3. TIENDAS (Versión corregida para evitar errores de sintaxis)
            tiendas = [
                {"n": "Cooperativa Obrera", "u": f"https://www.lacoopeencasa.coop/buscar?q={ean}"},
                {"n": "Carrefour", "u": f"https://www.google.com.ar/search?q=site:carrefour.com.ar+{ean}"},
                {"n": "Coto Digital", "u": f"https://www.cotodigital3.com.ar/sitios/cdigi/browse?question={ean}"},
                {"n": "Jumbo", "u": f"https://www.google.com.ar/search?q=site:jumbo.com.ar+{ean}"},
                {"n": "Vea", "u": f"https://www.google.com.ar/search?q=site:vea.com.ar+{ean}"},
                {"n": "Día", "u": f"https://www.google.com.ar/search?q=site:supermerca-dosdia.com.ar+{ean}"}
            ]
            
            for t in tiendas:
                st.markdown(f'<a href="{t["u"]}" target="_blank" class="res-block">{t["n"]}: Consultar</a>', unsafe_allow_html=True)
                
    else:
        st.warning("⚠️ No se detectó el código. Probá con más luz.")

st.caption("Find Easy v1.1 | Laprida")
