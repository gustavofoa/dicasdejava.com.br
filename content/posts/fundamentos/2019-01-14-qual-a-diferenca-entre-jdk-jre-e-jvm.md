title: Qual a diferença entre JDK, JRE e JVM
date: 2019-01-14
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: JDK, JRE, JVM
image: /images/logo-java.png

Uma grande confusão que paira sobre quem está começando a aprender sobre o mundo Java é
**a diferença entre JDK, JRE e JVM**.
Neste post você vai entender, de uma vez por todas, a diferença entre essas três siglas
e o porquê é importante saber para que serve cada um.

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

- **JDK - Compilar código-fonte (.java) em _bytecode_ (.class)**
- **JVM - Executa o _bytecode_ (.class)**
- **JRE - Fornece as bibliotecas padrões do Java para o JDK compilar o seu código e para a JVM executar o seu programa.**

Se você quiser já pode parar de ler o post por aqui, pois você já entendeu o básico sobre essas três siglas e como o Java funciona.

Mas agora vamos aprofundar um pouquinho mais sobre como o Java está organizado
e porquê você também pode executar programas na JVM que não foram escritos na linguagem Java, como Scala, JRuby, Jython, Clojure, Groovy, etc..

## Referências:

1. [Javadoc: java.lang.String](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html){:target=\_blank}
