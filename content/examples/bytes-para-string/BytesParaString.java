import java.io.UnsupportedEncodingException;

public class BytesParaString {

    public static void main(String[] args) throws UnsupportedEncodingException{

        byte[] bytes = new byte[]{116, 101, 120, 116, 111, 32, 116, 101, 115, 116, 101};

        String texto = new String(bytes, "UTF-8");

        System.out.println(texto);

    }

}