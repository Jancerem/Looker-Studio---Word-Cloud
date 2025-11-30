const API_URL = "https://script.google.com/macros/s/AKfycbx2Nq4wCkQPodRS_oGEjvUgSYeMBKGjA11O0neKK4PSLJb06M2kE0DCwFmvqRX871K_/exec";

google.visualization.events.addListener(google, 'ready', () => {
    fetch(API_URL)
        .then(response => response.json())
        .then(data => {
            const list = data.map(w => [w.text, w.value]);

            WordCloud(document.getElementById("cloud"), {
                list,
                gridSize: 12,
                weightFactor: size => size * 5,
                color: "random-dark",
                backgroundColor: "#ffffff",
                rotateRatio: 0.1
            });
        });
});

