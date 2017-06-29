title: Tudo que você precisa saber sobre comentários em Java
date: 2017-06-29
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Java Básico
image: /images/logo-java.png

Toda linguagem de programação provê formas de criar comentários no código,
ou seja, códigos que são ignorados pelo compilador.

Vejamos as formas de criar comentários em Java.

```java
package br.com.dicasdejava.fundamentos;

public class ComentariosEmjava {

	public static void main(String[] args) {

		String texto = "Este é um código sem comentário.";
		System.out.println(texto);

		//Este é um comentário de linha.
		//Este comentário pode aparecer em qualquer parte do arquivo .java
		//Tudo que estiver depois dos caracteres // é um comentário
		texto = "Outro comando";//Mesmo que seja uma linha que já tenha um comando.
		//Porém após abrir o comentário com // ele não pode ser fechado na linha.
		System.out.println(texto);

		/*Comentário interno da linha*/
		/*Este tipo de comentário deve ser fechado com */
		/*Ele pode inclusive ocupar
		mais de uma linha, mas deve ser fechado! */

		//Após fechar o comenário interno de linha pode ter um comando java
		/*Comentário de exemplo*/texto = "mais um comando";
		System.out.println(texto);

		texto /*este comentário pode estar no meio da linha*/ = "Outro comando";
		System.out.println(texto);

		texto = "Dentro de uma String não pode ter comentário " +
		"/*isso continua sendo um texto, não é comentário*/.";
		System.out.println(texto);

		//Comentários dentro de linha só não pode estar no meio de uma palavra do comando
		//Como este exemplo:
		//Str/*comentario*/ing texto2 = "teste";
		//Ou neste outro exemplo:
		//String tex/*comentario*/to = "teste;

		/*
		 * Bloco de comentário:
		 * Este bloco de comentário não é diferente do comentário interno de linha
		 * Mas é muito utilizado para organização do código com esses * no inicio.
		 * Geralmente vemos este tipo de comentário
		 * para descrever o funcionamento de um método ou uma classe.
		 * Como na descrição do método abaixo
		 */

	}
	
	/*
	 * Este método não faz nada!
	 * Este comentário descreve o método abaixo
	 */
	public void metodo(){
		
	}

}
```

Saída:

```
Este é um código sem comentário.
Outro comando
mais um comando
Outro comando
Dentro de uma String não pode ter comentário /*isso continua sendo um texto, não é comentário*/.
```

##Javadoc

Além dos comentários simples do Java, há um tipo de comentário especial,
utilizado para documentar classes, interfaces, enums e métodos.

Esse tipo de comentário é chamado de **Javadoc**.

O Javadoc é um comentário que começa com /** e é fechado com */.
No Javadoc podemos podemos descrever parâmetros e retornos de métodos,
exceções retornadas, etc.

Confira no código-exemplo abaixo.

```java
package br.com.dicasdejava.fundamentos;

/**
 * Esta classe é um exemplo de classe que tem comentários do tipo Javadoc
 */
public class ClasseComJavadoc {

	/**
	 * Este é um comentário de Javadoc
	 * @param parametro - este é um parâmetro do método
	 * @return Este metodo retorna falso (sempre)
	 * @throws Exception - Esta exeption nunca é lançada neste método,
	 * mas tá aqui pra exemplificar o comentário Javadoc para Exceptions
	 */
	public boolean outroMetodo(String parametro) throws Exception {
		return false;
		//Comentários de Javadoc iniciam com /**
		//O comentário deste método é um comentário de Javadoc
		//Mas estes comentários aqui de dentro do método não são do tipo Javadoc
	}

}
```

Referências:

1. [How to Write Doc Comments for the Javadoc Tool](http://www.oracle.com/technetwork/articles/java/index-137868.html)
