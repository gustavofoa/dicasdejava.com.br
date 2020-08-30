public class Pilha {
    
    public static void main(String b[]) {

        System.out.println("main1");
        metodo1();
        System.out.println("main2");


    }

    public static void metodo1(){
        System.out.println("metodo1 - 1");
        metodo2();
        System.out.println("metodo1 - 2");
    }

    public static void metodo2(){
        System.out.println("metodo2");
        metodo3();
    }

    public static void metodo3(){
        String a  = null;
        System.out.println(a.toString());
    }

}