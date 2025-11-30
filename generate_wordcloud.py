from wordcloud import WordCloud
import matplotlib.pyplot as plt

# --- Texto de prueba con acentos y ñ ---
texto = "ENSEÑANZA, NIÑOS, CORAZÓN, EDUCACIÓN, MÚSICA, CAMIÓN, LECCIÓN"

# --- Función de colores ---
from random import choice
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colores = ["#00FFFF", "#BF00FF", "#FFFF00"]  # cian, morado, amarillo eléctricos
    return choice(colores)

# --- Crear WordCloud ---
wc = WordCloud(
    width=800,
    height=600,
    background_color="white",
    max_words=50,
    font_path="fonts/DejaVuSans-Bold.ttf",  # fuente compatible con acentos y ñ
    color_func=color_func,
    collocations=False  # evita separar mal palabras
).generate(texto)

# --- Mostrar ---
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
