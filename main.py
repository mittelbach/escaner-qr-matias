import streamlit as st
import urllib.parse

# Configuración de UI para el Nodo Laprida
st.set_page_config(page_title="Easy Find - Valor de Plaza", layout="centered")
st.title("🔍 Easy Find: Sensor de Precios")

# 1. INPUT DE DATOS (Captura de EAN)
ean_input = st.text_input("1. Pegá el Código EAN-13:", placeholder="Ej: 7791274000928")

if ean_input:
    ean_limpio = ean_input.strip()
    query_ean = urllib.parse.quote(ean_limpio)
    
    # PASO 1: Identificación Global
    st.subheader("Paso 1: ¿Qué producto es?")
    url_identidad = f"https://www.google.com.ar/search?q=producto+codigo+EAN+{query_ean}"
    
    st.markdown(f'''
        <a href="{url_identidad}" target="_blank" style="text-decoration:none;">
            <div style="background-color: #4285F4; color: white; padding: 12px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 20px;">
                🌐 Identificar Nombre en Google (clic aquí)
            </div>
        </a>
    ''', unsafe_allow_html=True)

    # PASO 2: Entrada del nombre real (Ingeniería Inversa)
    nombre_real = st.text_input("2. Confirmá el Nombre del Producto:", placeholder="Ej: Espuma Algabo Piel Sensible 200ml")
    
    if nombre_real:
        query_final = urllib.parse.quote(nombre_real)
        
        st.divider()
        st.subheader("Paso 3: Análisis de Valor de Plaza")
        
        # EL NODO CRÍTICO: Google Shopping
        url_shopping = f"https://www.google.com.ar/search?q={query_final}&tbm=shop"
        
        st.markdown(f'''
            <a href="{url_shopping}" target="_blank" style="text-decoration:none;">
                <div style="background-color: #34A853; color: white; padding: 18px; border-radius: 10px; text-align: center; font-weight: bold; font-size: 1.1em; border: 2px solid #2d8e47; margin-bottom: 20px;">
                    🛒 VER VALOR EN GOOGLE SHOPPING (Plaza Total)
                </div>
            </a>
        ''', unsafe_allow_html=True)

        # NODOS DE REFERENCIA LOCAL (Específicos)
        st.write("Comparativa en Nodos Específicos:")
        nodos = [
            {"n": "Carrefour", "u": f"https://www.google.com.ar/search?q=site:carrefour.com.ar+{query_final}"},
            {"n": "La Coope en Casa", "u": f"https://www.lacoopeencasa.coop/buscar?q={query_final}"},
            {"n": "Coto Digital", "u": f"https://www.cotodigital3.com.ar/sitios/cdigital/search?question={query_final}"},
            {"n": "Mercado Libre", "u": f"https://listado.mercadolibre.com.ar/{query_final}"}
        ]

        cols = st.columns(2)
        for i, t in enumerate(nodos):
            with cols[i % 2]:
                st.markdown(f'''
                    <a href="{t["u"]}" target="_blank" style="text-decoration:none;">
                        <div style="background-color: #f8f9fa; color: #31333f; padding: 12px; border-radius: 8px; border: 1px solid #dee2e6; text-align: center; margin-bottom: 10px; font-size: 0.9em;">
                            Check en {t["n"]}
                        </div>
                    </a>
                ''', unsafe_allow_html=True)

else:
    st.info("
