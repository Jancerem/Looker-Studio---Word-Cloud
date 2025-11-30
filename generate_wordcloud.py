import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests
from io import StringIO

# --- 1️⃣ Obtener datos del Google Spreadsheet ---
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTwDOPQYznFyg_EwMENdzeP44Ua8gCB2eiyfqTPcm8tJFdXXFXKNanolv60T_1u5lFMT6ZI0Je04bC8/pub?output=csv"
response = requests.get(url)
csv_data = StringIO(response.text)

df = pd.read_csv(csv_data)

# --- 2️⃣ Unir todas las respuestas en una sola cadena ---
# Aquí asumimos que tu columna es la F
column_name = df.columns[5]  # columna F (índice 5)
text = " ".join(df[column_name].dropna()).upper()  # todo en mayúsculas

# --- 3️⃣ Función para colores personalizados ---
from random import choice

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colores = ["#00FFFF", "#BF00FF", "#FFFF00"]  # cian, morado y amarillo eléctricos
    return choice(colores)

# --- 4️⃣ Crear WordCloud ---
wc = WordCloud(
    width=800,
    height=600,
    background_color="white",
    max_words=200,
    font_path="fonts/Impact.ttf",  # Asegúrate que Impact.ttf esté en fonts/
    color_func=color_func
).generate(text)

# --- 5️⃣ Guardar PNG ---
wc.to_file("wordcloud_profesional.png")

# --- 6️⃣ Mostrar (opcional en Colab local) ---
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
