import java.io.*;

public class App {
    public static void main(String[] args) throws Exception {
        // System.out.println("Hello, World!");
        
        File fichero = new File("sd/sd2","readme.md");
        // FileWriter escritor = new FileWriter(fichero);
                
        // try {
        //     escritor.write("# El Titulo \n### Subtitulo");
        //     escritor.flush();
        //     escritor.close();
        // } catch (IOException e) {
        //     System.out.println("Error guardando en el fichero.");
        //     // TODO: handle exception
        // } 

        FileReader reader = new FileReader(fichero);
        BufferedReader br = new BufferedReader(reader);
        String linea;

        try {
            while ((linea = br.readLine()) != null) {
                System.out.println(linea);

                linea = br.readLine();
            }
            br.close();
            reader.close();
        } catch (IOException e) {
            System.out.println("Error leyendo en el fichero.");
            // TODO: handle exception
        } 


    }

    // if n =1 es file si 2 es dir
    public static void creaDirectorio(File f, int n){
        try {
            switch (n) {
                case 1:
                    if (!f.createNewFile()){
                        throw new IOException("No se ha creado el directorio");
                    } else {
                        System.err.println("No se creo el archivo");
                    }
                    break;
                case 2:
                    if (!f.mkdirs()){
                        throw new IOException("No se ha creado el directorio");
                    } else {
                        System.err.println("No se creo el directorio");
                    }
                    break;

                default:
                    System.err.println("No declarado tipo de archivo");
                    break;
            }

        } catch (IOException e) {
            // TODO: handle exception
            System.err.println("Error");

        }
    }
}

