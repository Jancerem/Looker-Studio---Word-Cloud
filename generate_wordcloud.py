import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests
from io import StringIO
from random import choice
import unicodedata

# --- 1️⃣ Descargar datos del Google Spreadsheet ---
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTwDOPQYznFyg_EwMENdzeP44Ua8gCB2eiyfqTPcm8tJFdXXFXKNanolv60T_1u5lFMT6ZI0Je04bC8/pub?output=csv"
response = requests.get(url)
csv_data = StringIO(response.text)

# Leer CSV en UTF-8
df = pd.read_csv(csv_data, encoding='utf-8')

# --- 2️⃣ Unir todas las respuestas en una sola cadena ---
column_name = df.columns[5]  # columna F (índice 5)
text = " ".join(df[column_name].dropna())

# --- 2️⃣a Normalizar texto: quitar acentos y ñ ---
def normalizar_texto(texto):
    # descomponer caracteres acentuados
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    # eliminar marcas de acento
    texto_sin_acentos = "".join([c for c in texto_normalizado if not unicodedata.combining(c)])
    # reemplazar ñ y Ñ por n/N
    texto_sin_acentos = texto_sin_acentos.replace("ñ", "n").replace("Ñ", "N")
    return texto_sin_acentos

text = normalizar_texto(text).upper()  # convertir a mayúsculas

# --- 3️⃣ Función para colores personalizados ---
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colores = ["#00FFFF", "#BF00FF", "#FFFF00"]  # cian, morado, amarillo eléctricos
    return choice(colores)

# --- 4️⃣ Crear WordCloud ---
wc = WordCloud(
    width=800,
    height=600,
    background_color="white",
    max_words=200,
    font_path="fonts/Impact.ttf",  # fuente que tengas
    color_func=color_func,
    collocations=False,           # evita separar palabras con espacios o acentos raros
    stopwords=set()               # aquí puedes agregar stopwords si quieres
).generate(text)

# --- 5️⃣ Guardar PNG ---
wc.to_file("wordcloud_profesional.png")

# --- 6️⃣ Mostrar (opcional) ---
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
