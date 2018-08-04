import static org.junit.Assert.*;

import org.junit.Test;

public class ClasseDeTeste {

    @Test
    public void teste(){
        ClasseASerTestada obj = new ClasseASerTestada();
        String retornoDoMetodo = obj.metodoASerTestado();
        assertEquals("teste", retornoDoMetodo);
    }

}