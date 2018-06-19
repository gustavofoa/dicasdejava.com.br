title: Spring-boot: Como criar a estrutura de uma aplicação web do ZERO com Spring Initializr
date: 2018-06-19
author: Gustavo Furtado de Oliveira Alves
category: Frameworks
tags: Spring-Boot, REST, API
image: /images/logo-spring-boot.png

Uma das grandes utilização do Java é para criação de aplicações Web e APIs REST e
um dos melhores frameworks para isso é o **Spring-boot**.

O Spring-boot surpreende pela facilidade para criar uma aplicação web em minutos
e com pouco código. Na verdade, só o código que você está interssado de fato.

O modo mais fácil (que nos dá o código praticamente pronto) de criar uma aplicação com Spring-Boot,
é utilizando o **Spring Initializr**.

Neste post vamos utilizar o Spring Initializr para criar uma API com um endpoint (endereço para um recurso) retornando um dado simples.

**Importante!** Você pode usar o maven do seu computador se já tiver instalado, ou utilizar o executavel `mvnw` que é baixado junto com a sua aplicação pelo Spring Initializr.

## Criando uma aplicação Web o Spring Initializr

Você pode seguir o passo-apasso abaixo para baixar o código da sua aplicação com Spring-boot já configurado.

### 1. Baixe o código do Spring-Boot configurado

Acesse [https://start.spring.io/](https://start.spring.io/), configure os metadados básicos do seu projeto,
quais dependências do Spring nós vamos utilizar (Web no caso) e pronto! Agora você pode baixar um arquivo ZIP com o seu projeto Spring-boot configurado.

![Criando um projeto spring-boot simples](/images/spring-boot-swagger/criando-um-projeto-spring-boot.gif){:width=100%}

### 2. Descompacte o arquivo ZIP localmente

Após clicar em **Generate Project**, um arquivo ZIP será baixado para o seu computador, agora você precisa descompactar o arquivo em uma pasta local.

### 3. Acesse a pasta descompactada pelo prompt de comando

Abra o prompt de comando e acesse a pasta descompactada. (`cd <caminho da pasta>`)

### 4. Baixe as dependências do projeto

Execute o comando `mvn clean install` para baixar as dependências do projeto através do maven.
Você também pode utilizar o mvnw que vem no arquivo ZIP do mesmo jeito `mvnw clean install`.

![mvn clean install](/images/spring-boot-swagger/mvn-clean-install.gif){:width=100%}

### 5. Crie seu primeiro endpoint

Crie uma class RestController com um método responsável por responder uma requisição GET, como no exemplo abaixo.

```java
package br.com.dicasdejava.springbootsample.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController("endpoint")
public class SampleController {

    @GetMapping
    public ResponseEntity<String> get(){
        return new ResponseEntity<>("OK", HttpStatus.OK);
    }

}

```

A classe acima utiliza a anotação `@RestController` para informar o Spring-boot que ela é um controller rest e ainda diz qual o endereço do endpoint.

Além disso ela tem um método com a anotação `@GetMapping` que diz qual método deve ser chamado quando o controller receber uma requisição HTTP GET em seu endereço padrão `endpoint`. O método retorna uma responsta HTTP com Status 200 e o corpo da resposta com o valor `OK`.

### 6. Execute aplicação

Execute o comando `mvn spring-boot:run` para executar a sua aplicação.
Você também pode utilizar o mvnw que vem no arquivo ZIP do mesmo jeito `mvnw spring-boot:run`.

Após a execução do comando você verá a seguind mensagem no prompt de comando

![mvn spring-boot:run ](/images/spring-boot-swagger/mvn-spring-boot-run.gif){:width=100%}

Isso significa que a sua aplicação web já está rodando na porta 8080.

### 7. Acesse o endpoint

Abra o seu browser e acesse a URL `http://localhost:8080/endpoint/`.

![Acessando a aplicação pelo browser](/images/spring-boot-swagger/acesso-endpoint-browser.png)

## Tudo pronto!

Com esse pequeno passo-a-passo você já tem a sua aplicação web rodando com Spring-boot.

## Referências

[Spring Initializr](https://github.com/spring-io/initializr){:target=\_blank}