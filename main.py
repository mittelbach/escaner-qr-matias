import streamlit as st
import urllib.parse

# Configuración de la App
st.set_page_config(page_title="Easy Find - Ingeniería Inversa", layout="centered")
st.title("🔍 Easy Find: Sensor de Plaza")

# 1. ENTRADA DE DATOS
ean_input = st.text_input("1. Pegá el Código EAN-13:", placeholder="Ej: 7798092965941")

if ean_input:
    ean_limpio = ean_input.strip()
    query_ean = urllib.parse.quote(ean_limpio)
    
    # PASO 1: Identificación de Identidad (Para códigos mentirosos)
    st.subheader("Paso 1: Identificar el Nombre")
    st.info("Si el código es genérico o 'mentiroso', buscalo primero en Google:")
    
    url_identidad = f"https://www.google.com.ar/search?q=producto+codigo+EAN+{query_ean}"
    st.markdown(f'''
        <a href="{url_identidad}" target="_blank" style="text-decoration:none;">
            <div style="background-color: #4285F4; color: white; padding: 12px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 20px;">
                🌐 Buscar Identidad Real (Google)
            </div>
        </a>
    ''', unsafe_allow_html=True)

    st.divider()

    # PASO 2: Búsqueda Semántica por Nombre
    st.subheader("Paso 2: Consultar Valor de Plaza")
    nombre_real = st.text_input("Confirmá el nombre del producto para buscar:", value=ean_limpio)
    
    if nombre_real:
        query_final = urllib.parse.quote(nombre_real)
        
        # BOTÓN PRINCIPAL: GOOGLE SHOPPING
        url_shopping = f"https://www.google.com.ar/search?q={query_final}&tbm=shop"
        st.markdown(f'''
            <a href="{url_shopping}" target="_blank" style="text-decoration:none;">
                <div style="background-color: #34A853; color: white; padding: 18px; border-radius: 10px; text-align: center; font-weight: bold; font-size: 1.1em; border: 2px solid #2d8e47; margin-bottom: 20px;">
                    🛒 VER VALOR EN GOOGLE SHOPPING
                </div>
            </a>
        ''', unsafe_allow_html=True)

        # COMPARATIVA EN NODOS ESPECÍFICOS
        st.write("Verificar en tiendas locales:")
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
                        <div style="background-color: #f8f9fa; color: #31333f; padding: 10px; border-radius: 8px; border: 1px solid #dee2e6; text-align: center; margin-bottom: 8px; font-size: 0.85em;">
                            Check en {t["n"]}
                        </div>
                    </a>
                ''', unsafe_allow_html=True)

else:
    st.warning("Esperando código EAN para iniciar el protocolo.")
