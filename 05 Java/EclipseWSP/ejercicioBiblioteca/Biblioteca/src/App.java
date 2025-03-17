import java.util.Scanner;
import Libro.Libro;

public class App {
    public static void main(String[] args) throws Exception {
        //Declaramos variables a usar
        String isbn, autor, titulo, editorial;
        int anyoPublicacion, pages;

        // Dos creados directamente desde el constructor
        Libro jura = new Libro("1", "Sanderson", "Juramentada", "Nova", 2021, 1304);
        Libro caminReyes = new Libro("2", "Sanderonn", "Judramentada", "Nova", 2021, 1304);
        
        //Abrimos para solicitar informacion al usuario
        Scanner read = new Scanner(System.in);

        //Solicitamos la informacion
        System.out.println("Isbn: ");
        isbn = read.nextLine();

        System.out.println("Autor: ");
        autor = read.nextLine();

        System.out.println("Titulo: ");
        titulo = read.nextLine();

        System.out.println("Editorial: ");
        editorial = read.nextLine();

        System.out.println("Año: ");
        anyoPublicacion = Integer.parseInt(read.nextLine());

        System.out.println("Paginas: ");
        pages = Integer.parseInt(read.nextLine());

        //Creamos el tercer objeto con la informacion del usuario.
        Libro third = new Libro(isbn, autor, titulo, editorial, anyoPublicacion, pages);

        //Mostramos la informacion guardada
        jura.showLibro();
        caminReyes.showLibro();
        third.showLibro();

        //Cerramos el scanner.
        read.close();
    }
}
