import java.util.Scanner;
import Libro.Libro;

public class App {
    public static void main(String[] args) throws Exception {

        Libro jura = new Libro("1", "Sanderson", "Juramentada", "Nova", 2021, 1304);
        Libro caminReyes = new Libro("2", "Sanderonn", "Judramentada", "Nova", 2021, 1304);
        
        Scanner read = new Scanner(System.in);

        String isbn, autor, titulo, editorial;
        int anyoPublicacion, pages;

        System.out.println("Isbn: ");
        isbn = read.nextLine();
        autor = read.nextLine();
        titulo = read.nextLine();
        editorial = read.nextLine();
        anyoPublicacion = Integer.parseInt(read.nextLine());
        pages = Integer.parseInt(read.nextLine());

        Libro third = new Libro(isbn, autor, titulo, editorial, anyoPublicacion, pages);

        jura.showLibro();
        caminReyes.showLibro();
        third.showLibro();

        read.close();
    }
}
