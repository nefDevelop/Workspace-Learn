package codigo;

public class Perro extends Mascota{
	String raza;
	
	public Perro(String nombre, int edad, String color, String raza) {
		super (nombre, edad, color);
		this.raza = raza;
	}

	@Override
	public void Saludar() {
		System.out.println("Hola, me llamo "+this.nombre+ "y soy "+this.raza);
	}
}
