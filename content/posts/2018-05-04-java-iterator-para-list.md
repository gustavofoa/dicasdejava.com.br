---
title: 'Java: Como converter um Iterator em List'
date: '2018-05-04'
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: IteratorUtils, Apache Commons, List, Iterator, Lambda
image: /images/logo-java.png
---

É possível converter um Iterator em List de muitas formas em java. Com _lambda_, java antigo, Apache Commons, etc.
Vejamos então algumas das formas de fazer essa conversão...

## Convertendo Iterator em List com Lambda (Java 8)

A partir do Java 8, a interface ```Iterator``` oferece o método ```forEachRemaining```
que podemos utilizar para iterar nos itens restantes do _Iterator_ com _Lambda_.

Veja:

```java
package br.com.dicasdejava.util;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class IteratorParaList {

    public static void main(String[] args) {

    	List<String> listaDeNomes = new ArrayList<String>();
    	listaDeNomes.add("Gustavo");
    	listaDeNomes.add("Maria");
    	listaDeNomes.add("José");
    	listaDeNomes.add("João");
    	listaDeNomes.add("Ana");

    	Iterator<String> iteratorDeNomes = listaDeNomes.iterator();

		List<String> listaConvertidaDoIterator = new ArrayList<>();

		iteratorDeNomes.forEachRemaining(n -> listaConvertidaDoIterator.add(n));

		listaConvertidaDoIterator.forEach(System.out::println);

    }
}

```

Saída:
```
Gustavo
Maria
José
João
Ana
```

Outra forma de fazer essa conversão com _Lambda_ é passando apenas o método ```add```
da interface ```List``` para o método ```forEachRemainning```.

Veja:

```java
iteratorDeNomes.forEachRemaining(listaConvertidaDoIterator::add);
```

Funciona da mesma forma que o exemplo anterior.

## Convertendo Iterator em List Java 7 ou anterior

A forma antiga, básica, para converter um ```Iterator``` em ```List``` em java
é justamente "iterar" no iterator ...
Utilizando os métodos ```hasNext``` (para verificar se tem mais ítens no Iterator) e ```next``` (para obter o próximo ítem do iterator).

Veja:

```java
package br.com.dicasdejava.util;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class IteratorParaList {

    public static void main(String[] args) {

    	List<String> listaDeNomes = new ArrayList<String>();
    	listaDeNomes.add("Gustavo");
    	listaDeNomes.add("Maria");
    	listaDeNomes.add("José");
    	listaDeNomes.add("João");
    	listaDeNomes.add("Ana");

    	Iterator<String> iteratorDeNomes = listaDeNomes.iterator();

		List<String> listaConvertidaDoIterator = new ArrayList<>();

		while (iteratorDeNomes.hasNext()) {
			listaConvertidaDoIterator.add(iteratorDeNomes.next());
		}

		listaConvertidaDoIterator.forEach(System.out::println);

    }
}
```

## Convertendo Iterator em List utilizando Apache Commons Collections

Como sempre, a **Apache** tem uma biblioteca (**Apache Commons Collections**)
que também nos oferece um método ```toList``` na classe ```IteratorUtils```
para converter Iterator em List de forma simples.

Veja:


```java
package br.com.dicasdejava.util;

import org.apache.commons.collections.IteratorUtils;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class IteratorParaList {

    public static void main(String[] args) {

    	List<String> listaDeNomes = new ArrayList<String>();
    	listaDeNomes.add("Gustavo");
    	listaDeNomes.add("Maria");
    	listaDeNomes.add("José");
    	listaDeNomes.add("João");
    	listaDeNomes.add("Ana");

    	Iterator<String> iteratorDeNomes = listaDeNomes.iterator();

		List<String> listaConvertidaDoIterator = IteratorUtils.toList(iteratorDeNomes);

		listaConvertidaDoIterator.forEach(System.out::println);

    }
}
```

Mas lembre-se que é necessário importar o _Apache Commons Collections_ no seu projeto.

Se você estiver utilizando o Maven, pode adicionar a dependência
abaixo no seu `pom.xml` para utilizar todo o poder da biblioteca **Apache Commons Collections**.

```xml
<dependency>
	<groupId>commons-collections</groupId>
	<artifactId>commons-collections</artifactId>
	<version>3.2.2</version>
</dependency>
```

Referências:

1. [JavaDoc: Iterator.forEachRemaining](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html#forEachRemaining-java.util.function.Consumer-){:target=\_blank}
2. [JavaDoc: Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html){:target=\_blank}
3. [JavaDoc: IteratorUtils.toList](https://commons.apache.org/proper/commons-collections/apidocs/org/apache/commons/collections4/IteratorUtils.html#toList(java.util.Iterator)){:target=\_blank}