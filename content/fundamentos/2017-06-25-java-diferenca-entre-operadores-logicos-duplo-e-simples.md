title: Java: Diferença entre os operadores &&, &, || e |
date: 2017-06-25
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Operadores lógicos
image: /images/logo-java.png

Uma dúvida muito comum entre programadores Java iniciantes
é saber a diferença entre os operadores lógicos duplo ou simples, ou seja, 
a diferença entre **&&** e **&** para o operador **E**
e a diferença entre **||** e **|** para o operador **OU**.

A diferença é que a quando usamos a versão dupla do operador (&& e ||), 
se a condição da operação for resolvida, ela não continua as avaliações das condições seguintes.

Imagine que você está executando uma operação **E**.
Se a verificação da esquerda resultar **falso**, não é necessário verificar o teste do lado direito da operação, concorda?
Independente do resultado da segunda parte da operação, o resultado final será **falso**.

O mesmo se aplica para a operação **OU**.
Se a verificação da esquerda resultar **verdadeiro**, não é necessário verificar o teste do lado direito da operação.
Independente do resultado da segunda parte da operação, o resultado final será **verdadeiro**.

Quando usamos os operadores duplos (&& e ||) o java não continua as verificações se o resultado já for conhecido.
Já usando os operadores simples (& e |), ambos os lados da operação são **sempre** verificados.

Vamos ver um exemplo...

##Exemplo:

```java
package br.com.dicasdejava.fundamentos;

public class OperadoresLogicosDuploOuSimples {

	public static void main(String[] args) {

		System.out.println("false && true = " +
				(primeiraCondicao(false) && segundaCondicao(true)) +
				" - sem teste da segunda condição.");

		System.out.println();

		System.out.println("false & true = " +
				(primeiraCondicao(false) & segundaCondicao(true)) +
				" - com teste da segunda condição.");

		System.out.println();

		System.out.println("true || false = " +
			(primeiraCondicao(true) || segundaCondicao(false)) +
			" - sem teste da segunda condição.");

		System.out.println();

		System.out.println("true | false = " +
				(primeiraCondicao(true) | segundaCondicao(false)) +
				" - com teste da segunda condição.");

	}

	private static boolean primeiraCondicao(boolean retorno){
		System.out.println("Executou o teste da primeira condição");
		return retorno;
	}

	private static boolean segundaCondicao(boolean retorno){
		System.out.println("Executou o teste da segunda condição");
		return retorno;
	}

}
```

Saída:

```
Executou o teste da primeira condição
false && true = false - sem teste da segunda condição.

Executou o teste da primeira condição
Executou o teste da segunda condição
false & true = false - com teste da segunda condição.

Executou o teste da primeira condição
true || false = true - sem teste da segunda condição.

Executou o teste da primeira condição
Executou o teste da segunda condição
true | false = true - com teste da segunda condição.
```


Referências:

1. [Boolean Logical Operators &, ^, and |](http://docs.oracle.com/javase/specs/jls/se8/html/jls-15.html#jls-15.22.2)
2. [Conheça os operadores lógicos!](http://dicasdeprogramacao.com.br/operadores-logicos/)