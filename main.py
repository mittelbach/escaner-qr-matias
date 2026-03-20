import streamlit as st
from pyzbar.pyzbar import decode
from PIL import Image, ImageOps

# Configuración de página con el nombre de tu proyecto
st.set_page_config(page_title="Find Easy", layout="centered")

st.title("🔍 Find Easy")

# El componente de cámara para el celular
foto = st.camera_input("Scanner")

if foto:
    img = Image.open(foto)
    # Pasamos a gris para mejorar la lectura del EAN
    img_gris = ImageOps.grayscale(img)
    resultado = decode(img_gris)

    if resultado:
        for codigo in resultado:
            ean = codigo.data.decode('utf-8')
            # El bloque verde de éxito según tu diseño
            st.success(f"✅ !Código detectado: {ean}")
            
            st.markdown("---")
            
            # Definimos las rutas de búsqueda para las cadenas
            # Usamos Google como "puente" para evitar bloqueos directos (504)
            tiendas = [
                {"nombre": "Cooperativa Obrera", "url": f"https://www.lacoopeencasa.coop/buscar?q={ean}"},
                {"nombre": "Carrefour", "url": f"https://www.google.com.ar/search?q=site:carrefour.com.ar+{ean}"},
                {"nombre": "Coto", "url": f"https://www.cotodigital3.com.ar/sitios/cdigi/browse?question={ean}"},
                {"nombre": "Jumbo", "url": f"https://www.google.com.ar/search?q=site:jumbo.com.ar+{ean}"},
                {"nombre": "Vea", "url": f"https://www.google.com.ar/search?q=site:vea.com.ar+{ean}"},
                {"nombre": "Día", "url": f"https://www.google.com.ar/search?q=site:supermerca-dosdia.com.ar+{ean}"}
            ]
            
            # Generamos los bloques de resultados
            for t in tiendas:
                st.link_button(f"{t['nombre']}: Consultar", t['url'], use_container_width=True)
    else:
        st.warning("No se detectó el código. Intentá alejar un poco el producto para que no salga borroso.")
