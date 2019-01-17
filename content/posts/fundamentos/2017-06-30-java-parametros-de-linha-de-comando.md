title: Java: Parâmetros de linha de comando
date: 2017-06-30
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Java Básico, main
image: /images/logo-java.png

Muita gente se acostuma a criar o método estático `main` no java 
e não sabe para quê serve o parâmetro do tipo `String[]` (Array de String),
geralmente nomeado como `args`. Vamos ver neste post porque este parâmetro existe
no método que inicia qualquer programa Java.

Antes de falar sobre java, é importante perceber que 
todo programa pode receber argumentos de linha de comando ao ser executado.
Peguemos por exemplo o programa "Bloco de Notas" do Windows, cujo comando de linha de comando é "notepad",
se você abrir o prompt de comando do Windows (ou o "Executar") e executar o comando 
`notepad <Caminho de um arquivo .txt por exemplo>`,
o software _Bloco de Notas_ vai abrir o seu arquivo que foi informado como argumento na linha comando.

O que foi informado na frente do comando para a execução do software
é chamado de **Argumento de linha de comando**.

No java, aquele array de String do método `main` serve para receber os _argumentos de linha de comando_
que são passados na hora de executar o programa.
Cada argumento é separado por um "espaço" no momento da execução.

Vamos ver isso na prática com o código abaixo:

```java
package br.com.dicasdejava.fundamentos;

public class ParametroDeLinhaDeComando {

	public static void main(String[] args) {

		System.out.println(args.length);
		for(String arg : args)
			System.out.println(arg);

	}

}
```

Ao ser executado, o código acima imprime no prompt de comandos a quantidade de argumentos recebidos,
e em seguida imprime cada argumento separadamente, ao imprimir cada item do array `args` em uma linha.

Abaixo eu apresento a compilação e a execução deste programinha Java
com diferentes argumentos de linha de comando (no Windows).

![Execução de um programa Java com argumentos de linha de comando](/images/parametros-de-linha-de-comando.png){:style="width:100%; padding:10px;"}

De **bônus**, no exemplo acima eu mostro como compilar e executar uma classe
que se encontra em um pacote.

Para compilar: `javac caminho\das\pastas\para\a\Classe.java` (\ para Windows e / para Linux e MacOS)

Para executar: `java caminho.das.pastas.para.a.Classe <argumentos de linha de comando separados por 'espaço'>`

Qualquer dúvida, escreva abaixo nos comentários.
