title: Java: Varargs...
date: 2017-07-05
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Varargs, Java Básico
image: /images/logo-java.png

Somente o último parâmetro de um método em Java pode ser do tipo **varargs**.

Um parâmetro vararg pode receber **0**, **muitos** ou um **array** de parâmetros.
Aliás, é por essa característica que o parâmetro vararg
**deve ser o último parâmetro do método**. 

Para declarar um vararg nós colocamos três pontinhos no tipo do parâmetro.
Por exemplo: `void metodo1(int a, String... b)`. 
Neste exemplo o parâmetro `b` é o parâmetro **vararg** do método.

Vejamos no exemplo abaixo todas as formas de utilizar o parâmetro do tipo _vararg_. 

```java
package br.com.dicasdejava.fundamentos;

public class Varargs {

	public static void main(String[] args) {

		//Sem o 3º parâmetro (Vararg...)
		metodoComVarargs("a1", true);

		//Com o 3º parâmetro do tipo int
		metodoComVarargs("a2", false, 1);

		//Com o 3º parâmetro do tipo int[] (array de int)
		metodoComVarargs("a3", true, new int[]{1, 2, 3});

		//Com vários parâmetros int a partir do 3º parâmetro (Vararg...)
		metodoComVarargs("a4", true, 1, 2, 3, 4, 5);

	}

	static void metodoComVarargs(String a, boolean b, int... c) {

		System.out.println(a);
		System.out.println(b);
		System.out.println(c.length);
		for (int d : c)
			System.out.println(d);
		System.out.println();

	}

}
```

Saída:

```
a1
true
0

a2
false
1
1

a3
true
3
1
2
3

a4
true
5
1
2
3
4
5
```

##Deve ser do mesmo tipo!

É importante notar que o Vararg recebe **valores do mesmo tipo**.
Não podemos por exemplo, chamar o método do exemplo acima
passando os seguintes parâmetros.

```java
//NÃO PODE CHAMAR O MÉTODO ASSIM!
metodoComVarargs("a3", true, 1, "texto", false, 'c');
```

##Deve ser o último parâmetro!

Como já vimos no inicio do post, 
o parâmetro _vararg_ deve ser o último parâmetro do método.
Não podemos declarar um método como no exemplo a baixo

```java
//NÃO PODE DECLARAR O MÉTODO ASSIM!
void metodoComVarargs(String a, boolean... b, int c)
```

Referências:

1. [JavaDoc: Varargs](https://docs.oracle.com/javase/1.5.0/docs/guide/language/varargs.html)
