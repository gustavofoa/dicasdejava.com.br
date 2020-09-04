import java.io.File;

public class FilePathSeparator {
    public static void main(String []a){

        String caminhoDoArquivo1 = "Usuario" + File.separator + "gustavo" + File.separator + "arquivo1.txt";
        String caminhoDoArquivo2 = "Usuario" + File.separator + "gustavo" + File.separator + "arquivo2.txt";

        System.out.println(caminhoDoArquivo1 + File.pathSeparator + caminhoDoArquivo2);

    }
}