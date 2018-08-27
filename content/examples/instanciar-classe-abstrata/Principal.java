abstract class ClasseAbstrata {
    public abstract void metodoAbstrato();
}

public class Principal {
    public static void main(String args[]){

        ClasseAbstrata objeto = new ClasseAbstrata(){
            public void metodoAbstrato(){
                System.out.println("Olá mundo!");
            }
        }

        objeto.metodoAbstrato();

    }
}