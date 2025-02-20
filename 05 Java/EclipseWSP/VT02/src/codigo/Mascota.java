package codigo;

public class Mascota {
	String nombre;
	int edad;
	String color;
	
	public Mascota(String nombre, int edad, String color) {
		this.nombre = nombre;
		this.edad = edad;
		this.color = color;	
	}
	
	public void Saludar() {
		System.out.println("Hola, me llamo "+this.nombre);
	}
}
