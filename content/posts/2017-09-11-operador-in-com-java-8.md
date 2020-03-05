---
title: 'Java: Operador IN - Verificando se um valor existe em um Array'
date: '2017-09-11'
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Java 8, Operadores
image: /images/logo-java.png
---

Em algumas linguagens de programação existem operadores para operações com conjuntos.
Um exemplo é o operador `in` em python, como podemos ver abaixo.

![Operador in na linguagem python](/images/in-python.png){:class=center-image}

Em java **não existe** o operador `in`, mas podemos fazer essa verificação de outras maneiras.

##Método **_contains_** 

A forma mais simples de fazer essa verificação em uma lista de **objetos**
é utilizando o método `contains` da interface `List`.

Lembrando que podemos
[converter um array em uma lista](http://dicasdejava.com.br/java-como-converter-array-para-list/){:target=\_blank}
de forma bem simples com o método `Arrays.asList()`.

Veja no exemplo abaixo:

```java
import java.util.Arrays;
import java.util.List;

public class ListaContem {
    public static void main(String[] args) {

        Integer[] a = new Integer[]{1, 2, 3, 4, 5};
        
        List<Integer> lista = Arrays.asList(a);

        System.out.println("3 in a = " + (lista.contains(3)));
        System.out.println("5 in a = " + (lista.contains(5)));
        System.out.println("6 in a = " + (lista.contains(6)));

    }
}
```

Saída:

```
3 in a = true
5 in a = true
6 in a = false
```

Entretanto, essa forma só funciona para uma lista de Objetos!
Não funciona para tipos primitivos, pois java não permite a criação de uma lista
 de tipo genérico primitivo.
 
Por exemplo, isso não é permitido em java:

```java
List<int> lista = new ArrayList<>();// <- NÃO COMPILA!!!
```
 
##Verificação em Tipo primitivo 

Vimos que não é possível utilizar o método `contains` para arrays de tipo primitivo.

Entretanto, podemos fazer essa verificação com Java 8 usando _Lambda_
e a classe de Stream do tipo primitivo.

No nosso exemplo vamos utilizar a class `java.util.stream.IntStream`,
mas poderíamos utilizar as classes `LongStream` ou `DoubleStream`
dependendo do tipo primitivo do array.

Veja no exemplo abaixo:

```java
import java.util.stream.IntStream;

public class ContainsParaTipoPrimitivo {
    public static void main(String[] args) {

        int[] a = new int[]{1, 2, 3, 4, 5};

        System.out.println("3 in a = " + (IntStream.of(a).anyMatch(x -> x == 3)));
        System.out.println("5 in a = " + (IntStream.of(a).anyMatch(x -> x == 5)));
        System.out.println("6 in a = " + (IntStream.of(a).anyMatch(x -> x == 6)));

    }
}
```

Saída:

```
3 in a = true
5 in a = true
6 in a = false
```


Referências:

1. [Javadoc: java.util.stream](https://docs.oracle.com/javase/8/docs/api/java/util/stream/package-summary.html){:target=\_blank}
2. [Javadoc: IntStream](https://docs.oracle.com/javase/8/docs/api/java/util/stream/IntStream.html){:target=\_blank}
3. [Javadoc: Arrays](https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html){:target=\_blank}
3. [Javadoc: List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html){:target=\_blank}