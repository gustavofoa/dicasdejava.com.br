---
title: 'Java: Implementando métodos na interface com Default Methods!'
date: '2017-07-10'
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Interface, Default Method, Java Básico
image: /images/logo-java.png
---

Aprendi desde o início da minha carreira que uma _interface_ em Orientação a Objetos
apenas define os métodos que devem ser implementados pelas classes.
Ou seja, não poderíamos implementar um método em uma classe.

Mas isso mudou e a partir do **Java 8** nós podemos ter implementação "padrão" de um método
na interface Java! Para isso, basta utilizarmos a palavra-chave `default` na declaração do método.

É importante observar que os métodos _default_ não foram criados com o objetivo de permitir herança multipla,
e sim de permitir a evolução de interfaces sem quebrar códigos existentes.
Essa recurso do **Java 8** é o que possibilitou o _Lambda_!

Vejamos um exemplo da implementação padrão de um método em uma interface.

```java
package br.com.dicasdejava.fundamentos;

interface InterfaceComDefaultMethod {

	default String metodo() {
		return "a";
	}

	String metodo2();

}

class Classe implements InterfaceComDefaultMethod {

	public String metodo2() {
		return "b";
	}

}

class Main {

	public static void main(String... args) {
		InterfaceComDefaultMethod a = new Classe();
		System.out.println(a.metodo());
		System.out.println(a.metodo2());
	}

}
```

Saída:

```
a
b
```

O arquivo Java acima exemplifica a utilização de um _"default method"_ em Java.

Podemos observar que o método que foi implementado na interface, 
necessariamente utilizando a palavra-chave `default`,
não precisa ser implementado na `Classe` que "implementa" a interface `InterfaceComDefaultMethod`.

##TEM que ter a palavra chave **default**

Para utilizarmos esse recurso do **Java 8** e implementar um método na própria interface,
precisamos utilizar a palavra-chave `default` na declaração do método que terá a implementação padrão.
Conforme o exemplo abaixo.

```java
default String metodo() {
	return "a";
}
```

Referências:

1. [Doc: Default Methods](https://docs.oracle.com/javase/tutorial/java/IandI/defaultmethods.html){:target=\_blank}
