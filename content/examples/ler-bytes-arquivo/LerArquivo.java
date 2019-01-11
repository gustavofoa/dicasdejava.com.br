import java.io.File;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.nio.file.Files;

public class LerArquivo {

    public static void main(String[] args) throws UnsupportedEncodingException, IOException{

        File file = new File("arquivo.txt");

        byte[] bytes = Files.readAllBytes(file.toPath());

        String textoDoArquivo = new String(bytes, "UTF-8");

        System.out.println(textoDoArquivo);

    }

}