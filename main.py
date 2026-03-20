import streamlit as st
from pyzbar.pyzbar import decode
from PIL import Image, ImageOps

# 1. CONFIGURACIÓN
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

# 2. INGRESO MANUAL (Tal cual lo pediste)
with st.expander("⌨️ Ingresar código manualmente"):
    ean_manual = st.text_input("Escribí los números:")
    boton_manual = st.button("Buscar")

# 3. SCANNER
foto = st.camera_input("Scanner")

ean_final = None

if boton_manual and ean_manual:
    ean_final = ean_manual
elif foto:
    img = Image.open(foto)
    img_gris = ImageOps.grayscale(img)
    resultado = decode(img_gris)
    if resultado:
        ean_final = resultado[0].data.decode('utf-8')
    else:
        st.warning("No se detectó el código en la foto.")

# 4. RESULTADOS - ANÁLISIS DE ENLACES
if ean_final:
    st.success(f"Buscando: {ean_final}")
    
    # Optimizamos los links para que Google ayude a encontrar el EAN
    tiendas = [
        ["La Coope", f"https://www.lacoopeencasa.coop/buscar?q={ean_final}"],
        ["Carrefour", f"https://www.google.com.ar/search?q=site:carrefour.com.ar+{ean_final}"],
        ["Coto", f"https://www.google.com.ar/search?q=site:cotodigital3.com.ar+{ean_final}"],
        ["Vea", f"https://www.google.com.ar/search?q=site:vea.com.ar+{ean_final}"],
        ["Día", f"https://www.google.com.ar/search?q=site:supermerca-dosdia.com.ar+{ean_final}"],
        ["Google Shopping", f"https://www.google.com.ar/search?q={ean_final}&tbm=shop"]
    ]
    
    for t in tiendas:
        nombre, url = t[0], t[1]
        st.markdown(f'<a href="{url}" target="_blank" class="res-block">{nombre}: Consultar</a>', unsafe_allow_html=True)

st.caption("Find Easy v1.2 | Laprida")
