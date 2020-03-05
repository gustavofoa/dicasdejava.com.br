---
title: 'Java: Como criar um InputStream a partir de uma String'
date: '2018-05-04'
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: IOUtils, Apache Commons, InputStream, String
image: /images/logo-java.png
---

A forma mais rápida para criar um InputStream a partir de uma String é criando uma instancia da classe
```ByteArrayInputStream```.

Veja no código abaixo.


```java
package br.com.dicasdejava.util;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.io.IOException;

public class InputStreamFromString {

	public static void main(String[] args) throws IOException {
		InputStream inputStream = new ByteArrayInputStream("Um texto qualquer".getBytes());
	}

}
```

O código acima cria um InputStream a partir de uma String.

A classe ```java.io.ByteArrayInputStream``` recebe um array de bytes em seu construtor.
E nós podemos obter esse array de bytes através do método ```getBytes()``` da classe String.

## Utilizando Apache Commons IO

Outra forma simples de converter uma String em InputStream é utilizando o método estático ```toInputStream```
da classe ```IOUtils``` da biblioteca **Apache Commons IO**.

Veja:


```java
package br.com.dicasdejava.util;

import org.apache.commons.io.IOUtils;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;

public class InputStreamFromString {
	public static void main(String[] args) throws IOException {
		InputStream inputStream = IOUtils.toInputStream(initialString);
	}
}
```

Mas lembre-se que é necessário importar o _Apache Commons IO_ no seu projeto.

Se você estiver utilizando o Maven, pode adicionar a dependência
abaixo no seu `pom.xml` para utilizar todo o poder da biblioteca **Apache Commons IO**.

```xml
<dependency>
	<groupId>org.apache.commons</groupId>
	<artifactId>commons-io</artifactId>
	<version>1.3.2</version>
</dependency>
```

Referências:

1. [JavaDoc: String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html){:target=\_blank}
2. [JavaDoc: ByteArrayInputStream](https://docs.oracle.com/javase/8/docs/api/java/io/ByteArrayInputStream.html){:target=\_blank}
3.  [JavaDoc: IOUtils](https://commons.apache.org/proper/commons-io/javadocs/api-2.5/org/apache/commons/io/IOUtils.html){:target=\_blank}