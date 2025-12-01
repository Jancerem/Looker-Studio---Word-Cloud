import pandas as pd
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from random import choice
import requests
from io import StringIO

# -----------------------------
# 1️⃣ Descargar datos del Google Spreadsheet público
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTwDOPQYznFyg_EwMENdzeP44Ua8gCB2eiyfqTPcm8tJFdXXFXKNanolv60T_1u5lFMT6ZI0Je04bC8/pub?output=csv"
response = requests.get(url)
csv_data = StringIO(response.text)
df = pd.read_csv(csv_data, encoding='utf-8')

# Nombre de la columna que contiene las respuestas
column_name = df.columns[5]  # columna F
data = df[column_name].dropna().tolist()

# -----------------------------
# 2️⃣ Filtrar palabras irrelevantes (stopwords)
stop_words = ["EL","LA","LOS","LAS","UN","UNA","UNOS","UNAS","DE","DEL","QUE",
              "EN","Y","SE","POR","CON","ELLOS","ÚLTIMA","LO","MI","ME","NOSOTROS",
              "SI","A","AL","PARA"]

words = []
for respuesta in data:
    # quitar signos de puntuación, mantener acentos y ñ
    respuesta = re.sub(r'[^\w\sáéíóúüñÁÉÍÓÚÜÑ]', '', str(respuesta))
    for palabra in respuesta.split():
        if palabra.upper() not in stop_words:
            words.append(palabra.upper())

# Contar frecuencia de cada palabra
word_freq = Counter(words)

# -----------------------------
# 3️⃣ Función para colores personalizados
from matplotlib import cm
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    norm = min(max(word_freq[word]/max(word_freq.values()), 0), 1)
    color = cm.get_cmap("winter")(norm)  # azul → cyan
    r, g, b, _ = color
    r = r + (1-norm)*0.8
    g = g + (1-norm)*0.8
    b = b
    r, g, b = [min(1, x) for x in (r, g, b)]
    return f"rgb({int(r*255)}, {int(g*255)}, {int(b*255)})"

# -----------------------------
# 4️⃣ Crear WordCloud
wc = WordCloud(
    width=1200,
    height=800,
    background_color="white",
    max_words=200,
    font_path=None,  # usa DejaVuSans, soporta acentos y ñ
    prefer_horizontal=0.9,
).generate_from_frequencies(word_freq)

# Aplicar gradiente de colores
wc.recolor(color_func=color_func)

# -----------------------------
# 5️⃣ Guardar y mostrar
wc.to_file("wordcloud_profesional.png")
plt.figure(figsize=(15,10))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

print("✅ Word Cloud profesional generado con acentos y ñ intactos")
