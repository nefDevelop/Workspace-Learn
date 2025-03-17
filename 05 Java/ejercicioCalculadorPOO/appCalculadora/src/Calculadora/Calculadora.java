package Calculadora;

public class Calculadora {
    private int numOperaciones;

    public Calculadora(){
        this.numOperaciones = 0;
    }

    public void setNumOperaciones(int num){
        this.numOperaciones = this.numOperaciones + num;
    }

    public int getNumOperaciones(){
        return this.numOperaciones;
    }

    public void operacion(int inum1, int inum2) {
        setNumOperaciones(1);
        System.out.println(inum1 * inum2);
    }

    public void operacion(int inum1, int inum2, String cadena) {
        System.out.println(cadena);
        
        if (cadena.equals("sumar")) {
            System.out.println(inum1 + inum2);
            System.out.println("Sumados");
            setNumOperaciones(1);
        }
        else if (cadena.equals("restar")){
            System.out.println(inum1 - inum2);
            System.out.println("Restados");
            setNumOperaciones(1);
        }
    }
}
