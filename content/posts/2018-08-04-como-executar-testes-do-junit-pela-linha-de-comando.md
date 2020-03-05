---
title: Como executar testes do jUnit pela linha de comando
date: '2018-08-04'
author: Gustavo Furtado de Oliveira Alves
category: Frameworks
tags: Junit
image: /images/logo-junit.png
---

A forma mais comum de executar os testes do Junit pela linha de comando é utilizando o maven, com o seguinte comando.

```
mvn test
```

Mas e se você não estiver utilizando o maven, como executar os testes do jUnit pela linha de comandos?

Vamos ver como fazer isso com o exemplo abaixo.

Primeiro criamos a classe de exemplo que será testada no arquivo `ClasseASerTestada.java`.

```java
public class ClasseASerTestada {

    public String metodoASerTestado(){
        return "teste";
    }

}
```

Agora a classe que tem o teste do junit no arquivo `ClasseDeTeste.java`.

```java
import static org.junit.Assert.*;

import org.junit.Test;

public class ClasseDeTeste {

    @Test
    public void teste(){
        ClasseASerTestada obj = new ClasseASerTestada();
        String retornoDoMetodo = obj.metodoASerTestado();
        assertEquals("teste", retornoDoMetodo);
    }

}
```

## Download dos jars do jUnit

Para utilizar as classes do jUnit, nós precisamos colocar os jars do junit no classpath.
Neste exemplo vamos colocar os jars do jUnit na própria pasta onde estão os nossos arquivos `.java`. Você pode baixar os arquivos .jar do jUnit [aqui](https://github.com/junit-team/junit4/wiki/Download-and-Install){:target=\_blank}.

[![Download dos jars do Junit](/images/junit-download-jars.png){:style="width:100%; padding:10px;"}](https://github.com/junit-team/junit4/wiki/Download-and-Install){:target=\_blank}

Agora temos os seguintes arquivos na nossa pasta.

![Duas classes e os arquivos jar na pasta](/images/classes-e-arquivos-jar.png){:style="width:100%; padding:10px;"}

## Compilação

O próximo passo é compilar as nossas duas classes, especificando os arquivos .jar do jUnit no classpath.

Primeiro compilamos a classe `ClasseASerTestada.java` com o seguinte comando:

```
javac ClasseASerTestada.java
```

Pronto. Em seguinda vamos compilar a classe que tem o teste do jUnit, desta vez precisamos expecificar o arquivo jar do jUnit no classpath no comando:

```
javac -cp junit-4.12.jar;. ClasseDeTeste.java
```

Perceba que para compilar precisamos especificar o classpath com o parâmetro `-cp`.
Informamos que o classpath é o arquivo junit-4.12.jar e a pasta atual: `junit-4.12.jar;.`.

Se você estiver no linux, troque o `;` por `:`.

## Execução do jUnit via linha de comando

Agora que já compilamos nossas classes, podemos executar os nossos testes do jUnit com o comando abaixo.

```
java -cp junit-4.12.jar;hamcrest-core-1.3.jar;. org.junit.runner.JUnitCore ClasseDeTeste
```

Duas coisas importantes a serem observadas neste comando.

1. Nosso classpath é composto por dois jars (`junit-4.12.jar;hamcrest-core-1.3.jar`) e as classes que estão na pasta local (`.`).
2. Com o comando `java` nós executamos a classe `org.junit.runner.JUnitCore`, passando o nome da nossa classe de Teste `ClasseDeTeste` como parâmetro.

O resultado deste comando é esse:

```
JUnit version 4.12
.
Time: 0,003

OK (1 test)
```

Ou seja, o jUnit executou o nosso teste. ;)

Dúvidas nos comentários...

## Referências

1. [Download do Junit](https://github.com/junit-team/junit4/wiki/Download-and-Install){:target=\_blank}
2. [Código fonte utilizado](https://github.com/gustavofoa/dicasdejava.com.br/tree/master/content/examples/junit-linha-de-comando/){:target=\_blank}