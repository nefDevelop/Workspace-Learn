package figuras;

public class Triangulo extends Figuras {
	private double base;
	private double altura;
	
	public Triangulo(String color, double area, double base, double altura) {
		super(color, area);
		this.base = base;
		this.altura = altura;
	}
	
	
}
