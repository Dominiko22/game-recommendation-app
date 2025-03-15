document.getElementById("recommendationForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const genre = document.getElementById("genre").value || "";
    const platform = document.getElementById("platform").value || "";

    try {
        const response = await fetch(`http://127.0.0.1:5000/recommend?genre=${genre}&platform=${platform}`);
        if (!response.ok) throw new Error("Błąd w żądaniu do backendu");
        const data = await response.json();

        const resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = ""; // Wyczyść poprzednie wyniki

        if (data.error) {
            resultsDiv.innerHTML = `<p style="color: red;">${data.error}</p>`;
        } else {
            data.forEach(game => {
                const gameDiv = document.createElement("div");
                gameDiv.style.marginBottom = "20px";
                gameDiv.innerHTML = `
                    <img src="${game.image}" alt="${game.name}">
                    <h3>${game.name}</h3>
                    <p><strong>Platformy:</strong> ${game.platforms.join(", ")}</p>
                    <p><strong>Gatunki:</strong> ${game.genres.join(", ")}</p>
                `;
                resultsDiv.appendChild(gameDiv);
            });
        }
    } catch (error) {
        console.error("Błąd w komunikacji z backendem:", error);
        const resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = `<p style="color: red;">Nie udało się pobrać rekomendacji.</p>`;
    }
});
