import javax.swing.JOptionPane;

public class HelloWorld {

    public static void main(String[] banana)
    {
        
        int voto, votos1, votos2, eleitor;

        voto = 0;
        votos1 = 0;
        votos2 = 0;
        eleitor = 0;
        
        for (eleitor=0 ; eleitor <= 6 ; eleitor++ ) {
            
            voto = Integer.parseInt(JOptionPane.showInputDialog("Informe o voto: "));

            if (voto == 1) {
                votos1++;
            } else {
                votos2++;
            }
        };


        if (votos1 > votos2) {
            JOptionPane.showMessageDialog(null, "O candidato 1 ganhou a eleição.");
        } else if (votos1 < votos2) {
            JOptionPane.showMessageDialog(null, "O candidato 2 ganhou a eleição.");
        } else {
            JOptionPane.showMessageDialog(null, "A eleição terminou empatada.");
        }


    }

}
