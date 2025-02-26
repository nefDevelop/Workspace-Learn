package vt03;

public class Persona {
    private String nombre;
    private String apellidos1;
    private String apellidos2;
    private char sexo;
    private int edad;
    private String direccion;

    public Persona (String nombre, String apellidos1, String apellidos2, char sexo, int edad, String direccion){ 
        this.nombre = nombre;
        this.apellidos1 = apellidos1;
        this.apellidos2 = apellidos2;
        this.sexo = sexo;
        this.edad = edad;
        this.direccion = direccion;
    }

    public String getNombre(){ return this.nombre; }
    public void setNombre(String n){ this.nombre = n; }

    public void mostrarDatos(){
        System.out.println("Nombre: " + this.nombre);
        System.out.println("Apellidos: " + this.apellidos1 +" "+this.apellidos2); 
        System.out.println("Sexo: " + this.sexo); 
        System.out.println("Edad: " + this.edad); 
        System.out.println("Direccion: " + this.direccion); 

    }

    public void mayorEdad (   ){
        if (this.edad >= 18) {
            System.out.println("Es mayor de edad.");
        } else {
            System.err.println("NO es mayor de edad.");
        }
    }


}   
