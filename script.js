const API_URL = "https://script.google.com/macros/s/AKfycbzI8snWaaHrKAgFf817Rp2_WZEd0W0BYdZuQqx1teqBBb8CZ4mQN2UStWIWJVoIVyCM/exec";

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

