title: Java: Como transformar uma String separada por virgula em Array
date: 2017-06-28
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Regex, String, Array
image: /images/logo-java.png

Confira no exemplo abaixo como transformar uma String
com valores separadores por vírgula em um Array.

##Exemplo:

```java
package br.com.dicasdejava.fundamentos;

public class StringSeparadaPorVirgulaEmArray {

	public static void main(String[] args) {

		String stringDeNomes = "João, Carlos, José, Marcos, Maria, Julia, Joaquim, Ana";

		String[] arrayDeNomes = stringDeNomes.split(", ");

		System.out.println("Tamanho do array: "+arrayDeNomes.length);

		for(String nome : arrayDeNomes)
			System.out.println(nome);

	}

}
```

Saída:

```
Tamanho do array: 8
João
Carlos
José
Marcos
Maria
Julia
Joaquim
Ana
```

Referências:

1. [JavaDoc: String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)
