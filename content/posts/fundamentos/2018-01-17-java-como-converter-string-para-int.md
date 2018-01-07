title: Java: Como converter String para int
date: 2018-01-17
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Java, String, int, conversão
image: /images/logo-java.png

Muitas vezes precisamos converter um texto em um número para, por exemplo, fazer cálculos.

Para converter uma String em um int em java basta utilizar o método ```parseInt``` da class wrapper ```Integer```.

Veja:

```java
package br.com.dicasdejava.fundamentos;

public class ConverterStringParaInt {

	public static void main(String[] args) {

		String numero = "25";
		
		int numeroConvertido = Integer.parseInt(numero);

		int numeroVezes2 = numeroConvertido * 2;

		System.out.println("Resultado: " + numeroVezes2);

	}

}
```

Saída:

```
Resultado: 50
```

## Tratando número inválido

Caso o texto que está sendo convertido não seja um número válido.
o método ```Integer.parseInt(String)``` lançará uma Exceção do tipo **NumberFormatException**.

Veja:

```java
package br.com.dicasdejava.fundamentos;

public class ConverterStringParaInt {

	public static void main(String[] args) {

		String numero = "dez";
		int numeroConvertido = Integer.parseInt(numero);

		int numeroVezes2 = numeroConvertido * 2;

		System.out.println("Resultado: " + numeroVezes2);

	}

}
```

Saída:

```
Exception in thread "main" java.lang.NumberFormatException: For input string: "dez"
	at java.lang.NumberFormatException.forInputString(NumberFormatException.java:65)
	at java.lang.Integer.parseInt(Integer.java:580)
	at java.lang.Integer.parseInt(Integer.java:615)
	at br.com.dicasdejava.fundamentos.ConverterStringParaInt.main(ConverterStringParaInt.java:8)
```

Por isso, é sempre importante tratar esta exceção quando estiver convertendo
um String para int.

Assim:

```java
package br.com.dicasdejava.fundamentos;

public class ConverterStringParaInt {

	public static void main(String[] args) {

		try {

			String numero = "dez";
			int numeroConvertido = Integer.parseInt(numero);

			int numeroVezes2 = numeroConvertido * 2;

			System.out.println("Resultado: " + numeroVezes2);

		} catch (NumberFormatException e){
			System.out.println("Número inválido!");
		}

	}

}
```

Saída:

```
Número inválido!
```


##Referências

1. [Javadoc: Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html){:target=\_blank}
