---
title: 'Como escrever arquivos CSV em java'
date: '2018-07-19'
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: CSV, IO
image: /images/logo-java.png
---

Existem várias formas de escrever arquivos CSV em Java.
Neste post vamos ver como criar arquivos CSV em java com o auxílio da biblioteca open-source **OpenCSV**.

[>> Como ler arquivos CSV em java](https://dicasdejava.com.br/como-ler-arquivos-csv-em-java/){:target=\_blank}

## OpenCSV como dependência (maven)

Para utilizar o **OpenCSV** você precisa importá-lo como dependência no seu projeto.
Se você estiver utilizando o _Maven_, basta adicionar a seguinte dependência no seu arquivo `pom.xml`.

```xml
<dependency>
    <groupId>com.opencsv</groupId>
    <artifactId>opencsv</artifactId>
    <version>4.2</version>
</dependency>
```

### Escrevendo CSV como uma lista de String[]

Uma situação simples é quando você tem uma lista de arrays de String, ou seja `List<String[]>`,
e quer escrever esses arrays como registros de um csv.
Veja no código abaixo como fazer isso com o **OpenCSV**.

```java
package br.com.dicasdejava.util.csv;

import com.opencsv.CSVWriter;

import java.io.IOException;
import java.io.Writer;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class CriarCsvComStringsOpenCsv {

    public static void main(String[] args) throws IOException {

        String[] cabecalho = {"nome", "idade", "telefone"};

        List<String[]> linhas = new ArrayList<>();
        linhas.add(new String[]{"Joao","35","joao@dicasdejava.com.br"});
        linhas.add(new String[]{"Maria","23","maria@dicasdeprogramacao.com.br"});
        linhas.add(new String[]{"Ana","25","ana@dicasdejava.com.br"});

        Writer writer = Files.newBufferedWriter(Paths.get("pessoas.csv"));
        CSVWriter csvWriter = new CSVWriter(writer);

        csvWriter.writeNext(cabecalho);
        csvWriter.writeAll(linhas);

        csvWriter.flush();
        writer.close();

    }

}
```

### Escrevendo CSV como um objeto

Outra forma interessante de criar um CSV é quando você tem uma lista de objetos de uma Classe que deve representar uma linha no csv.

Para isto, vamos criar como exemplo a classe CsvPessoa com os atributos contidos no CSV.


```java
package br.com.dicasdejava.csv;

public class CsvPessoa {
    private String nome;
    private Integer idade;
    private String email;

    public CsvPessoa(String nome, Integer idade, String email) {
        this.nome = nome;
        this.idade = idade;
        this.email = email;
    }

    // Gets e Sets omitidos para ficar menor

}
```

Agora vamos escrever o CSV com uma lista de pessoas, ou seja `List<CsvPessoa>`.

```java
package br.com.dicasdejava.util.csv;

import com.opencsv.bean.StatefulBeanToCsv;
import com.opencsv.bean.StatefulBeanToCsvBuilder;
import com.opencsv.exceptions.CsvDataTypeMismatchException;
import com.opencsv.exceptions.CsvRequiredFieldEmptyException;

import java.io.IOException;
import java.io.Writer;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class CriarCsvComObjetosOpenCsv {

    public static void main(String[] args) throws IOException, CsvDataTypeMismatchException, CsvRequiredFieldEmptyException {

        List<CsvPessoa> pessoas = new ArrayList<>();
        pessoas.add(new CsvPessoa("Joao",35,"joao@dicasdejava.com.br"));
        pessoas.add(new CsvPessoa("Maria",23,"maria@dicasdeprogramacao.com.br"));
        pessoas.add(new CsvPessoa("Ana",25,"ana@dicasdejava.com.br"));

        Writer writer = Files.newBufferedWriter(Paths.get("pessoas.csv"));
        StatefulBeanToCsv<CsvPessoa> beanToCsv = new StatefulBeanToCsvBuilder(writer).build();

        beanToCsv.write(pessoas);

        writer.flush();
        writer.close();

    }

}
```

A Saída dos dois programas acima é um arquivo `pessoas.csv` com o conteúdo abaixo:

```
email,idade,nome
joao@dicasdejava.com.br,35,Joao
maria@dicasdeprogramacao.com.br,23,Maria
ana@dicasdejava.com.br,25,Ana
```

## Referências:

1. [OpenCSV](http://opencsv.sourceforge.net/){:target=\_blank}
2. [Códigos-fonte deste post](https://github.com/gustavofoa/examples.dicasdejava.com.br/tree/master/src/main/java/br/com/dicasdejava/util/csv){:target=\_blank}