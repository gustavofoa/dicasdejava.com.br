title: Java: É possível acessar elementos da Superclasse da Superclasse?
date: 2017-07-21
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Java, Override, super.super
image: /images/logo-java.png

Você deve saber que para acessar um membro de uma Superclasse,
nós utilizamos a palavra-chave `super`.
Por exemplo, `super.nome`.

Mas e se nós quisermos acessar um elemento que está na Superclasse da Superclasse?
Ou seja, dois níveis acima.
Não podemos utilizar `super.super.nome` nem `super.super.super.nome`!

Isto pode ser um problema se você estiver subscrevendo métodos.
Ou seja, criando um método com o mesmo nome de um método da Superclasse.
Pois os métodos das classes acima da Superclasse podem se tornar inacessíveis.

Uma forma de acessar atributos de classes superiores é fazendo um _cast_.
Por exemplo:

```java
((Pai) this).nome
```

Mas isso não funciona para métodos se houver uma subscrição de método.
O código abaixo acessaria o método getNome da classe filha.

```java
((Pai) this).getNome();
```

Vamos ver um exemplo mais completo para percebermos esse comportamento.

##Exemplo:

```java
package br.com.dicasdejava.fundamentos;

class Avo {
	String nome = "Avo";
	String getNome() {
		return nome;
	}
}


class Pai extends Avo {
	String nome = "Pai";
	String getNome() {
		return nome;
	}
}


class Filho extends Pai {
	String nome = "Filho";
	String getNome() {
		return nome;
	}
}

class TesteOverriding {
	public static void main(String[] args) {
		Filho filho = new Filho();
		System.out.println(filho.nome);
		System.out.println(filho.getNome());
		System.out.println(((Pai) filho).nome);
		System.out.println(((Pai) filho).getNome());
		System.out.println(((Avo) filho).nome);
		System.out.println(((Avo) filho).getNome());
	}
}
```

Saída:

```
Filho
Filho
Pai
Filho
Avo
Filho
```

Podemos observar que, ao fazermos _cast_ do objeto `homem`, 
nós conseguimos acessar diretamente a variável nome das classes mais acima da hierarquia.
Mas o mesmo não funcionou para o método `getNome()`.

O método `getNome()` executado sempre foi o da classe Homem.
