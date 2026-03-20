import streamlit as st
import urllib.parse

# Configuración de la App
st.set_page_config(page_title="Easy Find - Sensor de Plaza", layout="centered")
st.title("🔍 Easy Find: Sensor de Plaza")

# 1. ENTRADA DE DATOS
ean_input = st.text_input("1. Pegá el Código EAN-13:", placeholder="Ej: 7798092965941")

if ean_input:
    ean_limpio = ean_input.strip()
    query_ean = urllib.parse.quote(ean_limpio)
    
    # PASO 1: Identificación de Identidad
    st.subheader("Paso 1: Identificar el Nombre")
    st.info("Buscá qué producto es este código en la red global:")
    
    url_identidad = f"https://www.google.com.ar/search?q=producto+codigo+EAN+{query_ean}"
    st.markdown(f'''
        <a href="{url_identidad}" target="_blank" style="text-decoration:none;">
            <div style="background-color: #4285F4; color: white; padding: 15px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 20px;">
                🌐 Buscar Identidad Real en Google
            </div>
        </a>
    ''', unsafe_allow_html=True)

    st.divider()

    # PASO 2: Búsqueda Semántica por Nombre
    st.subheader("Paso 2: Consultar Valor de Plaza")
    nombre_real = st.text_input("Confirmá el nombre del producto aquí:", value=ean_limpio)
    
    if nombre_real:
        query_final = urllib.parse.quote(nombre_real)
        
        # BOTÓN PRINCIPAL: GOOGLE SHOPPING (El sensor de valor real)
        url_shopping = f"https://www.google.com.ar/search?q={query_final}&tbm=shop"
        st.markdown(f'''
            <a href="{url_shopping}" target="_blank" style="text-decoration:none;">
                <div style="background-color: #34A853; color: white; padding: 25px; border-radius: 12px; text-align: center; font-weight: bold; font-size: 1.3em; border: 2px solid #2d8e47;">
                    🛒 VER VALOR EN GOOGLE SHOPPING
                </div>
            </a>
        ''', unsafe_allow_html=True)
        
        st.write("")
        st.caption("Nota: Al buscar por nombre en Shopping, evitás los errores de indexación de los supermercados.")

else:
    st.warning("Esperando código EAN para iniciar el protocolo.")
