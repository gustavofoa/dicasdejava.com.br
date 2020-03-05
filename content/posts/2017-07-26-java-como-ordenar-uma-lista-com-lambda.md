---
title: 'Java: Como ordenar uma lista com Lambda'
date: '2017-07-26'
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Java, List, Lambda, Comparator, Sort
image: /images/logo-java.png
---

A partir do Java 8, podemos usar funções lambda para muita coisas.
Uma delas é a ordenação de listas.

Inclusive, podemos utilizar o 
[**método default**](http://dicasdejava.com.br/java-implementando-metodos-na-interface-com-default-methods/){:target=\_blank}
da interface List `List.sort(Comparator<? super E> c)` para ordenar a nossa lista.  

Veja como ficou simples ordenar uma lista com Lambda a partir do Java 8.

```java
package br.com.dicasdejava.fundamentos;

import java.util.Arrays;
import java.util.List;

public class OrdenarListaComLamba {

	public static void main(String[] args) {

		List<String> nomes = Arrays.asList("Gustavo", "Daiana", "Wellington", "José", "Julia");

		nomes.sort((a, b) -> a.compareTo(b));

		for (String nome : nomes)
			System.out.println(nome);

	}

}
```

Saída:
 
```
Daiana
Gustavo
José
Julia
Wellington
```

##Referências

1. [Javadoc: List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html){:target=\_blank}
2. [Java: Implementando métodos na interface com Default Methods!](http://dicasdejava.com.br/java-implementando-metodos-na-interface-com-default-methods/){:target=\_blank}
3. [Using Lambda Expression to sort a List in Java 8 using Netbeans Lambda Support](https://sanaulla.info/2013/03/11/using-lambda-expression-to-sort-a-list-in-java-8-using-netbeans-lambda-support/){:target=\_blank}
4. [Código-fonte de Exemplo](https://github.com/gustavofoa/examples.dicasdejava.com.br){:target=\_blank}