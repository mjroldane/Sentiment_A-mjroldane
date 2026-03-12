import streamlit as st
from textblob import TextBlob
from PIL import Image
from googletrans import Translator
from streamlit_lottie import st_lottie # Importación según la imagen
import json # Importación según la imagen

st.title('Análisis de Sentimiento')

# Imagen de encabezado
try:
    image = Image.open('emoticones.jpg')
    st.image(image)
except:
    pass

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

translator = Translator()

with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.write("""
        Polaridad: Indica si el sentimiento es positivo, negativo o neutral. 
        Su valor oscila entre -1 y 1.
        
        Subjetividad: Mide cuánto del contenido es opinión frente a hechos. 
        Va de 0 a 1.
    """)

with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')
    
    if text:
        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        
        x = round(blob.sentiment.polarity, 2)
        st.write('Polarity: ', x)
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity, 2))

        # --- Lógica para mostrar las animaciones JSON ---
        
        if x > 0:
            st.write('Es un sentimiento Positivo 😊')
            archivo_json = 'happycow.json'
        elif x < 0:
            st.write('Es un sentimiento Negativo 😔')
            archivo_json = 'saddog.json'
        else:
            st.write('Es un sentimiento Neutral 😐')
            archivo_json = 'neutralcow.json'

        # Código siguiendo la estructura de la imagen del profesor
        try:
            with open(archivo_json) as source:
                animation = json.load(source)
            st.lottie(animation, width=350)
        except FileNotFoundError:
            st.error(f"No se encontró el archivo {archivo_json}")
