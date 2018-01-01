title: Java: Como ler dados do Console com a classe Scanner
date: 2017-07-24
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Java, Console, Scanner
image: /images/logo-java.png

Uma dúvida comum em iniciantes em java é:
**Como ler dados digitados pelo usuário no console**?
Neste post vou mostrar como usar a classe `java.util.Scanner` para fazer isso.

Confira o exemplo abaixo.

```java
import java.util.Scanner;

class LerConsoleComScanner {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Qual o seu nome: ");
		String nome = scanner.next();
		System.out.println("Seja bem vindo " + nome + "!");
	}
}
```

##Execução

Após executar esse programa Java, aparece no console o texto: `Qual o seu nome: `. 

Em seguida, o programa espera que o usuário informe um texto e precione ENTER.

Se, por exemplo, o usuário digitar `Gustavo` e pressionar ENTER
o programa continua com a saída abaixo.
 
```
Qual o seu nome: Gustavo
Seja bem vindo Gustavo!
```

## A classe Scanner

A classe Scanner apareceu a partir do **Java 5**
com o objetivo de facilitar a entrada de dados no modo Console.

Uma das características mais interessante da classe `Scanner`
é a possibilidade de obter o valor digitado diretamente
no formato do tipo primitivo que o usuário digitar.
Para isso basta utilizarmos os métodos `next` do tipo primitivo
no formato `nextTipoDado()`. Como no código abaixo.

```java
Scanner scanner = new Scanner(System.in);
int numeroInteiro = scanner.nextInt();
byte numeroByte = scanner.nextByte();
long numeroLong = scanner.nextLong();
boolean booleano = scanner.nextBoolean();
float numeroFloat = scanner.nextFloat();
double numeroDouble = scanner.nextDouble();
```

Sempre bom fazer um exemplo para verificar o funcionamento.

```java
import java.util.Scanner;

class LerNumeroConsoleComScanner {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Digite um número inteiro: ");
		int numero = scanner.nextInt();
		System.out.print("O valor informado foi " + numero);
	}
}
```

Digitando o valor 50 na execução do programa, temos a seguinda saída.

```
Digite um número inteiro: 50
O valor informado foi 50
```

Mas é importante observar que se o valor não puder ser convertido para o tipo
especificado a exceção `java.util.InputMismatchException` será lançada.

```
Digite um número inteiro: teste
Exception in thread "main" java.util.InputMismatchException
	at java.util.Scanner.throwFor(Scanner.java:864)
	at java.util.Scanner.next(Scanner.java:1485)
	at java.util.Scanner.nextInt(Scanner.java:2117)
	at java.util.Scanner.nextInt(Scanner.java:2076)
	at br.com.dicasdejava.fundamentos.LerNumeroConsoleComScanner.main(LerConsoleComScanner.java:21)
```

Por isso é importante tratar essa _exceção_ na leitura de tipos primitivos.

```java
import java.util.Scanner;

class LerNumeroConsoleComScanner {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Digite um número inteiro: ");
		try {
			int numero = scanner.nextInt();
			System.out.print("O valor informado foi " + numero);
		} catch (InputMismatchException e) {
			System.out.print("O valor informado não é um número!");
		}
	}

}
```

Saída:

```
Digite um número inteiro: teste
O valor informado não é um número!
```

##Outras utilizações de Scanner

Vimos neste post um exemplo de utilização básica da classe Scanner
para leitura dos dados digitados no console com Java.

A classe Scanner é muito poderosa, podendo ser utilizada com outros
canais de entrada de dados como texto, arquivo, rede, etc.
Por exemplo, a classe Scanner pode ser utilizada para ler arquivos.
Como no exemplo abaixo.

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

Uma outra utilização da classe Scanner é a obtenção de dados filtrados
com **REGEX** e customização de _delimiter_, como no exemplo abaixo.

```java
import java.util.Scanner;
class FiltrarDadosComScannerRegex {
	public static void main(String[] args) {
		Scanner scanner = new Scanner("a1,b2,c3,d4,e5,f6");
		scanner.useDelimiter("\\d,?");
		while (scanner.hasNext())
			System.out.println(scanner.next());
		scanner.close();
	}
}
```

Saída:

```
a
b
c
d
e
f

```

Neste exemplo, nós utilizamos _REGEX_ para extratir apenas as letras da sequência.
A classe Scanner usa o _delimiter_ para agrupar os dados obtidos da fonte,
da mesma forma que o método `String.split(regex)`.
A diferença é que o Scanner não retorna o array com os dados agrupados
e também aceita outras fontes de dados como arquivo, console, rede, etc.

Embora a classe Scanner seja utilizada principalmente para ler dados
que o usuário digita no console,
podemos perceber que a Scanner vai muito além disso, 
podendo ser uma ótima ferramenta para extração de dados.

##Referências

1. [Javadoc: Scanner](https://docs.oracle.com/javase/7/docs/api/java/util/Scanner.html){:target=\_blank}