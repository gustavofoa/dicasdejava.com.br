---
title: 'Java: Como juntar dois arrays'
date: '2018-07-16'
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: Array, Apache Commons
image: /images/logo-java.png
---

Neste post você verá como juntar dois arrays em java.

A forma mais simples de juntar dois arrays é utilizando o método estático `addAll` da classe `ArrayUtils`
da biblioteca **Apache Commons Lang**, passando os dois arrays como parâmetro.
O retorno deste método é um novo array que agrega os dois. Veja o código abaixo:

```java
package br.com.dicasdejava.util;

import org.apache.commons.lang3.ArrayUtils;

import java.util.Arrays;

public class JuntarArrays {

    public static void main(String[] args) {

    	String[] array1 = new String[]{ "a", "b", "c", "d"};
		String[] array2 = new String[]{ "e", "f", "g", "h"};

		String[] arraysJuntados = ArrayUtils.addAll(array1, array2);

		System.out.println(Arrays.toString(arraysJuntados));

    }
}
```

Saída:

```
[a, b, c, d, e, f, g, h]
```

## Maven

Se você utiliza Maven em seu projeto, pode adicionar a dependência abaixo no seu pom.xml
para utilizar todo o poder da biblioteca Apache Commons Lang.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.7</version>
</dependency>
```

## Referências:

1. [JavaDoc: ArrayUtils](https://commons.apache.org/proper/commons-lang/apidocs/org/apache/commons/lang3/ArrayUtils.html){:target=\_blank}
