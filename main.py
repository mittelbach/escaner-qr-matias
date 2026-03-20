import streamlit as st
import urllib.parse

# Configuración de la App - Nodo Laprida
st.set_page_config(page_title="Easy Find - Sensor de Plaza", layout="centered")
st.title("🔍 Easy Find: Sensor de Plaza")

# 1. ENTRADA DE DATOS (Captura de EAN)
st.markdown("### 1. Captura de Identidad")
ean_input = st.text_input("Pegá el Código EAN-13 capturado:", placeholder="Ej: 7790520028709")

if ean_input:
    ean_limpio = ean_input.strip()
    query_ean = urllib.parse.quote(ean_limpio)
    
    # PASO 1: Identificación Global (La "Traducción")
    st.info("**Paso 1:** Si no sabés el nombre exacto, buscalo aquí para identificarlo.")
    
    url_identidad = f"https://www.google.com.ar/search?q=producto+codigo+EAN+{query_ean}"
    st.markdown(f'''
        <a href="{url_identidad}" target="_blank" style="text-decoration:none;">
            <div style="background-color: #4285F4; color: white; padding: 12px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 20px;">
                🌐 Identificar Producto en Google
            </div>
        </a>
    ''', unsafe_allow_html=True)

    st.divider()

    # PASO 2: Entrada del nombre real (Ingeniería Inversa)
    st.markdown("### 2. Confirmación de Producto")
    # Dejamos el campo vacío o con el EAN para que el usuario escriba el nombre real
    nombre_real = st.text_input("Escribí el NOMBRE REAL (Ej: Ceramicol Lustramuebles):", value="")
    
    if nombre_real:
        # Verificación de seguridad para no mandar números a Shopping
        if nombre_real.isdigit():
            st.warning("⚠️ **¡Cuidado!** Estás buscando por número. Para que funcione bien, escribí el nombre del producto (ej: 'Ceramicol')")
        
        query_final = urllib.parse.quote(nombre_real)
        
        st.subheader("Paso 3: Análisis de Valor de Plaza")
        
        # EL MOTOR PRINCIPAL: Google Shopping
        url_shopping = f"https://www.google.com.ar/search?q={query_final}&tbm=shop"
        
        st.markdown(f'''
            <a href="{url_shopping}" target="_blank" style="text-decoration:none;">
                <div style="background-color: #34A853; color: white; padding: 25px; border-radius: 12px; text-align: center; font-weight: bold; font-size: 1.3em; border: 2px solid #2d8e47; margin-bottom: 20px;">
                    🛒 VER VALOR EN GOOGLE SHOPPING
                </div>
            </a>
        ''', unsafe_allow_html=True)
        
        st.caption(f"Buscando: **{nombre_real}**. Google Shopping comparará precios de las principales tiendas.")

else:
    st.write("---")
    st.warning("Esperando código EAN para iniciar el protocolo de ingeniería inversa.")
    st.caption("Usa la app de Team2swift para escanear y pegá el código aquí.")
