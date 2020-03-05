---
title: 'Java: Como ler um arquivo com a classe Scanner'
date: '2018-05-02'
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Java, Arquivo, Scanner
image: /images/logo-java.png
---

Muitas pessoas têm dúvidas de como ler os dados de um arquivo em java.
Neste post aprensento uma das formas mais simples de fazer isso:
Utilizando a classe ```java.util.Scanner```

Um dos construtores da classe **Scanner** recebe um arquivo como parâmetro.
Criando o objeto Scanner com este construtor, ele vai utilizar o arquivo como entrada de dados.

Confira o exemplo abaixo.

```java
import java.util.Scanner;

class LerArquivoComScanner {
	public static void main(String[] args) throws FileNotFoundException {
		File arquivo = new File("C:\\temp\\arquivo.txt");
		Scanner sc = new Scanner(arquivo);
		while (sc.hasNext()) {
			System.out.print(sc.nextLine());
		}
		sc.close();
	}
}
```

O exemplo acima, lê o arquivo `C:\temp\arquivo.txt` e imprime o seu
conteúdo no console.

## A classe Scanner

A classe Scanner é muito poderosa e foi introduzida a partir do **Java 5**
com o objetivo de facilitar a entrada de dados no modo Console.

Uma das características mais interessante da classe `Scanner`
é a possibilidade de obter o valor do Stream diretamente
no formato do seu tipo primitivo.
Para isso basta utilizar os métodos `next` do tipo primitivo
no formato `nextTipoDado()`.
Além disso é possível fazer filtros com Regex e muitas outras coisas.

Se quiser ver algumas outras utilizações da classe Scanner,
confira este outro post aqui do blog:

[**>> Java: Como ler dados do Console com a classe Scanner**](https://dicasdejava.com.br/java-como-ler-dados-do-console-com-a-classe-scanner/){:target=\_blank}

##Referências

1. [Javadoc: Scanner](https://docs.oracle.com/javase/7/docs/api/java/util/Scanner.html){:target=\_blank}