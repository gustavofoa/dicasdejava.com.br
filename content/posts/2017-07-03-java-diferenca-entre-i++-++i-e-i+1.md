---
title: 'Java: Diferença entre i++, ++i e i = i + 1'
date: '2017-07-03'
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Operadores aritméticos
image: /images/logo-java.png
---

É comum programadores iniciantes se depararem com um `i++` ou `++i`
no código **java** e não saberem para quê serve,
outros ficam na dúvida de qual a diferença entre `i++`, `++i` e `i = i + 1`.

No exemplo acima, `i` é apenas uma variável do tipo `int`,
podendo ter qualquer outro nome de variável.

No final das contas, essas três formas de incremento
vão incrementar um **único** valor na variável `i`.

Se forem utilizados em um comando simples, ou seja,
um comando que só tem o incremento e mais nada,
as três formas não tem nenhuma diferença.

Confira no exemplo abaixo.

```java
package br.com.dicasdejava.fundamentos;

public class IncrementoComMaisMaisOuComMais1ComandoSimples {

	public static void main(String[] args) {

		int i = 0;
		System.out.println(i);
		i++;
		System.out.println(i);
		++i;
		System.out.println(i);
		i = i + 1;
		System.out.println(i);

	}

}
```

Saída:

```
0
1
2
3
```

Entretanto se estas formas de incremento forem utilizadas em um comando composto,
ou seja, que contenha mais de uma instrução, os resultados podem ser diferentes.

A instrução `++i`, incrementa a variável `i` **antes** dela ser utilizada no comando.
Já a instrução `i++`, incrementa a variável `i` **depois** dela ser utilizada no comando.
E se você incrementar uma variável e atribuir o resultado a ela mesma,
em um comando, o resultado da instrução é o valor da variável após o incremento.

No exemplo abaixo vemos o resultado dos três tipos de incremento
como parâmetro do método `println`, ou seja, antes de terminar o "comando".

Lembrando que um comando _java_ só termina no `;` (ponto e vírgula)!

```java
package br.com.dicasdejava.fundamentos;

public class IncrementoComMaisMaisOuComMais1ComandoComposto {

	public static void main(String[] args) {

		int i = 0;

		System.out.println("      i++ => " + (i++));
		System.out.println("        i => " + i);

		System.out.println("      ++i => " + (++i));
		System.out.println("        i => " + i);

		System.out.println("i = i + 1 => " + (i = i + 1));
		System.out.println("        i => " + i);

	}

}
```

Saída:

```
      i++ => 0
        i => 1
      ++i => 2
        i => 2
i = i + 1 => 3
        i => 3
```

No primeiro `print`, quando utilizamos `i++`,
percebemos que foi utilizado o valor atual da variável `i` (0)
e em seguida a variável foi incrementada para (1), pois no print seguinte,
imprimimos apenas a variável, sem incremento.

Ao utilizar `++1`, percebemos que a variável `i`
foi incrementada antes de ser utilizada. Ou seja, era 1 e passou a ser 2.
Esse comportamento pode ser comprovado na linha seguinte,
quando imprimimos `i` novamente e obtemos o mesmo valor 2.

Por fim, se utilizarmos `i = i + 1` percebemos que a variável `i`
também foi incrementada antes de ser utilizada.
O que significa que a instrução `i = i + 1`,
resulta no valor da variável `i` após o incremento.

Espero que esta explicação te ajude, mas se ainda permenecer com dúvidas
poste aí nos comentários!
