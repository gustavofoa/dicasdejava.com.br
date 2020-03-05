---
title: '[Java] Como ler os bytes de um arquivo'
date: '2019-01-11'
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: Java 7, Arquivo, bytes
image: /images/logo-java.png
---

Quando você precisa ler os bytes de um arquivo em Java,
talvez venha à sua cabeça a criação de um `FileInputStream` e um objeto `byte[]`
para ler byte por byte do arquivo e adicioná-lo no array.

Funciona, mas a partir do **Java 7** é possível fazer isso de forma muito mais simples
através do método estático `readAllBytes` da classe `java.nio.file.Files`.

Para isso só precisamos do objeto `Path` do arquivo.
Se você já tiver o objeto `File` que representa o seu arquivo,
basta obter o objeto `Path` pelo método `toPath()`.

Confuso? Não tem segredo, veja o exemplo abaixo pra você entender melhor.

```java
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
```

[**VEJA TAMBÉM ~> [Java] Como converter um array de bytes em String**](https://dicasdejava.com.br/java-como-converter-um-array-de-bytes-em-string/){:target=\_blank}

Perceba que em uma apenas linha nós conseguimos ler os bytes do arquivo, sem precisar criar Streaming nenhum.

```java
byte[] bytes = Files.readAllBytes(file.toPath());
```

Para testar, eu criei um arquivo `arquivo.txt` com o conteúdo abaixo.

```
arquivo de teste para leitura no java.
```

Ao executar o nosso código java de exemplo, obtemos o seguinte resultado.

![Exemplo de leitura de bytes de um arquivo em java](/images/exemplo-ler-bytes-de-arquivo-java.gif){:style="width:100%; padding:10px;"}

Gostou? Alguma dúvida? Utilize a área de comentários aqui em baixo.

## Referências:

1. [Javadoc: java.nio.file.Files](https://docs.oracle.com/javase/7/docs/api/java/nio/file/Files.html){:target=\_blank}
2. [Javadoc: java.io.File](https://docs.oracle.com/javase/7/docs/api/java/io/File.html){:target=\_blank}