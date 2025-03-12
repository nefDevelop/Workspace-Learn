import java.util.Scanner;
import Libro.Libro;

public class App {
    public static void main(String[] args) throws Exception {

        Libro jura = new Libro("1", "Sanderson", "Juramentada", "Nova", 2021, 1304);
        Libro caminReyes = new Libro("2", "Sanderonn", "Judramentada", "Nova", 2021, 1304);
        Scanner read = new Scanner();

        System.out.println("Isbn: ");
        read.nextLine()

        jura.showLibro();
        caminReyes.showLibro();


    }
}
