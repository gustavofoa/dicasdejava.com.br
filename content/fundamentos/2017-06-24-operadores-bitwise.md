title: Operadores Bitwise em Java
date: 2017-06-24
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Operadores Bitwise, Bitwise, Operadores Lógicos
image: /images/logo-java.png

É possível realizar [operações lógicas](http://www.dicasdeprogramacao.com.br/operadores-logicos/) entre números inteiros em Java.
Mas como assim? Operações lógicas não são somente entre valores lógicos (booleanos)?

Sim e Não...

Sim, operações lógicas (E, Ou, Não, Não-E, Não-Ou, Ou-Exclusivo, etc.)
são realizadas apenas entre valores lógicos.

Entretanto em Java é possível realizar algumas operações lógicas entre valores numéricos inteiros.
Neste caso, as operações lógicas ocorrem no nível de _bits_ dos números,
ou seja, as operações lógicas ocorrem com as representações binárias dos números.

Para realizar uma operação lógica com números inteiros (a nível de bits) com java,
basta utilizarmos os operadores **&**, **|** e **^**.

##Exemplo:

```java
package br.com.dicasdejava.fundamentos;

public class OperacoesBitwise {

	public static void main(String[] args) {
		
		int a = 10;
		int b = 12;

		System.out.println(a + " | " + b + " = " + (a | b));
		System.out.println(a + " & " + b + " = " + (a & b));
		System.out.println(a + " ^ " + b + " = " + (a ^ b));

		a = 9;
		b = 7;

		System.out.println(a + " | " + b + " = " + (a | b));
		System.out.println(a + " & " + b + " = " + (a & b));
		System.out.println(a + " ^ " + b + " = " + (a ^  b));

	}

}
```

Saída:

```
10 | 12 = 14
10 & 12 = 8
10 ^ 12 = 6
9 | 7 = 15
9 & 7 = 1
9 ^ 7 = 14
```

## 10 OU 12

No exemplo acima, nós efetuamos primeiro uma operação lógica **OU** entre os números 10 e 12.
Mas como esta operação acontece no nível binário, primeiro termos que 
[converter os números para binário](http://www.dicasdeprogramacao.com.br/as-10-conversoes-numericas-mais-utilizadas-na-computacao/).

> 10<sub>10</sub> = 1010<sub>2</sub><br />
  12<sub>10</sub> = 1100<sub>2</sub>

Com os números binários em mãos podemos realizar as operações lógicas. Então 10 | 12 ...

```
10 | 12 = 14

1010
1100
----
1110
```

> 1110<sub>2</sub> = 14<sub>10</sub>

Esta operação é como se fosse uma soma (que você aprende no primário),
mas aplicando o operador **OU** ao invês do mais (+).

Da direita para a esquerda...

```
0 OU 0 = 0
1 OU 0 = 1
0 OU 1 = 1
1 OU 1 = 1
```

## 10 E 12

Aplicando o operador **E** aos valores 10 e 12 a nível de bits (binário), temos o seguinte resultado.

```
10 & 12 = 8

1010
1100
----
1000
```

> 1000<sub>2</sub> = 8<sub>10</sub>

A ideia aqui é a mesma, esta operação é como se fosse uma soma (que você aprende no primário),
mas aplicando o operador **E** ao invês do mais (+).

Da direita para a esquerda...

```
0 E 0 = 0
1 E 0 = 0
0 E 1 = 0
1 E 1 = 1
```

## 10 OU-EXCLUSIVO 12

Aplicando o operador **OU-EXCLUSIVO** aos valores 10 e 12 a nível de bits (binário), temos o seguinte resultado.

```
10 ^ 12 = 8

1010
1100
----
0110
```

> 0110<sub>2</sub> = 6<sub>10</sub>

Seguindo o mesmo raciocínio de aplicar o operador lógico no nível binário ...
(Da direita para a esquerda)
```
0 OU-EXCLUSIVO 0 = 0
1 OU-EXCLUSIVO 0 = 1
0 OU-EXCLUSIVO 1 = 1
1 OU-EXCLUSIVO 1 = 0
```

##Operações Bitwise entre 9 e 7
Como um segundo exemplo da aplicação dos operadores bitwise podemos usar os valores 9 e 7.
Vejamos como o Java executa as operações **OU**, **E** e **OU-EXCLUSIVO** entre esses valores:

```
9 | 7 = 15 (OU)

1001 - 9 em binário
0111 - 7 em binário 
----
1111 - 15 em binário

9 & 7 = 1 (E)

1001 - 9 em binário
0111 - 7 em binário 
----
0001 - 1 em binário

9 ^ 7 = 14 (OU-EXCLUSIVO)

1001 - 9 em binário
0111 - 7 em binário 
----
1110 - 14 em binário
```

Referências:

1. [Bitwise and Bit Shift Operators](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/op3.html)
2. [As 10 conversões numéricas mais utilizadas na computação](http://dicasdeprogramacao.com.br/as-10-conversoes-numericas-mais-utilizadas-na-computacao/)
3. [Conheça os operadores lógicos!](http://dicasdeprogramacao.com.br/operadores-logicos/)