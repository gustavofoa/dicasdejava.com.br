---
title: 'Como gerar um número aleatório em Java'
date: '2018-04-10'
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: Random
image: /images/logo-java.png
---

Gerar número aleatório em java é uma tarefa fácil.

Primeiro você precisa importar a classe `Random` do pacote `java.util`

```java
import java.util.Random
```

Agora você pode instanciar um objeto da classe `Random`.

```java
Random random = new Random();
```


Pronto! Com o objeto `random` você pode gerar números aleatórios! :)

Vejamos como gerar números aleatórios inteiros e reais.

### Gerando números inteiros aleatórios de 0 à 100

Para gerar números aleatórios inteiros de 0 até um determinado valor, basta chamar o método `nextInt`
informando o valor máximo. No nosso exemplo o máximo é 100:

```java
int numero = random.nextInt(100);
```

### Gerando números reais aleatórios

Números reais são gerados de 0 até 1 com a função `nextDouble`.
Logo, se você quiser um número aleatório de 0 até o número que você quiser, basta multiplicar por ele.

Por exemplo, para gerar um número aleatório de 0 até 100 basta multiplicar o número gerado por 100.

```java
double numero random.nextDouble() * 100; //Número aleatório de 0 à 100
```

### Código de exemplo

No código abaixo, podemos ver a geração de números aleatórios conforme expliquei acima.

```java
package br.com.dicasdejava.util;

import java.util.Random;

public class GerarNumeroAleatorio {

	public static void main(String[] args) {

		Random random = new Random();

		int numeroInteiroAleatorio_0_a_10 = random.nextInt(10);
		System.out.println("Número inteiro aleatório de 0 até 10: " + numeroInteiroAleatorio_0_a_10);

		double numeroRealAleatorio_0_a_1 = random.nextDouble();
		System.out.println("Número real aleatório de 0 até 1: " + numeroRealAleatorio_0_a_1);

		double numeroRealAleatorio_0_a_10 = random.nextDouble() * 10;
		System.out.println("Número real aleatório de 0 até 10: " + numeroRealAleatorio_0_a_10);

	}

}
```

Exemplo de saída:

```
Número inteiro aleatório de 0 até 100: 43
Número real aleatório de 0 até 1: 0.16296306514069792
Número real aleatório de 0 até 100: 46.890481714549026
```

Referências:

1. [JavaDoc: Random](https://docs.oracle.com/javase/8/docs/api/java/util/Random.html){:target=\_blank}
