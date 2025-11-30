document.addEventListener("DOMContentLoaded", async () => {
  const API_URL = "https://script.google.com/macros/s/AKfycbx2Nq4wCkQPodRS_oGEjvUgSYeMBKGjA11O0neKK4PSLJb06M2kE0DCwFmvqRX871K_/exec";

  try {
    const response = await fetch(API_URL);
    const data = await response.json();

    // Convertir JSON a formato WordCloud2.js: [texto, tamaño]
    const words = data.map(item => [item.text, item.size]);

    WordCloud(document.getElementById("wordcloud"), {
      list: words,
      gridSize: 8,
      weightFactor: 5,
      fontFamily: "Impact",
      rotateRatio: 0.4,
      rotationSteps: 2,
      backgroundColor: "#ffffff",
      color: () => `hsl(${Math.random() * 360}, 70%, 50%)`
    });

  } catch (error) {
    console.error("Error cargando datos del Word Cloud:", error);
  }
});
