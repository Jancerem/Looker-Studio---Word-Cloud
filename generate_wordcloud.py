import pandas as pd
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# 1️⃣ Leer datos desde Google Sheet público
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTwDOPQYznFyg_EwMENdzeP44Ua8gCB2eiyfqTPcm8tJFdXXFXKNanolv60T_1u5lFMT6ZI0Je04bC8/pub?output=csv"
df = pd.read_csv(url)
col_name = "¿Cuál es la problemática que estás viviendo actualmente dentro de la UANL?"
data = df[col_name].dropna().tolist()

# -----------------------------
# 2️⃣ Filtrar palabras irrelevantes
stop_words = ["el","la","los","las","un","una","unos","unas","de","del","que",
              "en","y","se","por","con","ellos","última","lo","mi","me","nosotros",
              "si","a","al","para"]

words = []
for respuesta in data:
    respuesta = re.sub(r'[^\w\s]', '', str(respuesta).lower())
    for palabra in respuesta.split():
        if palabra not in stop_words:
            words.append(palabra)

word_freq = Counter(words)

# -----------------------------
# 3️⃣ Crear un gradiente personalizado (azul→cyan→amarillo)
from matplotlib import cm

def azul_cyan_amarillo_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    norm = min(max(word_freq[word]/max(word_freq.values()), 0), 1)
    # Gradiente usando cmap de matplotlib
    color = cm.get_cmap("winter")(norm)  # azul → cyan
    # Añadimos un toque amarillo para palabras más frecuentes
    r, g, b, _ = color
    r = r + (1-norm)*0.8  # agregar amarillo según frecuencia
    g = g + (1-norm)*0.8
    b = b  # mantener azul-cyan
    r, g, b = [min(1, x) for x in (r, g, b)]
    return f"rgb({int(r*255)}, {int(g*255)}, {int(b*255)})"

# -----------------------------
# 4️⃣ Generar Word Cloud profesional
wc = WordCloud(
    width=1200,
    height=800,
    background_color="white",   # fondo blanco
    max_words=150,
    relative_scaling=0.5,
    colormap="winter",          # base azul→cyan
    prefer_horizontal=0.9,
    font_path=None               # None = fuente predeterminada; puedes poner ruta a TTF
).generate_from_frequencies(word_freq)

# Recolor con nuestra función personalizada
wc.recolor(color_func=azul_cyan_amarillo_color_func)

# -----------------------------
# 5️⃣ Guardar imagen PNG
wc.to_file("wordcloud_profesional.png")
print("Word Cloud profesional generado ✅")
