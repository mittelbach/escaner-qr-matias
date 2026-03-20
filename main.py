import streamlit as st
import urllib.parse

# 1. CAPA DE INGENIERÍA INVERSA (Diccionario de Certezas de Matías)
# Aquí guardamos los EAN que internet confunde, para forzar la identidad real.
PRODUCTOS_VERIFICADOS = {
    "7791866001364": "Mayonesa Natura 475g 500cm3",
    "7798092965941": "Desodorante Make Fresh Aerojet", # Corregido: No es Arroz
    "7799175003628": "Sahumerios Momentos Iluminarte x5", # Corregido: No es Pañal
    "7791274000928": "Espuma de afeitar Algabo Men 200ml", # Corregido: No es Gillette
}

def obtener_identidad_real(ean):
    """Devuelve el nombre real si el EAN está verificado, sino devuelve el EAN."""
    return PRODUCTOS_VERIFICADOS.get(ean, ean)

# 2. CONFIGURACIÓN DE UI
st.set_page_config(page_title="Easy Find - Nodo Laprida", layout="centered")
st.title("🔍 Easy Find: Ingeniería Inversa")
st.write("Pegá el código capturado por tu app de Team2swift para encontrar el valor de plaza.")

# 3. INPUT DE DATOS
ean_input = st.text_input("Ingrese Código EAN-13:", placeholder="Ej: 7791274000928")

if ean_input:
    # Proceso de Identidad
    identidad = obtener_identidad_real(ean_input)
    
    if ean_input in PRODUCTOS_VERIFICADOS:
        st.success(f"✅ PRODUCTO VALIDADO: **{identidad}**")
    else:
        st.info(f"🔎 Buscando por código genérico: {ean_input}")

    # 4. GENERACIÓN DE LINKS (Nodos de Búsqueda)
    # Codificamos el texto para que los espacios no rompan el link
    query = urllib.parse.quote(identidad)
    
    nodos = [
        {"n": "Carrefour", "u": f"https://www.google.com.ar/search?q=site:carrefour.com.ar+{query}"},
        {"n": "La Coope en Casa", "u": f"https://www.lacoopeencasa.coop/buscar?q={query}"},
        {"n": "Coto Digital", "u": f"https://www.cotodigital3.com.ar/sitios/cdigital/search?_dyncharset=utf-8&question={query}"},
        {"n": "Mercado Libre (Referencia)", "u": f"https://listado.mercadolibre.com.ar/{query}"}
    ]

    st.subheader("Puntos de Consulta de Valor:")
    
    # 5. RENDERIZADO DE BOTONES (Sin errores de Syntax)
    cols = st.columns(2)
    for i, t in enumerate(nodos):
        with cols[i % 2]:
            # Usamos un f-string limpio con llaves correctamente cerradas
            boton_html = f'''
                <a href="{t["u"]}" target="_blank" style="text-decoration:none;">
                    <div style="
                        background-color: #f0f2f6;
                        color: #31333f;
                        padding: 15px;
                        border-radius: 10px;
                        border: 1px solid #d1d5db;
                        text-align: center;
                        margin-bottom: 10px;
                        font-weight: bold;
                        cursor: pointer;
                    ">
                        Consultar en {t["n"]}
                    </div>
                </a>
            '''
            st.markdown(boton_html, unsafe_allow_html=True)

    st.divider()
    st.caption("Nota: La búsqueda semántica (por nombre) garantiza encontrar el precio de plaza incluso si el EAN no está indexado.")

else:
    st.warning("Esperando ingreso de código para iniciar análisis de plaza...")
