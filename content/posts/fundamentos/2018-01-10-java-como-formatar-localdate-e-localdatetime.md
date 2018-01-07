title: Java 8: Como formatar LocalDate e LocalDateTime
date: 2018-01-10
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Java 8, Formatação, java.time
image: /images/logo-java.png

Quando vamos imprimir uma data geralmente queremos que ela seja impressa em um formato específico.

A forma mais simples de formatar ```LocalDate``` e ```LocalDateTime``` é usando a classe ```DateTimeFormatter```.

Veja um exemplo:

```java
package br.com.dicasdejava.fundamentos;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class FormatarLocalDate {

    public static void main(String[] args) {

        //Obtém LocalDate de hoje
        LocalDate hoje = LocalDate.now();

        System.out.println("LocalDate antes de formatar: " + hoje);

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        String hojeFormatado = hoje.format(formatter);

        System.out.println("LocalDate depois de formatar: " + hojeFormatado);

        //Obtém LocalDateTime de agora
        LocalDateTime agora = LocalDateTime.now();

        System.out.println("LocalDateTime antes de formatar: " + agora);

        formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");

        String agoraFormatado = agora.format(formatter);

        System.out.println("LocalDateTime depois de formatar: " + agoraFormatado);

    }

}
```

Saída (No momento em que executo este programa):

```
LocalDate antes de formatar: 2018-01-07
LocalDate depois de formatar: 07/01/2018
LocalDateTime antes de formatar: 2018-01-07T16:11:26.485
LocalDateTime depois de formatar: 07/01/2018 16:11:26
```

## Padrões de formatação

Você deve ter observado que utilizei ```dd/MM/yyyy``` para formatar a data e
```dd/MM/yyyy HH:mm:ss```.
Para escrever estes formatos eu me baseei no
[JavaDoc da classe DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html){:target=\_blank}.

Existem muitas possibilidades de formatação das datas/horas
escrevendo números, palavras (como os meses do ano), abreviações, etc.

Você não precisa saber tudo, claro que é muito bom dar uma boa estudada,
mas vou deixar aqui alguns formatos básicos para você brincar com as formatações de data/hora.
Primeiro o formato normal que todo mundo usa com o mínimo de dois dígitos para cada número,
e quatro dígitos para o ano

- **dd**: dia do mês com mínimo de dois dígitos (01 à 31)
- **MM**: mês do ano com mínimo de dois dígitos (01 à 12)
- **yyyy**: ano com quatro dígitos (exemplo: 2018)
- **HH**: horas com mínimo de dois dígitos (00 à 24)
- **mm**: minutos com mínimo de dois dígitos (00 à 59)
- **ss**: minutos com mínimo de dois dígitos (00 à 59)
- **hh**: horas (até 12) com mínimo de dois dígitos (00 à 12)

Além dos formatos mais comuns citados acima, também pode-se obter variações deles.
Veja:

- **d**: dia do mês com mínimo de um dígito (1 à 31)
- **M**: mês do ano com mínimo de um dígito (1 à 12)
- **yy**: ano com dois dígitos (exemplo: 18)
- **H**: horas com mínimo de um dígito (0 à 24)
- **m**: minutos com mínimo de um dígito (0 à 59)
- **s**: minutos com mínimo de um dígito (0 à 59)
- **h**: horas (até 12) com mínimo de um dígito (0 à 12)

O exemplo abaixo mostra a utilização dos formatos com mínimos de um dígito.

```java
LocalDateTime agora = LocalDateTime.now();

DateTimeFormatter formatter = DateTimeFormatter.ofPattern("d/M/y h:m:s");

String agoraFormatado = agora.format(formatter);

System.out.println("LocalDateTime formatado: " + agoraFormatado);
```

Saída:

```
LocalDateTime formatado: 7/1/2018 4:32:4
```

Com isso você já pode brincar bastante com as formatações de Data/Hora em Java.

## Referências:

1. [JavaDoc: DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html){:target=\_blank}
