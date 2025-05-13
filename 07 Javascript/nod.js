// Probando con node
let hola = "hola";
let i = 0;

// Bucles
//  while
while (i < 5) {
    console.log(i);
    i++;
}

//  En una linea
i = 4;
while (i) console.log(i--);

//  do - while
i = 0;
do {
    console.log("do-while: " + i);
    i++;
} while (i < 4);

//  for
for (i = 0; i < 3; i++) {
    console.log("for: " + i);

}

//      Se pueden omitir partes del for este seria como un while
//      - se pueden omitir todos, bucle infinito
i = 0;
for (; i < 5;) {
    console.log('for omitted: ' + i
    );
    i++;
}


//  break (saliendo del bucle)
let sum = 0;

while (true) {
    if (!sum == 0) break;
}


//  Continue

