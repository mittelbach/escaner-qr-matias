import streamlit as st
import urllib.parse

# Configuración de UI
st.set_page_config(page_title="Easy Find - Ingeniería Inversa", layout="centered")
st.title("🔍 Easy Find: Identificador de Plaza")

# 1. INPUT DE DATOS
ean_input = st.text_input("Ingrese o pegue el Código EAN-13:", placeholder="Ej: 7791274000928")

if ean_input:
    # Limpiamos el código por si viene con espacios
    ean_limpio = ean_input.strip()
    query_ean = urllib.parse.quote(ean_limpio)
    
    st.subheader("Paso 1: Identificar el Nombre")
    st.write("Si no sabés qué producto es, usá este botón para que la red lo identifique:")
    
    # Este botón busca el EAN en todo Google para traerte el NOMBRE real
    url_identidad = f"https://www.google.com.ar/search?q=producto+codigo+EAN+{query_ean}"
    st.markdown(f'''
        <a href="{url_identidad}" target="_blank" style="text-decoration:none;">
            <div style="background-color: #4285F4; color: white; padding: 12px; border-radius: 8px; text-align: center; font-weight: bold;">
                🌐 Buscar Identidad en la Red (Google)
            </div>
        </a>
    ''', unsafe_allow_html=True)

    st.divider()

    # 2. BÚSQUEDA SEMÁNTICA (Por nombre o por código)
    st.subheader("Paso 2: Consultar Valor de Plaza")
    nombre_manual = st.text_input("¿Qué producto es? (Ej: Espuma Algabo 200ml)", value=ean_limpio)
    
    query_final = urllib.parse.quote(nombre_manual)
    
    nodos = [
        {"n": "Carrefour", "u": f"https://www.google.com.ar/search?q=site:carrefour.com.ar+{query_final}"},
        {"n": "La Coope en Casa", "u": f"https://www.lacoopeencasa.coop/buscar?q={query_final}"},
        {"n": "Coto Digital", "u": f"https://www.cotodigital3.com.ar/sitios/cdigital/search?question={query_final}"},
        {"n": "Mercado Libre", "u": f"https://listado.mercadolibre.com.ar/{query_final}"}
    ]

    cols = st.columns(2)
    for i, t in enumerate(nodos):
        with cols[i % 2]:
            boton_html = f'''
                <a href="{t["u"]}" target="_blank" style="text-decoration:none;">
                    <div style="background-color: #f0f2f6; color: #31333f; padding: 15px; border-radius: 10px; border: 1px solid #d1d5db; text-align: center; margin-bottom: 10px; font-weight: bold;">
                        Consultar en {t["n"]}
                    </div>
                </a>
            '''
            st.markdown(boton_html, unsafe_allow_html=True)

else:
    st.info("Esperando código EAN para iniciar el protocolo.")
