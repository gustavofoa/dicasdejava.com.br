import java.io.File;

public class FileSeparator {
    public static void main(String []a){

        String caminhoDoArquivo = "Usuario" + File.separator + "gustavo" + File.separator + "arquivo.txt";

        System.out.println(caminhoDoArquivo);

    }
}