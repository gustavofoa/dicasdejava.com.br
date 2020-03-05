---
title: 'Java: Como encriptar e desecriptar uma String em Base64'
date: '2018-06-06'
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: Apache Commons, Encriptação, String
image: /images/logo-java.png
---

Embora **NÃO seja uma forma segura de armazenar senhas**, encriptação com
Base64 é muito comum para serialização de arquivos e textos.
Ou melhor, os "bytes" do texto, já que Base64 é uma serialização _byte-to-text_.

Outra grande utilização da serialização em Base64 é para garantir a integridade de dados trafegados.

Enfim, existe mais de uma maneira de "serializar" e "deserializar" um texto para Base64 em Java.
Neste post vamos ver duas delas ...

## Utilizando a classe Base64 do pacote java.util

A classe `java.util.Base64` foi adicionada à 
[API Java](https://docs.oracle.com/javase/8/docs/api/java/util/Base64.html){:target=\_blank}
a partir do *Java 8*.
Dentre as funcionalidades disponíveis, estão duas classes aninhadas (nested-class)
`Base64.Encoder` e `Base64.Decoder`, que provêem métodos estáticos para serializar e deserializar bytes.

Vejamos um exemplo que mostra uma serialização/deserialização utilizando esta classe `Base64`.


```java
package br.com.dicasdejava.util;

import java.util.Base64;

public class SerializacaoDeserializacaoBase64 {

    public static void main(String[] args) {

    	String textoOriginal = "esta é uma string de teste para serialização/deserialização em Base64";

		System.out.println("Texto original: " + textoOriginal);

		String textoSerializado = Base64.getEncoder().encodeToString(textoOriginal.getBytes());

		System.out.println("Texto em Base64: " + textoSerializado);

		String textoDeserializado = new String(Base64.getDecoder().decode(textoSerializado));

		System.out.println("Texto deserializado: "+ textoDeserializado);

	}
}

```

Com o código acima, podemos perceber que a serialização Base64 é uma serialização de bytes em texto.
Ou seja:

- **Para encriptar**, passamos `textoOriginal.getBytes()` como parâmetro para o método `Base64.getEncoder().encodeToString` e recebemos uma `String` que é o texto no formato Base64.
- **Para decriptar**, passamos uma `String`, que é o texto no formato Base64, 
e recebemos um array de bytes (`byte[]`), para transformar esse array de bytes em string,
passamos esse array de bytes para o construtor da classe `String(byte[])`.

### Saída

A saída do programa acima é essa:

```
Texto original: esta é uma string de teste para serialização/deserialização em Base64
Texto em Base64: ZXN0YSDDqSB1bWEgc3RyaW5nIGRlIHRlc3RlIHBhcmEgc2VyaWFsaXphw6fDo28vZGVzZXJpYWxpemHDp8OjbyBlbSBCYXNlNjQ=
Texto deserializado: esta é uma string de teste para serialização/deserialização em Base64
```

## Utilizando Apache Commons Codec

Também tem uma biblioteca útil da apache (**Apache Commons Codec**)
que oferece métodos para serialização e deserialização de Base64.

Se você estiver utilizando o Maven, pode adicionar a dependência
abaixo no seu `pom.xml` para utilizar todo o poder da biblioteca **Apache Commons Codec**.

```xml
<dependency>
	<groupId>commons-codec</groupId>
	<artifactId>commons-codec</artifactId>
	<version>1.11</version>
</dependency>
```

A _Apache Commons Codec_ oferece a classe `org.apache.commons.codec.binary.Base64`.
para acessar os métodos _encodeAsString_  e _decode_ é necessário criar uma instância dela.
Veja abaixo um exemplo.


```java
package br.com.dicasdejava.util;

import org.apache.commons.codec.binary.Base64;

public class SerializacaoDeserializacaoBase64ApacheCommons {

    public static void main(String[] args) {

    	String textoOriginal = "esta é uma string de teste para serialização/deserialização em Base64";

		System.out.println("Texto original: " + textoOriginal);

		Base64 base64 = new Base64();

		String textoSerializado = base64.encodeAsString(textoOriginal.getBytes());

		System.out.println("Texto em Base64: " + textoSerializado);

		String textoDeserializado = new String(base64.decode(textoSerializado));

		System.out.println("Texto deserializado: "+ textoDeserializado);

	}
}
```

O funcionamento dos métodos `encodeAsString` e `decode` é o mesmo.
O `encodeAsString` recebe um array de bytes (`byte[]`) e retorna uma `String`,
e o método `decode` recebe uma `String` e retorna um array de bytes (`byte[]`).

A saída deste programinha é a mesma do exemplo anterior.

```
Texto original: esta é uma string de teste para serialização/deserialização em Base64
Texto em Base64: ZXN0YSDDqSB1bWEgc3RyaW5nIGRlIHRlc3RlIHBhcmEgc2VyaWFsaXphw6fDo28vZGVzZXJpYWxpemHDp8OjbyBlbSBCYXNlNjQ=
Texto deserializado: esta é uma string de teste para serialização/deserialização em Base64
```

Referências:

1. [JavaDoc: Base64 (API Java)](https://docs.oracle.com/javase/8/docs/api/java/util/Base64.html){:target=\_blank}
2. [JavaDoc Base64 (Apache)](https://commons.apache.org/proper/commons-codec/apidocs/org/apache/commons/codec/binary/Base64.html){:target=\_blank}