// Comparaciones
// alert(3>1); //true

// asignacion de bool al comparar
// let num = 4 > 1; // true 4 mayor que 1

// Cadenas
// alert ('Z' > 'A'); //true
// alert ('Glow' > 'Glew'); //true
// alert ('Bee' > 'Be'); //true

// let year = prompt("En que año naciste? ");

// if (year == 2000) alert("Correcto");

// if 0 false 1 true
if (0) {
    console.log(true);
} else {
    console.log(false);
}

// operador ternario
let vAccessAllow;
let age = prompt("Que edad dirias que tengo?");

if (age > 41) {
    vAccessAllow = "Te pasaste";
} else {
    vAccessAllow = "Perfecto";
}

let vAccestTemp = (age > 41) ? "Te pasaste" : "Perfecto"; // operador ternario

alert("Edad: " + vAccessAllow);
alert("Edad: " + vAccestTemp);


// Ternario multiple
let edad = prompt("Edad?: ");

let mensajeEdad = (edad < 5) ? "Hola bebe" : 
                 (edad < 20) ? "Hola veintiañero" :
                 (edad < 50) ? "Hola" : "Hola viejo";

alert(mensajeEdad);