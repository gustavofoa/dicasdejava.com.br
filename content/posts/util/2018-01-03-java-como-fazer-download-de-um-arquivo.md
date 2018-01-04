title: Java: Como fazer download de um arquivo
date: 2018-01-03
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: Array, List, Arrays
image: /images/logo-java.png

As vezes precisamos baixar um arquivo utilizando Java e existem várias formas de fazer isso.
Neste post você verá 3 formas de fazer o download de um arquivo com Java.

- Apache Commons IO
- Java IO
- Java NIO

## Apache Commons IO

A minha forma preferida de baixar arquivos com Java, e algumas outras tarefas,
é utilizando a biblioteca _Commons IO_ da Apache.

A Commons IO tem uma classe chamada FileUtils que tem vários métodos estáticos úteis,
um deles é o ```FileUtils.copyURLToFile(URL source, File destination)```.

O código abaixo mostra um exemplo de como baixar um arquivo utilizando a _Apache Commons IO_.

```java
package br.com.dicasdejava.util;

import org.apache.commons.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.net.URL;

public class DownloadFile {

    public static void main(String[] args) throws IOException {

        URL url = new URL("http://dicasdejava.com.br/images/logo-java.png");
        File file = new File("C:\\temp\\arquivo-baixado.png");

        FileUtils.copyURLToFile(url, file);

    }

}

```

Lembrando que é necessário adicionar a biblioteca _Commons IO_
como dependência do seu projeto.
Se você estiver utilizando o maven, basta adicionar a dependência do Apache Commons IO no seu arquivo pom.xml.

```xml
<dependency>
    <groupId>commons-io</groupId>
    <artifactId>commons-io</artifactId>
    <version>2.6</version>
</dependency>
```

## Java IO

Uma forma de baixar um arquivo com java, sem usar nenhuma dependência,
é com o pacote java.io nativo do java.

Basta obter o arquivo num InputStream e escrevê-lo num FileOutputStream.

```java
package br.com.dicasdejava.util;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;

public class DownloadFile {

    public static void main(String[] args) throws IOException {

        URL url = new URL("http://dicasdejava.com.br/images/logo-java.png");
        File file = new File("C:\\temp\\arquivo-baixado.png");

        InputStream is = url.openStream();
        FileOutputStream fos = new FileOutputStream(file);

        int bytes = 0;

        while ((bytes = is.read()) != -1) {
            fos.write(bytes);
        }

        is.close();

        fos.close();
    }


}
```

## Java NIO

Por fim, também podemos usar outro pacote nativo do Java: **java.nio**

```java
package br.com.dicasdejava.util;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.nio.channels.Channels;
import java.nio.channels.ReadableByteChannel;

public class DownloadFile {

    public static void main(String[] args) throws IOException {

        URL url = new URL("http://dicasdejava.com.br/images/logo-java.png");
        File file = new File("/home/gustavo/arquivo-baixado.png");

        ReadableByteChannel rbc = Channels.newChannel(url.openStream());
        FileOutputStream fos = new FileOutputStream(file);
        fos.getChannel().transferFrom(rbc, 0, Long.MAX_VALUE);
        fos.close();
        rbc.close();

    }

}
```

Referências:

1. [Maven: Commons IO](https://mvnrepository.com/artifact/org.apache.commons/commons-io){:target=\_blank}
2. [JavaDoc: FileUtils](https://commons.apache.org/proper/commons-io/javadocs/api-2.6/org/apache/commons/io/FileUtils.html){:target=\_blank}
3. [JavaDoc: URL](https://docs.oracle.com/javase/8/docs/api/java/net/URL.html){:target=\_blank}
4. [JavaDoc: FileOutputStream](https://docs.oracle.com/javase/8/docs/api/java/io/FileOutputStream.html){:target=\_blank}
5. [JavaDoc: InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html){:target=\_blank}
6. [JavaDoc: FileChannel](https://docs.oracle.com/javase/8/docs/api/java/nio/channels/FileChannel.html){:target=\_blank}
7. [JavaDoc: ReadableByteChannel](https://docs.oracle.com/javase/8/docs/api/java/nio/channels/ReadableByteChannel.html){:target=\_blank}