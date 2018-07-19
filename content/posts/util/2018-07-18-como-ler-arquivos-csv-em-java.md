title: Como ler arquivos CSV em java
date: 2018-07-18
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: CSV, IO
image: /images/logo-java.png

Existem várias formas de ler arquivos CSV em Java. A forma mais "raiz" é lendo o arquivo e fazendo Split, por espaço, vírgula ou ponto-e-vírgula, mas pra quê reinventar a roda né? Tem bibliotecas open-source que fazem todo o trabalho pra gente.

Neste post vamos ver como ler arquivos CSV em java com a biblioteca open-source **OpenCSV**.

[>> Como escrever arquivos CSV em java](https://dicasdejava.com.br/como-escrever-arquivos-csv-em-java/)

##CSV de exemplo

Para os exemplos destes post, vamos usar um CSV simples.
Considere que o arquivo `pessoas.csv` esteja em algum lugar acessível pela sua classe, ou seja no `classpath`, e tenha este conteúdo:

```
nome,idade,email
Gustavo,28,gustavo@dicasdeprogramcao.com.br
Joao,35,joao@dicasdejava.com.br
Maria,23,maria@dicasdeprogramacao.com.br
Ana,25,ana@dicasdejava.com.br
```

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

### Lendo CSV como uma lista de String[]

Uma forma simples de ler um CSV é como uma lista de arrays de String, ou seja: `List<String[]>`.
Veja no código abaixo como fazer isso com o **OpenCSV**.

```java
package br.com.dicasdejava.util.csv;

import com.opencsv.CSVReader;
import com.opencsv.CSVReaderBuilder;

import java.io.IOException;
import java.io.Reader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class LerLinhasOpenCsv {

    public static void main(String[] args) throws IOException {

        Reader reader = Files.newBufferedReader(Paths.get("pessoas.csv"));
        CSVReader csvReader = new CSVReaderBuilder(reader).withSkipLines(1).build();

        List<String[]> pessoas = csvReader.readAll();
        for (String[] pessoa : pessoas)
            System.out.println("Name : " + pessoa[0] +
                            " - Idade : " + pessoa[1] +
                            " - Email : " + pessoa[2]);

    }

}

```

Saída:

```
Name : Gustavo - Idade : 28 - Email : gustavo@dicasdeprogramcao.com.br
Name : Joao - Idade : 35 - Email : joao@dicasdejava.com.br
Name : Maria - Idade : 23 - Email : maria@dicasdeprogramacao.com.br
Name : Ana - Idade : 25 - Email : ana@dicasdejava.com.br
```

### Lendo CSV como um objeto

Outra forma interessante de ler um CSV é obter uma lista de Objetos de uma Classe que representa um registro do csv.

Para isto, vamos criar a classe CsvPessoa com os atributos contidos no CSV.

É importante que os nomes dos atributos sejam iguais as colunas do CSV.

```java
package br.com.dicasdejava.csv;

public class CsvPessoa {
    private String nome;
    private Integer idade;
    private String email;

    // Gets e Sets omitidos para ficar menor

    public String toString() {
        return "CsvPessoa{nome='" + nome + "\', idade=" + idade + ", email='" + email + "\'}";
    }
}
```

Agora vamos ler o CSV e obter uma lista de pessoas, ou seja: `List<Pessoa>`

```java
package br.com.dicasdejava.csv;

import br.com.dicasdejava.model.CsvPessoa;
import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;

import java.io.IOException;
import java.io.Reader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class LerLinhasComoObjetosOpenCsv {

    public static void main(String[] args) throws IOException {

        Reader reader = Files.newBufferedReader(Paths.get("pessoas.csv"));

        CsvToBean<CsvPessoa> csvToBean = new CsvToBeanBuilder(reader)
                .withType(CsvPessoa.class)
                .build();

        List<CsvPessoa> pessoas = csvToBean.parse();

        for (CsvPessoa pessoa : pessoas)
            System.out.println(pessoa);

    }

}
```

Saída:

```
CsvPessoa{nome='Gustavo', idade=28, email='gustavo@dicasdeprogramcao.com.br'}
CsvPessoa{nome='Joao', idade=35, email='joao@dicasdejava.com.br'}
CsvPessoa{nome='Maria', idade=23, email='maria@dicasdeprogramacao.com.br'}
CsvPessoa{nome='Ana', idade=25, email='ana@dicasdejava.com.br'}
```

## Referências:

1. [OpenCSV](http://opencsv.sourceforge.net/){:target=\_blank}
2. [Códigos-fonte deste post](https://github.com/gustavofoa/examples.dicasdejava.com.br/tree/master/src/main/java/br/com/dicasdejava/util/csv){:target=\_blank}