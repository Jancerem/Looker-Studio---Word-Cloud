import pandas as pd
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

# ===============================
# 1️⃣ Leer datos desde Google Sheets CSV
# ===============================
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTwDOPQYznFyg_EwMENdzeP44Ua8gCB2eiyfqTPcm8tJFdXXFXKNanolv60T_1u5lFMT6ZI0Je04bC8/pub?output=csv"

df = pd.read_csv(csv_url)

# ===============================
# 2️⃣ Obtener columna de preguntas
# ===============================
# Cambia la letra de la columna si es diferente
column_name = 'F'
if column_name not in df.columns:
    # A veces el CSV de Google Sheets cambia el nombre, usamos la 6ta columna
    column_name = df.columns[5]

# Combinar todo el texto y pasar a mayúsculas
text = " ".join(df[column_name].dropna().astype(str))
text = text.upper()

# ===============================
# 3️⃣ Eliminar palabras comunes
# ===============================
stopwords = set([
    "EL", "LA", "LOS", "LAS", "UN", "UNA", "UNO", "QUE", "DE", "Y", "EN", "CON",
    "POR", "PARA", "SE", "MI", "TU", "SU", "NOS", "ME", "TE", "LO", "AL", "DEL", "ETC"
])

text = " ".join([word for word in text.split() if word not in stopwords])

# ===============================
# 4️⃣ Configurar colores y fuente
# ===============================
# Colores eléctricos: cian, morado y amarillo
color_list = ["#00FFFF", "#8A2BE2", "#FFFF00"]  # cian, morado, amarillo

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    import random
    return random.choice(color_list)

# Fuente que soporte acentos y ñ
font_path = "fonts/Impact.ttf"  # Debes tener esta fuente en tu repo en carpeta 'fonts'

# ===============================
# 5️⃣ Generar WordCloud
# ===============================
wc = WordCloud(
    width=1200,
    height=800,
    background_color="black",
    max_words=200,
    colormap=None,
    color_func=color_func,
    font_path=font_path
).generate(text)

# ===============================
# 6️⃣ Guardar imagen
# ===============================
wc.to_file("wordcloud_profesional.png")

# ===============================
# 7️⃣ Mostrar en pantalla (opcional)
# ===============================
plt.figure(figsize=(15,10))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
