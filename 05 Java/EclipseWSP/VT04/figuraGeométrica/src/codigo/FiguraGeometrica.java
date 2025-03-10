package codigo;

public class FiguraGeometrica {
    private String color;
    private double area;


    public FiguraGeometrica(String color, double area) {
        this.color = color;
        this.area = area;
    }


    public String getColor() {return color;}
    public void setColor(String color) {this.color = color;}
    public double getArea() {return area;}
    public void setArea(double area) {this.area = area;}

    public double calcularArea () {
        return 0;
    }

    public double calcularArea (double d) {
        return 0;
    }

    public double calcularArea (double d1, double d2) {
        return 0;
    }
}

