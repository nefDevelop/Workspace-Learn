package Libro;

public class Libro {
    private String isbn;
    private String autor;
    private String titulo;
    private String editorial;
    private int anyoPublicacion;
    private int numPaginas;

    public Libro(String isbn, String autor, String titulo, String editorial, int anyoPublicacion, int numPaginas){
        this.isbn = isbn;
        this.autor = autor;
        this.titulo = titulo;
        this.editorial = editorial;
        this.anyoPublicacion = anyoPublicacion;
        this.numPaginas = numPaginas;
    }

    public void showLibro (){
        System.out.println(this.isbn);
        System.out.println(this.autor);
        System.out.println(this.titulo);
        System.out.println(this.editorial);
        System.out.println(this.anyoPublicacion);
        System.out.println(this.numPaginas);
    }
}
