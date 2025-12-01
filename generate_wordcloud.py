import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests
from io import StringIO
from random import choice

# --- 1️⃣ Descargar datos del Google Spreadsheet ---
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTwDOPQYznFyg_EwMENdzeP44Ua8gCB2eiyfqTPcm8tJFdXXFXKNanolv60T_1u5lFMT6ZI0Je04bC8/pub?output=csv"
response = requests.get(url)
csv_data = StringIO(response.text)

# Leer CSV en UTF-8
df = pd.read_csv(csv_data, encoding='utf-8')

# --- 2️⃣ Unir todas las respuestas en una sola cadena ---
column_name = df.columns[5]  # columna F (índice 5)
text = " ".join(df[column_name].dropna())
text = text.replace("\xa0", " ").strip().upper()  # limpiar espacios invisibles y pasar a mayúsculas

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
    font_path="fonts/DejaVuSans-Bold.ttf",  # asegúrate de que la fuente esté en fonts/
    color_func=color_func,
    collocations=False  # ⚡ clave para que no se rompan palabras con acentos o ñ
).generate(text)

# --- 5️⃣ Guardar PNG ---
wc.to_file("wordcloud_profesional.png")

# --- 6️⃣ Mostrar (opcional) ---
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
