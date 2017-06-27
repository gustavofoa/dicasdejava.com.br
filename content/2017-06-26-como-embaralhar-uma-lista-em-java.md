title: Como embaralhar uma lista em Java
date: 2017-06-26
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: List
image: /images/logo-java.png

Para embaralhar uma lista (List) em Java, 
nós podemos utilizar o método shuffle a classe java.util.Collections
que é nativa da API java.

Veja no exemplo abaixo como embaralhar os valores de um List.

```java
package br.com.dicasdejava;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class EmbaralharList {

	public static void main(String[] args){

		List<String> lista = Arrays.asList("A", "B", "C", "D", "E", "F");

		//Antes de embaralhar
		System.out.println(lista);

		Collections.shuffle(lista);

		//Depois de embaralhar
		System.out.println(lista);

		Collections.shuffle(lista);

		//Depois de embaralhar novamente
		System.out.println(lista);

	}

}
```

Saída:

```
[A, B, C, D, E, F]
[A, C, B, F, D, E]
[E, D, C, F, B, A]
```

Referências:

1. [JavaDoc: Collections](https://docs.oracle.com/javase/8/docs/api/java/util/Collections.html)
