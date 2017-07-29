title: Java: Como converter um InputStream em String
date: 2017-07-30
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: IOUtils, Apache Commons, InputStream, String
image: /images/logo-java.png

Para converter um InputStream, que pode ser qualquer fonte de informação,
em um String nós podemos fazer uso do método estático `IOUtils.toString(inputStream)`
da biblioteca **Apache Commons IO**.

Um InputStream pode ser vários tipos de fonte de inforamação,
um arquivo, a rede, uma requisição Http, um array de bytes (como o exemplo abaixo), etc.

Veja no exemplo abaixo **como converter um InputStream em uma String**
de forma simples utilizando a biblioteca _Apache Commons IO_.

```java
package br.com.dicasdejava.util;

import org.apache.commons.io.IOUtils;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;

public class InputStreamToString {
	public static void main(String[] args) throws IOException {
		InputStream inputStream = new ByteArrayInputStream("Gustavo Furtado de Oliveira Alves".getBytes());
		String textoConvertido = IOUtils.toString(inputStream);
		System.out.println(textoConvertido);
	}
}
```

Saída:

```
Gustavo Furtado de Oliveira Alves
```

No exemplo acima, podemos ver que utilizando a classe IOUtils da _Apache Commons IO_
conseguimos facilmente converter um InputStream em um objeto String através do método `toString`.

##Maven

Se você utiliza Maven em seu projeto, pode adicionar a dependência
abaixo no seu `pom.xml` para utilizar todo o poder da biblioteca **Apache Commons IO**.

```xml
<dependency>
	<groupId>org.apache.commons</groupId>
	<artifactId>commons-io</artifactId>
	<version>1.3.2</version>
</dependency>
```

Referências:

1. [JavaDoc: IOUtils](https://commons.apache.org/proper/commons-io/javadocs/api-2.5/org/apache/commons/io/IOUtils.html){:target=\_blank}
2. [Código-fonte de Exemplo](https://github.com/gustavofoa/examples.dicasdejava.com.br/blob/master/src/br/com/dicasdejava/util/InputStreamToString.java){:target=\_blank}