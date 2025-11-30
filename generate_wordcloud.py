import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random

# ===============================
# 1️⃣ Leer datos desde Google Sheets CSV
# ===============================
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTwDOPQYznFyg_EwMENdzeP44Ua8gCB2eiyfqTPcm8tJFdXXFXKNanolv60T_1u5lFMT6ZI0Je04bC8/pub?output=csv"
df = pd.read_csv(csv_url)

# ===============================
# 2️⃣ Obtener columna F
# ===============================
column_name = 'F'
if column_name not in df.columns:
    column_name = df.columns[5]  # fallback si cambia el nombre

# Texto en mayúsculas
text = " ".join(df[column_name].dropna().astype(str))
text = text.upper()

# ===============================
# 3️⃣ Stopwords
# ===============================
stopwords = set([
    "EL", "LA", "LOS", "LAS", "UN", "UNA", "UNO", "QUE", "DE", "Y", "EN", "CON",
    "POR", "PARA", "SE", "MI", "TU", "SU", "NOS", "ME", "TE", "LO", "AL", "DEL", "ETC"
])
text = " ".join([word for word in text.split() if word not in stopwords])

# ===============================
# 4️⃣ Colores eléctricos
# ===============================
color_list = ["#00FFFF", "#8A2BE2", "#FFFF00"]  # cian, morado, amarillo
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return random.choice(color_list)

# ===============================
# 5️⃣ Fuente Impact
# ===============================
font_path = "fonts/Impact.ttf"

# ===============================
# 6️⃣ Generar WordCloud
# ===============================
wc = WordCloud(
    width=1200,
    height=800,
    background_color="black",
    max_words=200,
    font_path=font_path,
    color_func=color_func
).generate(text)

# ===============================
# 7️⃣ Guardar imagen
# ===============================
wc.to_file("wordcloud_profesional.png")
