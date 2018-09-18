title: Como configurar o lombok no IntelliJ IDEA
date: 2018-09-18
author: Gustavo Furtado de Oliveira Alves
category: Ferramentas
tags: instalar, lombok, Intellij IDEA
image: /images/logo-intellij.png

O projeto Lombok é uma biblioteca java que você pode adicionar na sua IDE e ferramenta de _build_ para minimizar a quantidade de código necessário no seu projeto.

O Lombok atua no processo de compilação do seu código adicionando códigos automaticamente. Tirando de você a necessidade de escrever alguns códigos como por exemplo os métodos GET, SET, hashcode, equals, etc.

Se você usa o IntelliJ IDEA como ambiente de desenvolvimento e quer usar o Lombok no seu projeto, o que você precisa fazer é ...

## 1. Adicionar o Lombok como dependência do seu projeto.

Se você estiver utilizando o maven, basta adicionar o código abaixo no bloco `<dependencies>` do seu `pom.xml`.

```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.2</version>
    <scope>provided</scope>
</dependency>
```

## 2. Instalar o plugin do Lombok no IntelliJ IDEA

Instalar o plugin do Lombok do Intellij IDEA é muito simples. Basta seguir os passos abaixo:

### 1. Acesse o menu `File > Settings` (ou o atalho `Ctrl+Alt+S`).

![IntelliJ: File > Settings](/images/intellij/intellij-file-settings.png)

### 2. Acesse a opção `Plugins`.

### 3. Clique em  `Browse repositories`.

![IntelliJ: Browse repositories...](/images/intellij/intellij-plugins-browse-repositories.png){:width=100%}

### 4. Pesquise por `Lombok Plugin`

### 5. Selecione o plugin na lista de opções.

### 6. Clique em `Install`.

![IntelliJ: Install Lombok Plugin...](/images/intellij/install-lombok-plugin.png){:width=100%}

### 7. Após o download e a instalação do plugin, reinicie o Intellij IDEA.

Com esses passos você poderá utilizar todo o poder do Lombok no seu projeto Java.

## Referencias

1. [ProjectLombok: IntelliJ IDEA](https://projectlombok.org/setup/intellij){:target=\_blank}
