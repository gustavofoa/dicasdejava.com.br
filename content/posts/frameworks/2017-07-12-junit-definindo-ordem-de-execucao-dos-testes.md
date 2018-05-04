title: Junit: Como definir a ordem de execução dos testes!
date: 2017-07-12
author: Gustavo Furtado de Oliveira Alves
category: Frameworks
tags: Junit
image: /images/logo-junit.png

Você sabia que podemos definir uma ordem de execução dos testes do JUnit?

Sabemos que os testes de unidade não devem ter dependências entre si
e devem ser capazes de executar em qualquer ordem,
mas a partir da **versão 4.11 do Junit**, nós podemos especificar um padrão
de ordenação a ser seguido na execução dos testes.

Não sei pra quê você precisaria disso, mas se quiser ordenar a execução dos testes 
do Junit confira abaixo como fazer.

Para determinar a ordem de execução dos testes, 
basta anotar a classe de testes com a anotação `@FixMethodOrder`.

Esta anotação recebe como parâmetro o enum `MethodSorters`,
que podem assumir os valores `DEFAULT`, `JVM` e `NAME_ASCENDING`.

O valor `JVM` diz que vamos seguir a ordem que a JVM determinar
e isso significa uma ordem mais ou menos _aleatória_, depende da JVM.

O valor `DEFAULT` deixa a ordenação sob responsabilidade do próprio JUnit.
Entretanto na própria [_release notes da versão 4.11_](https://github.com/junit-team/junit4/blob/master/doc/ReleaseNotes4.11.md#test-execution-order)
eles não se comprometem a seguir uma ordem específica.

Portanto, se quizermos controlar a ordem de execução dos testes,
nós devemos usar o valor `NAME_ASCENDING` do enum `MethodSorders`.

Veja no exemplo abaixo que, alfabeticamente, o segundo teste deve ser executado primeiro.
Como colocamos a anotação `@FixMethodOrder(MethodSorters.NAME_ASCENDING)` na classe,
o primeiro teste executado é o segundo, seguindo a ordem alfabética do nome do teste.

```java
package br.com.dicasdejava.junit;

import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class OrdemJunitTest {

	@Test
	public void test2() {
		System.out.println("Segundo teste");
	}

	@Test
	public void test1() {
		System.out.println("Primeiro teste");
	}

}
```

Saída:

```
Primeiro teste
Segundo teste
```

Agora, removendo a anotação `@FixMethodOrder(MethodSorters.NAME_ASCENDING)`,
o resultado seguiu a ordem de criação dos testes no código-fonte.

Mas isso não significa que sempre seria assim.
O Junit que recebeu a responsabilidade de ordenar e não sabemos
que regra ele segue, ou irá seguir futuramente.

```java
package br.com.dicasdejava.junit;

import org.junit.Test;

public class OrdemJunitTest {

	@Test
	public void test2() {
		System.out.println("Segundo teste");
	}

	@Test
	public void test1() {
		System.out.println("Primeiro teste");
	}

}
```

Saída:

```
Segundo teste
Primeiro teste
```

##Maven

Se precisar do xml de dependência do **Junit 4.11**, aqui está:

```
<dependency>
	<groupId>junit</groupId>
	<artifactId>junit</artifactId>
	<version>4.11</version>
	<scope>test</scope>
</dependency>
```


##Referencias

1. [JavaDoc: FixMethodOrder](http://junit.org/junit4/javadoc/4.12/org/junit/FixMethodOrder.html){:target=\_blank}
2. [JavaDoc: MethodSorters](http://junit.org/junit4/javadoc/4.12/org/junit/runners/MethodSorters.html){:target=\_blank}
3. [Release notes: Junit 3.11](https://github.com/junit-team/junit4/blob/master/doc/ReleaseNotes4.11.md#test-execution-order){:target=\_blank}
