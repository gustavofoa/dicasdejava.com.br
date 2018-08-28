title: Como instalar o MAVEN no Windows
date: 2018-08-28
author: Gustavo Furtado de Oliveira Alves
category: Ferramentas
tags: instalar, maven, windows
image: /images/logo-maven.png

O **maven** é um dos principais gerenciadores de dependências conhecidos para Java.
Mas este nome pode assustar um pouco os iniciantes no desenvolvimento Java
e a primeira dúvida que surge para começar a usá-lo é **como eu instalo o maven**.

Como não tem um "instalador" normal pra você executar e ir clicando em "Próximo",
a instalação do maven pode gerar um pouco de confusão, mas é bem simples.

## Primeiro passo - Pré-requisito (JDK 1.7)

O principal requisito para instalar e usar o **maven** na sua máquina é ter previamente instalado
o JDK (Java Development Kit) 1.7 ou superior.

Também é necessário configurar a variável de ambiente `JAVA_HOME` no seu computador.
Mas isso eu vou mostrar como fazer ao longo do post.

Por agora tenha certeza que você tenha instalado o JDK 1.7 ou superior.

## Segundo passo - Download do maven

O próximo passo é baixar o maven compactado em sua versão mais atual.
Você precisa baixar o arquivo com os binários do maven, não é necessário baixar o arquivos-fonte.
Ou seja, você vai baixar o arquivo que termina com `-bin` e não o arquivo que termina com `-src`.

Para baixar o maven, basta [clicar aqui](https://maven.apache.org/download.cgi) e fazer o download.

Você pode escolher qualquer formato de compactação para download, mas eu sugiro o arquivo `-bin.zip`,
por ser o formato de compactação mais comum.

Veja um exemplo da página de download do maven.

![Página de download do maven](/images/maven/download-maven.png){:width=100%}

## Terceiro passo - Descompactação

Após fazer o download do arquivo compactado, você deve descompactá-lo em uma pasta de sua preferência.

Mas é importante você saber que esta pasta será a pasta onde o maven estará "instaldo".

Eu vou descompactar o maven em `C:\maven`. Ao final da descompactação a pasta do maven estará assim:

![Pasta do maven localmente](/images/maven/pasta-do-maven.png){:width=100%}

Pode ser que quando você descompactou o arquivo zip a pasta `C:\maven` tenha ficado só uma pasta com os arquivo do maven dentro, algo como `C:\maven\apache-maven-3.5.4`.

Não tem problema, basta se lembrar disso quando for configurar a variável de ambiente. Ou você pode copiar os arquivos de dentro desta pasta e subir um nível, colocando em `C:\maven`. Você escolhe ...

## Quarto passo - Configurando as variáveis de ambiente

Agora vem a parte que faz o maven funcionar :)

Para fazer o maven funcionar você só precisa adicionar a pasta `bin` do maven na variável de ambiente `PATH`.

Se você nunca configurou uma variável de ambiente no Windows basta seguir esses passos.

### 1. Clique com o botão direito do mouse no ícone do seu computador e clique em **Propriedades**.

![menu: propriedades do computador](/images/maven/meu-computador-propriedades.png){:width=100%}

### 2. Clique em **Configurações avançadas do sistema**.

![Configurações avançadas do sistema](/images/maven/configuracoes-avancadas-do-sistema.png){:width=100%}

### 3. Clique no botão **Variáveis de ambiente**.

![Configurações avançadas do sistema](/images/maven/botao-variaveis-de-ambiente.png){:width=100%}

### 4. Selecione a variável de ambiente **PATH** e clique em **Editar**.

![Editar variável de ambiente PATH](/images/maven/edicao-variavel-de-ambiente-PATH.png){:width=100%}

### 5. Clique no botão **Novo** e adicione o caminho da pasta bin do maven: `C:\maven\bin`.

![Adicionando a pasta bin do maven na variável de ambiente PATH](/images/maven/adiciona-maven-bin-no-PATH.png){:width=100%}

### 6. Verificar se existe a variável de ambiente **JAVA_HOME**.

Lembra que falei da variável de ambiente **JAVA_HOME**?
Precisamos saber se ela já existe no seu sistema ou se precisamos criar.

Entre as variáveis de ambiente do seu sistema, verifique se já existe uma variável de ambiente chamada **JAVA_HOME** que contenha o caminho para o JDK instalado no seu computador.

Se não existir, você precisa criar essa nova variável de ambiente, clicando em **Novo...**
e informando o nome `JAVA_HOME` e o valor com o caminho para a pasta onde o seu JDK está instalado.
Por exemplo:

![Exemplo de configuração do JAVA_HOME](/images/maven/exemplo-java-home.png){:width=100%}

## Testando a instalação do maven

Para testar se a configuração do maven funcionou, abra o prompt de comando do seu computador e digite `mvn`.

A saída deve ser algo assim:

![Resultado do comando mvn](/images/maven/saida-do-comando-mvn.png){:width=100%}

Se o resultado do seu comando foi como a imagem abaixo, significa que você não configurou a variável de ambiente `PATH` com o caminho válido para a pasta `bin` do maven.

![mvn comando não encontrado](/images/maven/mvn-comando-nao-encontrado.png){:width=100%}

Neste caso, volte para o início deste **Quarto passo - Configurando as variáveis de ambiente**.

## Referencias

1. [Maven: Home](https://maven.apache.org/){:target=\_blank}
2. [Maven: Instalação](https://maven.apache.org/install.html){:target=\_blank}
3. [Maven: Download](https://maven.apache.org/download.cgi){:target=\_blank}
