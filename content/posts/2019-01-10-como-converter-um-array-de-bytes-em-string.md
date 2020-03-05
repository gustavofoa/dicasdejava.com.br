---
title: '[Java] Como converter um array de bytes em String'
date: '2019-01-10'
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: String, bytes
image: /images/logo-java.png
---

Você tem um array de bytes (`byte[]`) com você e precisa transformá-lo em texto?

Primeiro você precisa saber em qual _encoding_ esse array de bytes se encontra.
O mais comum é que seja **UTF-8**.

Neste caso a única coisa que você precisa fazer é criar um objeto
String passando o array de bytes e o encoding utilizado (UTF-8).
Veja o exemplo abaixo.

```java
import java.io.UnsupportedEncodingException;

public class BytesParaString {

    public static void main(String[] args) throws UnsupportedEncodingException{

        byte[] bytes = new byte[]{116, 101, 120, 116, 111, 32, 116, 101, 115, 116, 101};

        String texto = new String(bytes, "UTF-8");

        System.out.println(texto);

    }

}
```

Perceba que é necessário capturar a exception `UnsupportedEncodingException` quando chamamos este construtor da classe String.

O array de bytes `116, 101, 120, 116, 111, 32, 116, 101, 115, 116, 101` representa o texto `texto teste`.

Logo, ao executarmos este código obtemos a sequinte saída:

![Exemplo de conversão de bytes para string em java](/images/exemplo-bytes-para-string.gif){:style="width:100%; padding:10px;"}

Gostou? Alguma dúvida? Utilize a área de comentários aqui em baixo.

## Referências:

1. [Javadoc: java.lang.String](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html){:target=\_blank}
