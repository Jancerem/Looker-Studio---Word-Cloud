import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from collections import Counter
import requests
from io import StringIO
from random import choice
import math

# --- 1️⃣ Descargar datos del Google Spreadsheet ---
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTwDOPQYznFyg_EwMENdzeP44Ua8gCB2eiyfqTPcm8tJFdXXFXKNanolv60T_1u5lFMT6ZI0Je04bC8/pub?output=csv"
response = requests.get(url)
csv_data = StringIO(response.text)

df = pd.read_csv(csv_data, encoding='utf-8')

# --- 2️⃣ Unir todas las respuestas en una sola cadena ---
column_name = df.columns[5]  # columna F
text = " ".join(df[column_name].dropna()).upper()  # convertir a mayúsculas

# --- 3️⃣ Contar frecuencia de palabras ---
words = text.split()
counter = Counter(words)

# --- 4️⃣ Configuración de imagen ---
width, height = 800, 600
background_color = "white"
img = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(img)

# --- 5️⃣ Fuente ---
font_path = "fonts/DejaVuSans-Bold.ttf"
max_font_size = 80
min_font_size = 20

# --- 6️⃣ Función para escoger color ---
def color_func():
    colores = ["#00FFFF", "#BF00FF", "#FFFF00"]  # cian, morado, amarillo eléctricos
    return choice(colores)

# --- 7️⃣ Ordenar palabras por frecuencia ---
sorted_words = counter.most_common(200)

# --- 8️⃣ Dibujar palabras ---
x, y = 10, 10
for word, freq in sorted_words:
    font_size = int(min_font_size + (freq / max(counter.values())) * (max_font_size - min_font_size))
    font = ImageFont.truetype(font_path, font_size)

    # Medir tamaño de palabra usando textbbox
    bbox = draw.textbbox((0,0), word, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    
    if x + w > width:
        x = 10
        y += h + 5
    if y + h > height:
        break

    draw.text((x, y), word, fill=color_func(), font=font)
    x += w + 5


# --- 9️⃣ Guardar imagen ---
img.save("wordcloud_profesional.png")
print("✅ Word Cloud generado con éxito.")
