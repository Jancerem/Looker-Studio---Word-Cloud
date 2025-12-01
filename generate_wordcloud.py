import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from random import choice
import unicodedata
import requests
from io import StringIO

# --- 1️⃣ Descargar datos del Google Spreadsheet (hoja Word Cloud) ---
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTwDOPQYznFyg_EwMENdzeP44Ua8gCB2eiyfqTPcm8tJFdXXFXKNanolv60T_1u5lFMT6ZI0Je04bC8/pub?gid=1639666393&single=true&output=csv"

response = requests.get(url)
csv_data = StringIO(response.text)

# Leer CSV en UTF-8, sin que la primera fila sea usada como header
df = pd.read_csv(csv_data, encoding='utf-8')

# --- 2️⃣ Unir todas las respuestas de la columna A ---
column_index = 0  # columna A
text = " ".join(df[column_index].dropna())  # ahora incluye fila 1

# --- 2️⃣b Agregar stopwords ---
from wordcloud import STOPWORDS
mis_stopwords = set(STOPWORDS)
mis_stopwords.update(["DE", "LA", "EL", "QUE", "Y", "EN", "A", "POR"])

# --- 3️⃣ Función para colores personalizados ---
from random import choice
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colores = ["#00FFFF", "#BF00FF", "#FFFF00"]  # cian, morado, amarillo eléctricos
    return choice(colores)

# --- 4️⃣ Crear WordCloud ---
from wordcloud import WordCloud
import matplotlib.pyplot as plt
wc = WordCloud(
    width=800,
    height=600,
    background_color="white",
    max_words=200,
    font_path="fonts/DejaVuSans-Bold.ttf",
    color_func=color_func,
    stopwords=mis_stopwords,
    collocations=False
).generate(text)

# --- 5️⃣ Guardar PNG ---
wc.to_file("wordcloud_profesional.png")

# --- 6️⃣ Mostrar (opcional) ---
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
