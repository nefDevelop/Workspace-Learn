package Animal;

import Animal.Animal.AnimalAction;


public class Gato extends Animal implements AnimalAction{

    public Gato (String color, String  nombre, int edad){
        super(color, nombre, edad);

    }

    public void emitirSonido(){
        System.out.println("Miau!!");
    }

    public void comer(){
        System.out.println("Comiendo Pescado");
    }
}