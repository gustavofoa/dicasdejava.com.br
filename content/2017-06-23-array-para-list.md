title: Como converter Array para List em Java
date: 2017-06-23
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: Array, List, Arrays
image: /images/logo-java.png

Para converter um Array (Vetor) em um List, nós podemos utilizar a classe java.util.Arrays
que é nativa da API java.

Veja no exemplo abaixo como converter um Array em um List.

```java
package br.com.dicasdejava;

import java.util.Arrays;
import java.util.List;

public class ArrayParaList {

	public static void main(String[] args) {
		String[] nomes = new String[]{"Gustavo", "Maria", "José", "João", "Ana"};

		List listaDeNomes = Arrays.asList(nomes);

		System.out.println(listaDeNomes);
	}
}
```

Saída:

```
[Gustavo, Maria, José, João, Ana]
```

Referências:

1. [JavaDoc: Arrays](https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html)
