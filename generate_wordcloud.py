import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import random
import requests
from io import StringIO

# -----------------------------
# 1️⃣ Leer datos del Google Spreadsheet
# -----------------------------
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTwDOPQYznFyg_EwMENdzeP44Ua8gCB2eiyfqTPcm8tJFdXXFXKNanolv60T_1u5lFMT6ZI0Je04bC8/pub?output=csv"
resp = requests.get(url)
csv_data = StringIO(resp.text)
df = pd.read_csv(csv_data, encoding="utf-8")  # soporte completo de acentos y ñ

# -----------------------------
# 2️⃣ Tomar columna F (índice 5) y pasar a mayúsculas
# -----------------------------
text = " ".join(df.iloc[:, 5].dropna()).upper()  # todo a mayúsculas

# -----------------------------
# 3️⃣ Stopwords personalizadas
# -----------------------------
custom_stopwords = set(STOPWORDS)
custom_stopwords.update([
    "EL", "LA", "LOS", "LAS", "ELLOS", "UNA", "UN", "EN", "Y", "DE", "QUE", "ME", "MI", "SE", "PARA", "DEL"
])

# -----------------------------
# 4️⃣ Función de colores
# -----------------------------
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    palette = ["#00FFFF", "#9B30FF", "#FFFF00"]  # cian, morado, amarillo eléctricos
    return random.choice(palette)

# -----------------------------
# 5️⃣ Generar Word Cloud
# -----------------------------
wc = WordCloud(
    width=800,
    height=600,
    background_color="white",
    max_words=200,
    stopwords=custom_stopwords,
    colormap=None,
    font_path="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # fuente que soporta acentos y ñ
).generate(text)

wc.recolor(color_func=color_func)

# -----------------------------
# 6️⃣ Guardar imagen
# -----------------------------
wc.to_file("wordcloud_profesional.png")

# -----------------------------
# 7️⃣ Mostrar imagen (opcional)
# -----------------------------
plt.figure(figsize=(10,8))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
