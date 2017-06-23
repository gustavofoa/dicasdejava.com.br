title: Como ordenar um Array
date: 2017-06-23
author: Gustavo Furtado de Oliveira Alves
category: Java Util
tags: Array, Arrays
image: /images/logo_java.png

Para ordenar um Array (Vetor) nós podemos utilizar a classe java.util.Arrays
que é nativa da API java.

Veja no exemplo abaixo como ordenar um Array, tanto de texto quanto de número.

```java
package br.com.dicasdejava;

import java.util.Arrays;

public class OrdenarArray {

	public static void main(String[] args) {
		String[] nomes = new String[]{"João", "Gustavo", "Maria", "José", "Ana"};

		System.out.println("Nomes não ordenados:");
		for(String nome : nomes)
			System.out.println(nome);
		System.out.println();

		Arrays.sort(nomes);

		System.out.println("Nomes ordenados:");
		for(String nome : nomes)
			System.out.println(nome);
		System.out.println();

		int[] numeros = new int[]{20,2, 8, 19, 100, 5, 1, 6, 13};

		System.out.println("Números não ordenados:");
		for(int numero : numeros)
			System.out.println(numero);
		System.out.println();

		Arrays.sort(numeros);

		System.out.println("Números ordenados:");
		for(int numero : numeros)
			System.out.println(numero);
		System.out.println();

	}
}

```

Saída:

```
Nomes não ordenados:
João
Gustavo
Maria
José
Ana

Nomes ordenados:
Ana
Gustavo
José
João
Maria

Números não ordenados:
20
2
8
19
100
5
1
6
13

Números ordenados:
1
2
5
6
8
13
19
20
100
```

Referências:

1. [JavaDoc: Arrays](https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html)
