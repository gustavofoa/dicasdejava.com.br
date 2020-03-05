---
title: Como personalizar o banner do Spring-boot no log
date: '2018-06-25'
author: Gustavo Furtado de Oliveira Alves
category: Frameworks
tags: Spring-Boot, Personalização
image: /images/logo-spring-boot.png
---

Quando você roda a sua aplicação Spring-boot você já deve ter percebido que aparece no log um texto "Spring" bem grande. Assim:

![banner spring-boot](/images/spring-boot/banner-spring-boot.png){:style="width:80%; padding:10px;"}

Você gostaria de customizar esse banner no seu projeto do Spring-Boot?

Para alterar o banner que aparece no log do Spring-boot basta, criar um arquivo chamado `banner.txt`
na pasta `resources` do seu projeto.

![arquivo banner.txt na pasta resources](/images/spring-boot/resources-banner.png){:style="width:60%; padding:10px;"}

No arquivo `banner.txt` você pode colocar o texto que você quiser para aparecer no log.

![banner spring-boot personalizado com texto Dicas de Java](/images/spring-boot/banner-dicas-de-java.png){:style="width:80%; padding:10px;"}

### Escolhendo a fonte do texto

Legal, essa parte foi fácil! Mas eu não escrevi aquele texto, espaço-por-espaço, caracter-por-caracter...
Eu acessei [esse site](https://devops.datenkollektiv.de/banner.txt/index.html){:target=_\blank} que oferece um
**Gerador online de banner para o Spring-boot**.

Basta digitar o texto que você quer personalizar e escolher a fonte, dentre as várias que eles oferecem.

![Gerador online de banner para o Spring-boot](/images/spring-boot/gerador-banner-spring-boot.png){:style="width:100%; padding:10px;"}

Por fim, você pode copiar esse texto gerado pelo site e colar no seu arquivo `banner.txt`.

## Referências

[Spring-Boot: Customizing the banner](https://docs.spring.io/spring-boot/docs/current-SNAPSHOT/reference/htmlsingle/#boot-features-banner){:target=\_blank}