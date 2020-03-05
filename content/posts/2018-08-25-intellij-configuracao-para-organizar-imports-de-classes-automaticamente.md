---
title: 'Intellij IDEA: Configuração para organizar imports de classe automaticamente'
date: '2018-08-25'
author: Gustavo Furtado de Oliveira Alves
category: Ferramentas
tags: atalhos, Intellij IDEA
image: /images/logo-intellij.png
---

Uma das primeiras dúvidas de quem migra do eclipse para o IntelliJ IDEA é:

**Qual o atalho para organizar os imports do java, equivalente ao `CTRL + SHIFT + O` do eclipse?**

No intelliJ o atalho muda para **`CTRL + ALT + O`**. Mas este atalho apenas limpa os imports não utilizados.
Ou seja, não importa automaticamente classes sem ambiguidade, como no eclipse.

## Configurando import automático no IntelliJ IDEA

Mas você pode configurar o IntelliJ para importar classes automaticamente, inclusive sem precisar pressionar o atalho **`CTRL + ALT + O`**. Para fazer essa configuração siga estes passos no menu.

> **File –>> Settings –>> Editor –>> General –>> Auto Import**

E marque estas opções:

1. [X] **Add unambiguous imports on the fly**
2. [X] **Optimize imports on the fly**

Assim:

![Configuração para auto-import de classes no IntelliJ](/images/intellij/intellij-configuracao-atalho-auto-import.png){:style="width:100%; padding:10px;"}

Pronto, agora quando o IntelliJ identificar uma classe que não tenha ambiguidade de import, ele vai importar a classe e organizar os imports automaticamente seu código.
Isso é muito útil!

Veja um exemplo de utilização...

O IntelliJ não importa o `Map` inicialmente por ser possível mais de um import possível (ou seja, ele ainda é ambíguo neste momento), mas quando eu especifico que a implementação da interface `Map` é o `HashMap`, o IntelliJ já importa a classe e a interface automaticamente, isso porque acaba a ambiguidade.

E quando eu apago a linha que tem o `Map` o `HashMap`, o IntelliJ já remove os imports sem eu precisar pressionar nenhuma tecla!

![Exemplo de import automático no IntelliJ](/images/intellij/intellij-exemplo-auto-import.gif){:style="width:100%; padding:10px;"}

## Import de classes ambíguas

Classes ambíguas são as classes que podem ser encontradas em pacotes diferentes, com o mesmo nome.
Neste caso o IntelliJ não saberia escolher qual classe importar.

Mas ainda assim, você pode informar o IntelliJ, qual classe você quer importar, para isso basta utilizar o atalho `Alt + Enter` e selecionar a classe desejada.

For ambiguous imports (same class name in a different package), you still need click on the class name and press ALT + ENTER keys to import the package manually.

##Referencias

1. [Intellij IDEA Help: auto import](https://www.jetbrains.com/help/idea/settings-auto-import.html#d2587995e32){:target=\_blank}
