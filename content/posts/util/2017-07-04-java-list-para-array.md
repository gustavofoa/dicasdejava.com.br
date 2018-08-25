title: Java: Como converter List para Array
date: 2017-07-04
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: Array, List, Arrays
image: /images/logo-java.png

Para converter um List (`java.util.List`) em um Array (Vetor),
nós podemos utilizar o método toArray da interface `List`
que pertence à API nativa do Java.

Veja no exemplo abaixo como converter um List em um Array em Java.

```java
package br.com.dicasdejava.util;

import java.util.ArrayList;
import java.util.List;

public class ListParaArray {

    public static void main(String[] args) {
    	List<String> listaDeNomes = new ArrayList<String>();
    	listaDeNomes.add("Gustavo");
    	listaDeNomes.add("Maria");
    	listaDeNomes.add("José");
    	listaDeNomes.add("João");
    	listaDeNomes.add("Ana");

    	String[] arrayDeNomes = listaDeNomes.toArray(new String[0]);

    	System.out.println(listaDeNomes);
    }
}
```

Saída:

```
[Gustavo, Maria, José, João, Ana]
```

## Referências:

1. [JavaDoc: List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html){:target=\_blank}
