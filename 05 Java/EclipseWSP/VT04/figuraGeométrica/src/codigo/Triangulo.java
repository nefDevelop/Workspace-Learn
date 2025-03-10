package codigo;

public class Triangulo extends FiguraGeometrica{
    private double base;
    private double altura;

    public Triangulo(String color, double area, double base, double altura) {
        super(color, area);
        this.base = base;
        this.altura = altura;
    }

    public double getBase() {return base;}
    public void setBase(double base) {this.base = base;}
    public double getAltura() {return altura;}
    public void setAltura(double altura) {this.altura = altura;}
    
    public double calcularArea() {
        
        this.setArea((this.base * this.altura) / 2);
        return (this.getArea());
    }
}
