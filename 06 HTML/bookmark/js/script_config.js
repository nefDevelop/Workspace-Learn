async function cargarConfig() {
    try {
        const response = await fetch('./config.json'); // Carga el JSON
        if (!response.ok) throw new Error("Error al cargar el JSON");
        
        const data = await response.json(); // Convierte a objeto JS
        console.log(data); // Ver en consola

        // Mostrar los links en la página
        const linksList = document.getElementById("links");
        Object.entries(data.links).forEach(([nombre, url]) => {
            const li = document.createElement("li");
            li.innerHTML = `<a href="${url}" target="_blank">${nombre}</a>`;
            linksList.appendChild(li);
        });

        // Usar configuraciones
        document.body.style.background = data.settings.theme === "dark" ? "#222" : "#fff";
        document.body.style.color = data.settings.theme === "dark" ? "#fff" : "#000";

    } catch (error) {
        console.error("Error cargando JSON:", error);
    }
}

cargarConfig();
