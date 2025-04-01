import Animal.Perro;
import Animal.Gato;


public class App {
    public static void main(String[] args) throws Exception {
        // Animal onlyAnimal = new Animal("Verder", "Cala", 23);
        Perro perrito = new Perro("Azul", "Perro", 2);
        Gato gato = new Gato("Blanco", "Jimm", 4);

        // onlyAnimal.comer();
        // onlyAnimal.dormir();
        // onlyAnimal.emitirSonido();
        System.out.println("Hello, World!");

        perrito.comer();
        perrito.dormir();
        perrito.emitirSonido();
        System.out.println("Hello, World!");

        gato.comer();
        gato.dormir();
        gato.emitirSonido();
        System.out.println("Hello, World!");

    }
}
