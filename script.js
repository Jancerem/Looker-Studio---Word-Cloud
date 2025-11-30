// Visualización para Looker Studio usando ECharts wordcloud
// Espera: dscc.subscribeToData está disponible por la librería dscc incluida en index.html

// función que recibe los datos y dibuja la nube
function updateViz(dataObject) {
  try {
    const data = dataObject.tables.DEFAULT; // array de filas
    // crear array de {name, value}
    const words = data.map(r => {
      // r.c[0] es la dimensión word, r.c[1] la métrica count
      const word = r.c[0] && r.c[0].v ? r.c[0].v : "";
      const count = r.c[1] && r.c[1].v ? r.c[1].v : 0;
      return { name: String(word), value: Number(count) };
    }).filter(w => w.name);

    // inicializar chart (si ya existe, reusar)
    const container = document.getElementById('chart');
    container.innerHTML = "";
    const chart = echarts.init(container);

    const option = {
      backgroundColor: "#ffffff",
      tooltip: { show: true },
      series: [{
        type: "wordCloud",
        shape: "circle",
        left: "center",
        top: "center",
        width: "100%",
        height: "100%",
        sizeRange: [14, 60],
        rotationRange: [-45, 45],
        rotationStep: 45,
        gridSize: 6,
        drawOutOfBound: false,
        textStyle: {
          // color aleatorio dentro de una paleta
          color: function () {
            const colors = ["#FFCE00","#1C2E4A","#000000","#FF6B6B","#4ECDC4","#556270"];
            return colors[Math.floor(Math.random() * colors.length)];
          }
        },
        data: words
      }]
    };

    chart.setOption(option);
    window.onresize = function() { chart.resize(); };
  } catch (e) {
    console.error("Error updateViz:", e);
  }
}

// Suscribirse a datos de Looker Studio
if (typeof dscc !== "undefined" && dscc.subscribeToData) {
  dscc.subscribeToData(function(data) {
    updateViz(data);
  });
} else {
  // En pruebas locales, podrías generar datos dummy:
  console.log("dscc no definido (prueba local).");
}
