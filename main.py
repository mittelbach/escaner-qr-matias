import streamlit as st
import urllib.parse

# Configuración de la App - Nodo Laprida
st.set_page_config(page_title="Easy Find - Sensor GS1", layout="centered")
st.title("🔍 Easy Find: Sensor de Plaza")

# 1. ENTRADA DE DATOS
st.markdown("### 1. Captura de Identidad Oficial")
ean_input = st.text_input("Pegá el Código EAN-13:", placeholder="Ej: 7798144810014")

if ean_input:
    ean_limpio = ean_input.strip()
    
    # PASO 1: Consulta Directa a GS1 (La Fuente de Verdad)
    st.info("**Paso 1:** Consultá la base de datos oficial de GS1 para ver quién es el dueño del código.")
    
    # URL directa al buscador de GS1 Argentina
    # Nota: El usuario debe pegar el código en la web de destino, 
    # ya que GS1 requiere validación manual por seguridad.
    url_gs1 = "https://www.gs1.org.ar/Sitio/Bootstrap5/VerifiedGO.html"
    
    st.markdown(f'''
        <a href="{url_gs1}" target="_blank" style="text-decoration:none;">
            <div style="background-color: #002C6C; color: white; padding: 15px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 20px;">
                🏢 Consultar Identidad en GS1 Argentina (Oficial)
            </div>
        </a>
    ''', unsafe_allow_html=True)

    st.divider()

    # PASO 2: Confirmación Semántica
    st.markdown("### 2. Confirmación de Producto")
    st.write("Una vez que GS1 te dé el nombre (ej: Agroliva), escribilo acá:")
    nombre_real = st.text_input("Nombre del Producto / Marca:", value="")
    
    if nombre_real:
        query_final = urllib.parse.quote(nombre_real)
        
        st.subheader("Paso 3: Análisis de Valor de Plaza")
        
        # EL MOTOR DE VALOR: Google Shopping
        url_shopping = f"https://www.google.com.ar/search?q={query_final}&tbm=shop"
        
        st.markdown(f'''
            <a href="{url_shopping}" target="_blank" style="text-decoration:none;">
                <div style="background-color: #34A853; color: white; padding: 25px; border-radius: 12px; text-align: center; font-weight: bold; font-size: 1.3em; border: 2px solid #2d8e47; margin-bottom: 20px;">
                    🛒 VER VALOR EN GOOGLE SHOPPING
                </div>
            </a>
        ''', unsafe_allow_html=True)

else:
    st.warning("Esperando código EAN para iniciar el protocolo.")
