title: Java: Como ler variável de ambiente
date: 2018-08-23
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: System
image: /images/logo-java.png

Ler uma variável de ambiente é muito simples com Java.
Basta chamar o método `System.getenv(String)` informando o nome da variável de ambiente como parâmetro.

Veja o código abaixo:

```java
public class LerVariavelDeAmbiente {
    public static void main(String[] args) {
        
        String variavelDeAmbiente = System.getenv("JAVA_HOME");

        System.out.println(variavelDeAmbiente);

    }
}
```

Saída:

```
C:\Program Files\Java\jdk1.8.0_161
```

**Importante!** A variável de ambiente `JAVA_HOME` já estava configurada na minha máquina no momento da execução.

Você pode consultar o valor de qualquer variável de ambiente do seu sistema operacional.

## Exemplo de execução

![Como ler variável de ambiente com Java](/images/ler-variavel-de-ambiente.gif){:style="width:100%; padding:10px;"}

## Referência

1. [API: java.lang.System](https://docs.oracle.com/javase/8/docs/api/java/lang/System.html){:target=\_blank}