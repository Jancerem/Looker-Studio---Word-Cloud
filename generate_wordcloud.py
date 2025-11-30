import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import random
import requests
from io import StringIO

# -----------------------------
# 1️⃣ Leer datos del Google Spreadsheet
# -----------------------------
# Tu CSV publicado de Google Sheets
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTwDOPQYznFyg_EwMENdzeP44Ua8gCB2eiyfqTPcm8tJFdXXFXKNanolv60T_1u5lFMT6ZI0Je04bC8/pub?output=csv"
resp = requests.get(url)
csv_data = StringIO(resp.text)
df = pd.read_csv(csv_data)

# Columna F: problemática
text = " ".join(df['F'].dropna())

# -----------------------------
# 2️⃣ Palabras a ignorar (stopwords personalizadas)
# -----------------------------
custom_stopwords = set(STOPWORDS)
custom_stopwords.update([
    "el", "la", "los", "las", "ellos", "una", "un", "en", "y", "de", "que", "me", "mi", "se", "para", "del"
])

# -----------------------------
# 3️⃣ Función para colores
# -----------------------------
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    palette = ["#00FFFF", "#9B30FF", "#FFFF00"]  # cian, morado, amarillo eléctricos
    return random.choice(palette)

# -----------------------------
# 4️⃣ Generar Word Cloud
# -----------------------------
wc = WordCloud(
    width=800,
    height=600,
    background_color="white",
    max_words=200,
    stopwords=custom_stopwords,
    colormap=None
).generate(text)

wc.recolor(color_func=color_func)

# -----------------------------
# 5️⃣ Guardar imagen
# -----------------------------
wc.to_file("wordcloud_profesional.png")

# -----------------------------
# 6️⃣ Mostrar imagen (opcional, útil en Colab)
# -----------------------------
plt.figure(figsize=(10,8))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
