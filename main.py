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

# 2. INGRESO MANUAL
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

# 4. RESULTADOS
if ean_final:
    st.success(f"Buscando: {ean_final}")
    
    # Lista de tiendas simplificada para evitar errores de sintaxis
    tiendas = [
        ["Cooperativa Obrera", f"https://www.lacoopeencasa.coop/buscar?q={ean_final}"],
        ["Carrefour", f"https://www.google.com.ar/search?q=site:carrefour.com.ar+{ean_final}"],
        ["Coto Digital", f"https://www.cotodigital3.com.ar/sitios/cdigi/browse?question={ean_final}"],
        ["Jumbo", f"https://www.google.com.ar/search?q=site:jumbo.com.ar+{ean_final}"],
        ["Vea", f"https://www.google.com.ar/search?q=site:vea.com.ar+{ean_final}"],
        ["Día", f"https://www.google.com.ar/search?q=site:supermerca-dosdia.com.ar+{ean_final}"]
    ]
    
    for t in tiendas:
        nombre = t[0]
        url = t[1]
        st.markdown(f'<a href="{url}" target="_blank" class="res-block">{nombre}: Consultar</a>', unsafe_allow_html=True)

st.caption("Find Easy v1.2 | Laprida")
