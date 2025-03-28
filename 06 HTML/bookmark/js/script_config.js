async function cargarConfig() {
    try {
        const response = await fetch('js/config.json'); // Cargar JSON
        if (!response.ok) throw new Error(`Error al cargar JSON: ${response.status}`);

        const data = await response.json(); // Convertir a objeto JS
        console.log(data); // Ver en consola

        // Obtener el contenedor donde se mostrarán los links
        const linksContainer = document.getElementById("mainlinks");
        linksContainer.innerHTML = ""; // Limpiar contenido anterior

        Object.entries(data.links).forEach(([categoria, datos]) => {
            const columna = document.createElement("div");
            columna.classList.add("column"); // Crear columna

            const categoriaElemento = document.createElement("h3");
            categoriaElemento.textContent = categoria;
            categoriaElemento.style.color = `var(${datos.color})`;
            columna.appendChild(categoriaElemento); // Agregar título dentro de la columna

            Object.entries(datos.items).forEach(([nombre, info]) => {
                const linkContainer = document.createElement("div");
                linkContainer.classList.add("link-item");

                const link = document.createElement("a");
                link.href = info.url;
                link.target = "_blank";
                link.classList.add("link");

                // Crear icono
                if (info.icon) {
                    const icono = document.createElement("i");
                    icono.className = info.icon;
                    link.appendChild(icono);
                }

                // Contenedor de texto
                const textContainer = document.createElement("div");
                textContainer.classList.add("text-container");

                // Agregar título
                const title = document.createElement("span");
                title.textContent = nombre;
                title.classList.add("title");
                textContainer.appendChild(title);

                // Agregar descripción debajo (opcional)
                if (info.description) {
                    const description = document.createElement("span");
                    description.textContent = info.description;
                    description.classList.add("description");
                    textContainer.appendChild(description);
                }

                link.appendChild(textContainer);
                linkContainer.appendChild(link);
                columna.appendChild(linkContainer);
            });

            linksContainer.appendChild(columna); // Agregar columna al contenedor principal
        });

    } catch (error) {
        console.error("Error cargando JSON:", error);
    }
}

async function showName() {
    try {
        const response = await fetch('js/config.json'); // Cargar JSON
        if (!response.ok) throw new Error(`Error al cargar JSON: ${response.status}`);
        
        const data = await response.json(); // Convertir a objeto JS
        console.log(data); // Ver en consola
        
        const targetElement = document.getElementById("divName"); 
        targetElement.textContent = data.settings.name;  // Agregar título dentro de la columna

    } catch (error) {
        console.error("Error cargando JSON:", error);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const dropdownLinks = document.querySelectorAll(".dropdown-content a");
    const themeImage = document.getElementById("theme-image"); // Seleccionamos la imagen

    // Obtener el tema guardado o por defecto "auto"
    const savedTheme = localStorage.getItem("theme") || "auto";
    setTheme(savedTheme);

    // Manejar la selección del tema al hacer clic en los enlaces
    dropdownLinks.forEach(link => {
        link.addEventListener("click", function () {
            const selectedTheme = link.dataset.theme;
            setTheme(selectedTheme);
            localStorage.setItem("theme", selectedTheme);
        });
    });

    function setTheme(baseTheme) {
        let finalTheme = baseTheme;

        if (baseTheme !== "auto") {
            // Si el usuario eligió un tema, decidir si se usa la versión clara u oscura
            const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
            finalTheme = prefersDark ? `${baseTheme}-dark` : `${baseTheme}-light`;
        }

        // Establecer el atributo 'data-theme' en el documento
        document.documentElement.setAttribute("data-theme", finalTheme);

        // Cambiar la imagen según el tema
        updateThemeImage(finalTheme);
    }

    function updateThemeImage(finalTheme) {
        const themeName = finalTheme.split('-')[0]; // Obtener el nombre del tema (sin "dark" o "light")

        // Cambiar la imagen según el tema y modo
        if (finalTheme.includes("dark")) {
            themeImage.src = `img/${themeName}-dark.png`;  // Imagen para el tema oscuro
        } else {
            themeImage.src = `img/${themeName}-light.png`;  // Imagen para el tema claro
        }
    }
});


// Miramos si se pulsa \ para activar la busqueda
document.addEventListener("keydown", function (event) {
    const searchBar = document.getElementById("searchBar");

    if (event.key === "\\" && document.activeElement !== searchBar) {
        event.preventDefault(); // Evita que se escriba "/" en otro campo de texto
        searchBar.style.display = "block"; // Muestra la barra de búsqueda
        searchBar.focus(); // Enfoca la barra de búsqueda
    } else if (event.key === "Escape") {
        searchBar.style.display = "none"; // Oculta la barra con Escape
        searchBar.value = ""; // Borra el texto al ocultar
    }
});

// TODO:: Filtrar por buscador o motor. Se configura en json
document.getElementById("searchBar").addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        const query = event.target.value.trim();
        if (query) {
            window.open(`https://www.google.com/search?q=${encodeURIComponent(query)}`, "_blank");
            event.target.value = ""; // Limpia la barra
            event.target.style.display = "none"; // Oculta la barra
        }
    }
});


document.addEventListener("DOMContentLoaded", showName);
document.addEventListener("DOMContentLoaded", cargarConfig);