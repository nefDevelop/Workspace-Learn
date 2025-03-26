// En esta PAC de Desarrollo tendrás que ser capaz de hacer funcionar el programa java que se adjunta. Se trata de un creador de personajes de 
// rol, que cuenta con una clase base llamada Personaje y una clase derivada llamada Heroe. 
// Además, hay una clase Main con el método main para ejecutar el programa.
// Los tres ficheros (Personaje.java, Heroe.java y Main.java) se encuentran en las Preguntas 2, 3 y 4 respectivamente, 
// PERO tienen huecos en el código que debes que completar para hacer funcionar el programa.
// ADVERTENCIA: Cada hueco corresponde a una sola palabra. Ten cuidado con las mayúsculas y minúsculas, 
// con los signos de puntuación y ten en cuenta que debes completar el hueco únicamente con la palabra que se necesite. 
// No se atenderán reclamaciones a palabras "parecidas", la palabra debe ser exacta y precisamente la que se necesite para que el 
// programa funcione.


//     La PAC de Desarrollo consta de 4 apartados o preguntas:
//     Pregunta 1. Captura de pantalla de la ejecución. Aquí hay que insertar una captura de pantalla con la ejecución válida del programa. 
//     Como podrás observar, al ejecutar el programa, solicita tres datos, nuestro nombre, nuestros apellidos y nuestra raza, que puede ser Humano, 
//     Elfo u Orco. Introduce tu nombre y apellidos reales, y selecciona una raza a tu gusto, pero para superar la PAC de Desarrollo 
//     es IMPRESCINDIBLE que introduzcas tu nombre y apellidos reales.

//     Pregunta 2. Huecos de Personaje.java. Aquí tendrás que rellenar los 13 huecos de la clase Personaje.java.
//     Pregunta 3. Huecos de Heroe.java. Aquí tendrás que rellenar los 6 huecos de la clase Heroe.java.
//     Pregunta 4. Huecos de Main.java. Aquí tendrás que rellenar los 9 huecos de la clase Main.java.


//     Escribe en cada hueco la palabra de código que falta, pero presta mucha atención a los detalles porque 
//     NO SE ATENDERÁN revisiones por incurrir en un error al escribir el código que falta (cuidado con los paréntesis, 
//     con el resto de símbolos, con los nombres de las funciones, con las mayúsculas y minúsculas, etc.). Por pequeño que sea el 
//     error, si no se escribe correctamente, el programa NO funcionará.



package codigo;

import java.util.Scanner;


public class Main { 
    public static void main(String args[]) { 
        Scanner scanner = new Scanner(System.in);
        System.out.print("Introduzca el nombre: ");
        String nombre = scanner.nextLine();
        System.out.print("Introduzca los apellidos: ");
        String apellidos = scanner.nextLine();
        System.out.print("Introduzca su raza (Humano, Elfo, Orco): ");
        String raza = scanner.nextLine();

        Heroe heroe = new Heroe(nombre, apellidos, raza);
        heroe.mostrarInfo();
        scanner.close();
    }
}
