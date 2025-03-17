import Calculadora.Calculadora;
import java.util.Scanner;


public class App {
    public static void main(String[] args) throws Exception {
        
        
        Scanner scanner = new Scanner(System.in);
        Calculadora calc = new Calculadora();
        String op = "";
        int num1, num2;
        int exit = 0;

        while (exit == 0) {
            System.out.println("Primer operando?");
            num1 = scanner.nextInt();


            System.out.println("Segundo operando?");
            num2 = scanner.nextInt();

            System.out.println("restar sumar exit");
            op = scanner.next();

            System.out.println(op);

        
            if (op.equals("restar") || op.equals("sumar"))   {
                calc.operacion(num1, num2, op);
            } 
            else if (op.equals("exit")){
                exit = 1;
            }
            else{
                calc.operacion(num1, num2);
            }

            System.out.println(calc.getNumOperaciones());
            
        }
        scanner.close();
    }
}
