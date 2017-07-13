title: Java: Como extrair uma lista de propriedades de itens de uma lista
date: 2017-07-13
author: Pedro Henrique Ribeiro Rodrigues
category: Util
tags: List, Collectors
image: /images/logo-java.png

Pense na classe Pessoa:

```java
package br.com.dicasdejava.entity;

public class Pessoa {
	private String nome;
	
	public Pessoa(String nome) {
		this.nome = nome;
	}
	
	public String getNome() {
		return this.nome;
	}
}
```

Quando você tem em mãos uma lista de Pessoas, e deseja obter uma listagem dos nomes dessas pessoas. O que fazer?

A partir do Java 8 foi introduzido em collections as funcionalidades do Collectors que funcionam em cima do Stream de uma coleção. Sendo assim para obter a lista de nomes utiliza-se o código exemplo a seguir:

```java
	List<Pessoa> pessoas = Arrays.asList(new Pessoa("Fulano"), new Pessoa("Ciclano"), new Pessoa("Beltrano"));
	List<String> nomes = pessoas.stream().map(Pessoa::getNome).collect(Collectors.toList());
	System.out.print(nomes.toArray());
```

Resultado:

```
["Fulano", "Ciclano", "Beltrano"]
```

Referências:

1. [JavaDoc: Collectors](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Collectors.html)