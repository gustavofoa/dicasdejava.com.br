---
title: 'Qual a diferença entre File.pathSeparator e File.separator'
date: '2020-09-03'
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: 'File, Java'
image: /images/logo-java.png
---

Em Java, quando você precisa criar o caminho de um arquivo ou pasta,
pode ser que, dependendo do sistema operacional, o caracter que separa as pastas seja uma / (barra inclinada à direita) ou uma \ (barra inclinada a esquerda).

Este é um exemplo de problema comum para sistemas que funcionam em qualquer sistema operacional.

Pensa comigo, se você vai construir o caminho de uma pasta no Windows, pode paracer com algo assim:

```
C:\Users\Gustavo\arquivo.txt
```

Já no Linux ou no MacOS, o a "contra-barra" não existe para formar caminhos de arquivos.
Neste caso seria algo assim:

```
/home/Gustavo/arquivo.txt
```

Você percebeu que a barra que separa as pastas no Windows é diferente da barra do Linux?
No Windows a barra é assim \ e no Linux é assim /.

Para você deixar isto transparente no seu programa java, você pode fazer uso da constante `separator`
que existe na class `File`.

Desta forma, se você construir um caminho para um arquivo ou pasta utilizando a constante `File.separator`, você fica independente ao sistema operacional.

Por exemplo...

```java
import java.io.File;

public class FileSeparator {
    public static void main(String []a){

        String caminhoDoArquivo = "Usuario" + File.separator + "gustavo" + File.separator + "arquivo.txt";

        System.out.println(caminhoDoArquivo);

    }
}
```

Se executarmos este programa Java no Linux, a resposta seria esta:

```
Usuario/gustavo/arquivo.txt
```

Se executarmos este programa Java no Windows, a resposta seria esta:

```
Usuario\gustavo\arquivo.txt
```

Agora sabemos como deixar o nosso software independente de sistema operacional.
Basta usar o `File.separator` para separar as pastas do caminho do seu arquivo.

Mas **qual é a diferença entre o `File.separator` e o `File.pathSeparator`**?

Já aprendemos que o `File.separator` separa as pastas de um caminho (*path*).

Já o `File.pathSeparator`, faz sentido no contexto de separar "caminhos completos".

Pra entender direito onde ele se aplica é importante entender sobre variáveis de ambiente do seu sistema operacional.

No post sobre [Como instalar o Maven no Windows](https://dicasdejava.com.br/como-instalar-o-maven-no-windows/), eu explico detalhadamente como configurar variáveis de ambiente no Windows.

Mas se você for um pouco mais atento, vai perceber que podemos configurar mais de um caminho (_path_) para um determinada variável de ambiente. E como estes caminhos são separados na variável?

A resposta é: Depende do Sistema Operacional. (De novo!)

No Windows, o caracter que separa os "Paths" em uma variável de ambiente é o `;`, já no Linux e no MacOS é o `:`.

Por exemplo, se você abrir o prompt de comando do Windows e digitar `echo %PATH%`, você verá vários caminhos sendo aprensentados na linha de comando, este é o conteúdo da variável de ambiente chamada `PATH`.

No meu caso, apareceu este conteúdo aqui:

![Conteúdo da variável de ambiente PATH no Windows, mostrando a separação dos caminhos usando o ponto-e-virgula](/images/conteudo-da-variavel-de-ambiente-path.png){:style="max-width:100%; padding:10px;"}

Mas se você executar um comando para verificar o conteúdo da variável de ambiente `PATH` no linux, verá que o caracter que separa os caminhos é o `:` (dois-pontos).

Veja abaixo.

![Conteúdo da variável de ambiente PATH no Linux, mostrando a separação dos caminhos usando o dois-pontos](/images/conteudo-da-variavel-de-ambiente-path-no-linux.png){:style="max-width:100%; padding:10px;"}


Acho que deu pra você perceber que a separação de "Paths" (Caminhos) utiliza caracateres diferentes dependendo do sistema operacional.

E é exatamente isso que o `File.pathSeparator` resolve!

Dependendo do SO em que você está executando o seu programa java, ele vai ter um valor diferente para esta constante.

Vamos ver no exemplo abaixo.

```java
import java.io.File;

public class FilePathSeparator {
    public static void main(String []a){

        String caminhoDoArquivo1 = "Usuario" + File.separator + "gustavo" + File.separator + "arquivo1.txt";
        String caminhoDoArquivo2 = "Usuario" + File.separator + "gustavo" + File.separator + "arquivo2.txt";

        System.out.println(caminhoDoArquivo1 + File.pathSeparator + caminhoDoArquivo2);

    }
}
```

Se executarmos este programa Java no Linux, a resposta seria esta:

```
Usuario/gustavo/arquivo1.txt:Usuario/gustavo/arquivo2.txt
```

Se executarmos este programa Java no Windows, a resposta seria esta:

```
Usuario\gustavo\arquivo1.txt;Usuario\gustavo\arquivo2.txt
```

Agora você já sabe qual a diferença entre o `File.separator` e o `File.pathSeparator`,
bem como a importância de usá-los no momento correto, pois isso pode determinar se o
código que você está desenvolvendo será Multi-plataforma ou não.

Qualquer dúvida, deixe nos comentários aqui abaixo.


## Referências

1. [Javadoc: File.separator](https://docs.oracle.com/javase/7/docs/api/java/io/File.html#separator){:target=_blank}
2. [Javadoc: File.pathSeparator](https://docs.oracle.com/javase/7/docs/api/java/io/File.html#pathSeparator){:target=_blank}
