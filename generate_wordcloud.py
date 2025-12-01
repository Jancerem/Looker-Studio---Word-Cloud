import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from random import choice
import unicodedata
import requests
from io import StringIO

# --- 1️⃣ Descargar datos del Google Spreadsheet ---
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTwDOPQYznFyg_EwMENdzeP44Ua8gCB2eiyfqTPcm8tJFdXXFXKNanolv60T_1u5lFMT6ZI0Je04bC8/pub?gid=1639666393&single=true&output=csv"
response = requests.get(url)
csv_data = StringIO(response.text)

# Leer CSV sin encabezado
df = pd.read_csv(csv_data, encoding='utf-8', header=None)

# --- 2️⃣ Unir todas las respuestas de la columna A ---
column_index = 0  # columna A
text = " ".join(df[column_index].dropna())

# --- 2️⃣b Stopwords ---
mis_stopwords = set(STOPWORDS)
mis_stopwords.update(["DE", "LA", "EL", "QUE", "Y", "EN", "A", "POR", "PARA", "ES", "MUY", "TODOS", "TODAS"])

# --- 3️⃣ Función para colores personalizados ---
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colores = ["#FFDD33", "#190B24", "#44C1F2", "#690DAC", "#01E5FF", "#8C3EF4", "#BAA566"]  # cian, morado, amarillo eléctricos
    return choice(colores)

# --- 4️⃣ Crear WordCloud ---
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

# --- 6️⃣ Mostrar limpio en Colab ---
plt.figure(figsize=(12,8))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")  # Quitar ejes
plt.tight_layout(pad=0)  # Quitar márgenes
plt.show()
