title: Java: Como limpar a tela do console
date: 2018-08-03
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: console, Scanner
image: /images/logo-java.png

Para limpar a tela do console nós utilizamos o comando `cls` no Windows e `clear` no Linux e no MacOS.

Para limpar a tela do console com Java nós temos que verificar qual o sistema operacional estamos utilizando e executar o respectivo comando.

No exemplo abaixo, nós escrevemos `Teste` no console, lemos um texto que o usuário digitar através da classe Scanner pra vermos o programa "parar".
E após o ENTER o programa limpa a tela. Veja o código:

[**>> Java: Como ler dados do Console com a classe Scanner**](https://dicasdejava.com.br/java-como-ler-dados-do-console-com-a-classe-scanner/){:target=\_blank}

```java
import java.io.IOException;
import java.util.Scanner;

public class LimpaConsole {
    public static void main(String[] args) throws IOException, InterruptedException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Teste");
        String texto = scanner.next();

        //Limpa a tela no windows, no linux e no MacOS
        if (System.getProperty("os.name").contains("Windows"))
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        else
            Runtime.getRuntime().exec("clear");

    }
}
```

## Resultado

Veja abaixo a execução deste programa no Windows.

![Limpando a tela do console com Java](/images/java-limpa-console.gif){:width=100%}
