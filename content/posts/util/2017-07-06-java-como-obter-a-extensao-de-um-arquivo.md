title: Java: Como obter a extensão de um arquivo
date: 2017-07-06
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: FilenameUtils, List, Apache Commons IO
image: /images/logo-java.png

Há várias formas de extrair a extensão do nome de um arquivo.
A forma mais simples e legível para o o seu código, é utilizando o método 
`FilenameUtils.getExtension` da biblioteca **Apache Commons IO**.

Veja no exemplo abaixo como obter a extensão do nome de um arquivo
com `FilenameUtils.getExtension`.

```java
package br.com.dicasdejava.util;

import org.apache.commons.io.FilenameUtils;

public class ExtrairExtensaoArquivoComFilenameUtils {

	public static void main(String[] args) {
		//Exemplo de arquivo do Windows
		String nomeCompletoDoArquivo = "C:\\temp\\arquivo de teste.txt";
		String extensaoDoArquivo = FilenameUtils.getExtension(nomeCompletoDoArquivo);
		System.out.println(extensaoDoArquivo);

		//Exemplo de arquivo sem extensão
		nomeCompletoDoArquivo = "C:\\temp\\arquivo sem extensao";
		extensaoDoArquivo = FilenameUtils.getExtension(nomeCompletoDoArquivo);
		System.out.println(extensaoDoArquivo);

		//Exemplo de arquivo do Linux/Unix/OSX
		nomeCompletoDoArquivo = "/home/gustavo/arquivo de imagem.png";
		extensaoDoArquivo = FilenameUtils.getExtension(nomeCompletoDoArquivo);
		System.out.println(extensaoDoArquivo);
	}

}
```

Saída:

```
txt

png
```

#Importação da biblioteca Apache Commons IO

Como a **Apache Commons IO** não é uma biblioteca nativa do Java,
nós precisamos adicionar o arquivo **jar** da biblioteca 
no classpath da nossa aplicação.

Você pode baixar o **jar** da _Apache Commons IO_ diretamente no 
[site da Apache](http://commons.apache.org/proper/commons-io/download_io.cgi){:target=\_blank}.

Se você estiver utilizando o maven no seu projeto,
basta adicionar a dependência do _Apache Commons IO_ no seu arquivo `pom.xml`.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-io</artifactId>
    <version>1.3.2</version>
</dependency>
```

Indico a importação do **Apache Commons IO** porque,
além do método que mostrei aqui, há muitos outros métodos úteis
nessa biblioteca.

##Obter extensão do arquivo com Java PURO

Podemos utilizar uma lógica para obter a extensão do arquivo
utilizando apenas **java**.
Sem a necessidade de usar a biblioteca citada anteriormente.

Para isso, podemos fazer um `substring` do nome do arquivo,
a partir da posição (+1) do último ponto encontrado no nome do arquivo.

Mas devemos nos atentar para a verificação se o arquivo tem extensão,
ou seja, se tem "ponto" no nome do arquivo,
pois se o nome do arquivo não tiver ponto,
vamos obter o nome completo do arquivo ao invés de uma "extensão vazia". 

Observe no exemplo.

```java
package br.com.dicasdejava.util;

public class ExtrairExtensaoArquivoComJavaPuro {

	public static void main(String[] args) {

		//Exemplo de arquivo do Windows
		String nomeCompletoDoArquivo = "C:\\temp\\arquivo de teste.docx";
		String extensaoDoArquivo = getFileExtension(nomeCompletoDoArquivo);
		System.out.println(extensaoDoArquivo);

		//Exemplo de arquivo sem extensão
		nomeCompletoDoArquivo = "C:\\temp\\arquivo sem extensao";
		extensaoDoArquivo = getFileExtension(nomeCompletoDoArquivo);
		System.out.println(extensaoDoArquivo);

		//Exemplo de arquivo do Linux/Unix/OSX
		nomeCompletoDoArquivo = "/home/gustavo/arquivo de imagem.jpg";
		extensaoDoArquivo = getFileExtension(nomeCompletoDoArquivo);
		System.out.println(extensaoDoArquivo);

	}

	static String getFileExtension(String filename) {
		if (filename.contains("."))
			return filename.substring(filename.lastIndexOf(".") + 1);
		else
			return "";
	}

}
```

Saída:

```
docx

jpg
```

## Referências:

1. [Javadoc: FilenameUtils](https://commons.apache.org/proper/commons-io/javadocs/api-release/index.html?org/apache/commons/io/package-summary.html){:target=\_blank}
2. [Maven: Apache Commons IO](https://mvnrepository.com/artifact/org.apache.commons/commons-io){:target=\_blank}
3. [Javadoc: String](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html){:target=\_blank}
