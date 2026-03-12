from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator
from streamlit_lottie import st_lottie  # Falta esta línea
import json                             # Falta esta línea

st.title('Análisis de Sentimiento')
image = Image.open('emoticones.jpg')
st.image(image)
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
        
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        
        x = round(blob.sentiment.polarity, 2)
        
        # 1. Definimos qué archivo usar según el resultado
        if x > 0:
            st.write('Es un sentimiento Positivo 😊')
            archivo_json = 'happycow.json'
        elif x < 0:
            st.write('Es un sentimiento Negativo 😔')
            archivo_json = 'saddog.json'
        else:
            st.write('Es un sentimiento Neutral 😐')
            archivo_json = 'neutralcow.json'

        # 2. Cargamos y mostramos la animación (Instrucciones del profe)
        with open(archivo_json) as source:
            animation = json.load(source)
        
        st_lottie(animation, width=350, key="animacion_emocion")
