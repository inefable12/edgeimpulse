import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="EDGE IMPULSE", layout="wide")
st.image("imagenes/image1.png")

# Pestañas
tabs = ["Introducción", "Aplicaciones", "Tutorial"]
selected_tab = st.sidebar.radio("Selecciona una sección", tabs)

# Ruta base de imágenes en GitHub (ajústala según tu repositorio)
GITHUB_BASE_URL = "https://github.com/inefable12/edgeimpulse/tree/main/imagenes/"
#"https://raw.githubusercontent.com/tu_usuario/tu_repositorio/main/imagenes/"

if selected_tab == "Introducción":
    st.title("Introducción a EDGE IMPULSE")
    st.write("""
    Edge Impulse es una plataforma que permite el desarrollo de modelos de Machine Learning embebido, 
    conocida como **TinyML**. TinyML permite ejecutar modelos de inteligencia artificial en dispositivos 
    con recursos limitados, como **Arduino, ESP32, Raspberry Pi** y otros microcontroladores.
    
    Con Edge Impulse, los desarrolladores pueden capturar datos, entrenar modelos y desplegarlos fácilmente 
    en hardware embebido para aplicaciones como reconocimiento de voz, detección de movimiento y visión por computadora.
    """)
    
    # Cargar imagen desde GitHub
    image_url = GITHUB_BASE_URL + "imagen1.png"
    st.image(image_url, caption="TinyML con Edge Impulse", use_column_width=True)

elif selected_tab == "Aplicaciones":
    st.title("Aplicaciones de EDGE IMPULSE")
    st.write("""
    Edge Impulse se usa en diversos campos, incluyendo:
    - **Dispositivos de salud**: Monitoreo de signos vitales con sensores portátiles.
    - **Agricultura de precisión**: Detección de plagas mediante visión artificial.
    - **Automatización industrial**: Mantenimiento predictivo en máquinas industriales.
    - **Seguridad**: Identificación de sonidos anómalos en ambientes urbanos.
    """)
    
    # Cargar imagen desde GitHub
    image_url = GITHUB_BASE_URL + "imagen2.jpg"
    st.image(image_url, caption="Aplicaciones de Edge Impulse", use_column_width=True)
    
    # Enlace a ejemplos reales
    st.markdown("[Ver casos de éxito en Edge Impulse](https://www.edgeimpulse.com/use-cases)")

elif selected_tab == "Tutorial":
    st.title("Tutorial: Creando un modelo en EDGE IMPULSE")
    st.write("""
    A continuación, se describen los pasos básicos para crear un modelo con Edge Impulse:
    
    1. **Crear una cuenta** en [Edge Impulse](https://edgeimpulse.com/).
    2. **Configurar un nuevo proyecto** y definir el tipo de datos a recolectar.
    3. **Capturar datos** desde sensores conectados a Arduino o cargar archivos existentes.
    4. **Entrenar un modelo** con los datos capturados.
    5. **Optimizar y probar el modelo** para mejorar precisión y eficiencia.
    6. **Desplegar el modelo** en un dispositivo embebido.
    """)
