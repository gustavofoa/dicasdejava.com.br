import java.util.Scanner;

public class Temperatura {
    public static void main(String[] a) {

        Scanner sc = new Scanner(System.in);
        double temperaturaOrigem;
        int unidadeOrigem;
        
        temperaturaOrigem = 0;
        unidadeOrigem = 0;

        System.out.print("Informe a temperatura: ");
        temperaturaOrigem = sc.nextDouble();
        System.out.println("1 - ºC (Grau Celsius)");
        System.out.println("2 - ºF (Grau Fahrenheit)");
        System.out.println("3 -  K (Kelvin)");
        System.out.print("Informe a unidade da temperatura (1, 2 ou 3): ");
        unidadeOrigem = sc.nextInt();
    
        switch (unidadeOrigem)
        {
            case 1:
                System.out.println("Temperatura em ºF: " + ( (temperaturaOrigem * 9/5) + 32) );
                System.out.println("Temperatura em K: " + ( temperaturaOrigem + 273.15) );
                break;
            case 2:
                System.out.println("Temperatura em ºC: " + ( (temperaturaOrigem - 32) * 5/9) );
                System.out.println("Temperatura em K: " + ( (temperaturaOrigem - 32) * 5/9 + 273.15 ) );
                break;
            case 3:
                System.out.println("Temperatura em ºC: " + ( temperaturaOrigem - 273.15) );
                System.out.println("Temperatura em ºF: " + ( (temperaturaOrigem - 273.15) * 9/5 + 32) );
                break;
        }
    }
}