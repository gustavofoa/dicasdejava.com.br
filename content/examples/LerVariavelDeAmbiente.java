public class LerVariavelDeAmbiente {
    public static void main(String[] args) {
        
        String variavelDeAmbiente = System.getenv("JAVA_HOME");

        System.out.println(variavelDeAmbiente);

    }
}