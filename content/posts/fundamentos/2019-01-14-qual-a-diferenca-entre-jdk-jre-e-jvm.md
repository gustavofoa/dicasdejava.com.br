title: Qual a diferença entre JDK, JRE e JVM
date: 2019-01-14
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: JDK, JRE, JVM
image: /images/logo-java.png

Uma grande confusão que paira sobre quem está começando a aprender sobre o mundo Java é
**a diferença entre JDK, JRE e JVM**.
Neste post você vai entender, de uma vez por todas, a diferença entre essas três siglas
e porque é importante saber para que serve cada um.

A primeira coisa que você precisa saber é que o Java é muito conhecido por trazer o conceito de multi-plataforma.
Na verdade esse é o motivo do grande sucesso do Java à mais de vinte anos!
O famoso [**WORA**](https://pt.wikipedia.org/wiki/WORA){:target=\_blank} (_Write once, run anywhere._),
ou em bom português: "_Escreva uma vez, execute em qualquer lugar_".

Na prática, só de entender esse conceito e como o Java faz para tornar possível
escrever um único código e executá-lo em qualquer sistema operacional,
você já vai perceber, por alto, a diferença entre JDK, JRE e JVM e onde cada um se encaixa.

O fluxo é basicamente o seguinte:

1. Você escreve o seu código-fonte (arquivo com a extensão .java).
2. Você utiliza o JDK para compilar o seu código-fonte e gerar o arquivo _bytecode_ (arquivo com a extensão .class).
3. Para executar o seu programa, a JVM lê o seu arquivo compilado (.class) e as bibliotecas padrões do Java que estão no JRE.
4. Pronto, seu programa está rodando e todo mundo está feliz! :)

Então, a grosso modo, já deu pra perceber pra quê serve cada um:

- **JDK (Java Development Kit) - é o Kit de Desenvolvimento Java responsável por compilar código-fonte (.java) em _bytecode_ (.class)**
- **JVM (Java Virtual Machine) - é a Máquina Virtual do Java reponsável por executar o _bytecode_ (.class)**
- **JRE (Java Runtime Environment) - Ambiente de Execução do Java que fornece as bibliotecas padrões do Java para o JDK compilar o seu código e para a JVM executar o seu programa.**

Este é o básico que você precisa saber sobre essas três siglas e como o Java funciona.

Mas estes 3 componentes têm um certo relacionamento entre eles.
Vamos nos aprofundar um pouco mais o entendimento de cada um e como eles se relacionam entre sí para possibilitar a "mágica" do mundo Java.

## JVM - Máquina Virtual do Java

Já vimos que a JVM é a responsavel por executar os programas no formato _bytecode_, certo?
Mas a JVM não é só isso, ela é na verdade o coração do Java,
reponsável por fornecer a tal capacidade de multi-plataforma.

Isso porque depois que você instala a JVM no sistema operacional (Windows, Linux, Mac, etc.),
Ela é capaz de interpretar e executar o programa compilado em formato _bytecode_
em qualquer um desses SOs.

Um coisa legal de perceber aqui é que a JVM executa um programa _bytecode_,
mesmo que este programa _bytecode_ não tenha sido escrito em Java necessariamente.

Isso mesmo! Você não precisa programar na linguagem java, para executar um programa na JVM.
Você pode criar seus programas em outras linguagens que também geram arquivos _bytecode_.
Existem várias delas, alguns exemplos são: Scala, JRuby, Jython, Clojure, Groovy, etc..

Outro ponto importante é que a **JVM** é, na verdade, uma especificação.
Isso significa que uma JVM pode ser desenvolvida por qualquer organização,
desde que sigam as especificações para a Java Virtual Machine.

## JRE - Ambiente de Execução Java

O JRE provê os requisitos mínimos para executar um programa java.
Ele contém uma JVM, os pacotes básicos do Java (API core),
por exemplo o pacote lang que tem a classe `String`.

Por fim o JRE também provê ferramentas para executar os programas java.
Uma delas é o executável `java.exe`, que é utilizado para executar uma classe java
que contém um método `main(String args[])`.

Agora você já sabe que quando você executa o comando `java SuaClasse`,
é o JRE que provê esse programa `java.exe` que você está usando.

## JDK - Kit de Desenvolvimento Java

O JDK é Kit que provê ferramentas para o desenvolvimento de programas Java.
Ou seja, ele contém um compilador, um depurador e o próprio JRE para você executar os seus programas.

É o JDK que nos provê o programa `javac.exe`, que compila códigos `.java` em _bytecodes_ `.class`.

Agora você já sabe q eu quando você executa o comando `javac SuaClasse.java`,
é o JDK que provê esse programa `javac.exe` que você está usando.

## Uma visão geral

Agora que você já sabe um pouco mais sobre JDK, JRE e JVM,
você já deve ter percebido que a JDK traz também um JRE,
e o JRE, por sua vez, traz também uma implementação da JVM.

A imagem abaixo ilustra a relação entre esses componentes.

![JDK, JRE e JVM](/images/jdk_jre_jvm.png){:style="width: 100%; padding: 10px;"}

Espero que este post tenha sido esclarecedor para você
e que tenha contribuído um pouco com o seu aprendizado.

Se tiver alguma dúvida, fique à vontade para postar aí nos comentários!

## Referências:

1. [Java.com: TechInfo](https://www.java.com/pt_BR/download/faq/techinfo.xml){:target=\_blank}
