package Animal;

import Animal.Animal.AnimalAction;

public class Perro extends Animal implements AnimalAction{
    private String raza;

    public Perro (String color, String  nombre, int edad){
        super(color, nombre, edad);

    }

    
    public void emitirSonido(){
        System.out.println("Guau!!");
    }

    public void comer(){
        System.out.println("Comer");
    }

    public String getRaza(){
        return this.raza;
    }



}

