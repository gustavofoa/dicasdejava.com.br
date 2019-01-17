title: Java: Como instanciar uma classe abstrata ou interface
date: 2018-08-27
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Java, classe abstrata, interface
image: /images/logo-java.png

Logo de cara você já deve estar pensando: para de falar besteira cara! Não dá pra instanciar nem classe abstrata nem interface em java!

Pois bem, se você sempre achou que era impossível instanciar uma classe abstrata, ou até mesmo uma interface, você está enganado.

**É possível sim, instanciar uma classe abstrata ou uma interface!**

O único requisito pra isso é, adivinha ... implementar todos os métodos abstratos. E você pode fazer isso sem declarar uma nova classe explicitamente.
O que você precisa é de uma **classe anônima**!

## Classe anônima

Casse anônima é uma classe que não é declarada explicitamente no código.

Elas possibilitam a você declarar e instanciar uma classe ao mesmo tempo.
Você não precisa nem mesmo dar um nome para a classe que você está criando.

Veja no código abaixo.

```java

abstract class ClasseAbstrata {
    public abstract void metodoAbstrato();
}

public class Principal {
    public static void main(String args[]){

        ClasseAbstrata objeto = new ClasseAbstrata(){
            public void metodoAbstrato(){
                System.out.println("Olá mundo!");
            }
        };

        objeto.metodoAbstrato();

    }
}

```

Veja abaixo um exemplo de excução deste código:

![Como instanciar uma classe abstrata como classe anônima](/images/instanciar-classe-abstrata.gif){:style="width:100%; padding:10px;"}


## Referências

1. [Doc: Anonymous classes](https://docs.oracle.com/javase/tutorial/java/javaOO/anonymousclasses.html){:target=\_blank}