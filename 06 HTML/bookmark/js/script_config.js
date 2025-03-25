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
                link.textContent = nombre;
                link.target = "_blank";

                // // Agregar tooltip con la descripción
                // if (info.description) {
                //     link.title = info.description;
                // }

                // Agregar icono si está definido
                if (info.icon) {
                    const icono = document.createElement("i");
                    icono.className = info.icon;
                    // icono.style.fontSize = "1.5rem"; // Corregido el tamaño
                    // icono.style.marginRight = "1.2rem"; // Espacio entre icono y texto
                    link.prepend(icono);
                }

                linkContainer.appendChild(link);

                // Agregar la descripción debajo del enlace (opcional)
                if (info.description) {
                    const description = document.createElement("span");
                    description.textContent = info.description;
                    description.classList.add("link-description");
                    linkContainer.appendChild(description);
                }

                columna.appendChild(linkContainer); // Agregar enlace dentro de la columna
            });

            linksContainer.appendChild(columna); // Agregar columna al contenedor principal
        });

        // Aplicar configuraciones globales
        document.body.style.background = data.settings.theme === "dark" ? "#222" : "#fff";
        document.body.style.color = data.settings.theme === "dark" ? "#fff" : "#000";

    } catch (error) {
        console.error("Error cargando JSON:", error);
    }
}



document.addEventListener("DOMContentLoaded", cargarConfig);


//document.getElementById("main").innerHTML = Date();
function updateClock() {
    var days = ['SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY'];
    var m = new Date();
    var dateString =
        (days[ m.getDay() ]) + " " +
        ("0" + m.getDate()).slice(-2) + "/" +
        ("0" + (m.getMonth()+1)).slice(-2) +"/"+
        m.getFullYear() +" "+
        ("0" + m.getHours()).slice(-2) + ":" +
        ("0" + m.getMinutes()).slice(-2) + ":" +
        ("0" + m.getSeconds()).slice(-2);
    
    // set the content of the element with the ID time to the formatted string
    document.getElementById('time').innerHTML = dateString;

    // call this function again in 1000ms
    setTimeout(updateClock, 1000);
}

document.addEventListener("DOMContentLoaded", updateClock);


async function showName() {
    const response = await fetch('config.json'); // Cargar JSON
    if (!response.ok) throw new Error(`Error al cargar JSON: ${response.status}`);

    const data = await response.json(); // Convertir a objeto JS
    // console.log(data); // Ver en consola

    const targetElement = document.getElementById("divName"); 

    targetElement.textContent = data.settings.name;  // Agregar título dentro de la columna

}

document.addEventListener("DOMContentLoaded", showName);
