import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests
from io import StringIO
from random import choice
import unicodedata
import re

# Descargar datos del Google Spreadsheet
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTwDOPQYznFyg_EwMENdzeP44Ua8gCB2eiyfqTPcm8tJFdXXFXKNanolv60T_1u5lFMT6ZI0Je04bC8/pub?output=csv"
response = requests.get(url)
csv_data = StringIO(response.text)
df = pd.read_csv(csv_data, encoding='utf-8')

# Unir todas las respuestas en una sola cadena
column_name = df.columns[5]
text = " ".join(df[column_name].dropna())

# Normalizar texto: quitar acentos y ñ
def normalizar_texto(texto):
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    texto_sin_acentos = "".join([c for c in texto_normalizado if not unicodedata.combining(c)])
    texto_sin_acentos = texto_sin_acentos.replace("ñ", "n").replace("Ñ", "N")
    # quitar caracteres que no sean letras o espacios
    texto_sin_acentos = re.sub(r"[^A-Za-z ]", "", texto_sin_acentos)
    return texto_sin_acentos

text = normalizar_texto(text).upper()

# Función para colores
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colores = ["#00FFFF", "#BF00FF", "#FFFF00"]
    return choice(colores)

# Crear WordCloud
wc = WordCloud(
    width=800,
    height=600,
    background_color="white",
    max_words=200,
    font_path="fonts/DejaVuSans-Bold.ttf",
    color_func=color_func,
    collocations=False  # <- esto evita separar palabras
).generate(text)

# Guardar PNG
wc.to_file("wordcloud_profesional.png")

# Mostrar opcional
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
