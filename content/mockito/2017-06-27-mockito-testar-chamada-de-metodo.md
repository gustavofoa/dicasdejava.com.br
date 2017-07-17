title: Mockito: Como testar chamada de método
date: 2017-06-27
author: Gustavo Furtado de Oliveira Alves
category: Mockito
tags: Mockito
image: /images/logo-mockito.png

Muita gente começa a usar o framework Mockito para fazer testes em Java
e tem dúvidas de como verificar se o método de uma dependência foi ou não chamado.

Confira no exemplo abaixo como fazer a verificação de chamada de método de uma dependência com o Mockito.

##Exemplo:

Primeiro vamos definir a Classe que está sendo testada
e uma dependência dela na qual vamos verificar a chamada do método,
através de um Mock criado com o Mockito. 

```java
package br.com.dicasdejava.mockito.verificarSeMetodoFoiChamado;

public class ClasseSendoTestada {

	DependenciaDaClasseSendoTestada dependencia;

	public ClasseSendoTestada(DependenciaDaClasseSendoTestada dependencia){
		this.dependencia = dependencia;
	}

	void metodoSendoTestado(String parametro){
		dependencia.metodoQueSeraChamado(parametro);
	}

}
```

Agora a dependência:

```java
package br.com.dicasdejava.mockito.verificarSeMetodoFoiChamado;

public interface DependenciaDaClasseSendoTestada {

	void metodoQueSeraChamado(String parametro);

}
```

##Teste

E o teste que faz a verificação da chamada do método com Mockito. 

```java
package br.com.dicasdejava.mockito.verificarSeMetodoFoiChamado;

import org.junit.Test;
import org.mockito.Mockito;

public class ClasseSendoTestadaTest {

	@Test
	public void testeMetodoFoiChamado(){

		//Cria Mock da dependência
		DependenciaDaClasseSendoTestada dependencia = Mockito.mock(DependenciaDaClasseSendoTestada.class);

		//Instancia a classe sendo testada passando a dependência Mockada
		ClasseSendoTestada classeSendoTestada = new ClasseSendoTestada(dependencia);

		//chama o método sendo testado
		classeSendoTestada.metodoSendoTestado("parâmetro-teste");

		//Verifica se o método da dependência foi chamado (incluindo o parâmetro exato)
		Mockito.verify(dependencia, Mockito.times(1)).metodoQueSeraChamado("parâmetro-teste");

	}

}
```

Este teste verifica se o método da dependência da classe foi chamado
e ainda verifica a quantidade de vezes que ele foi testado.

Se, por exemplo, quisermos verificar se o método foi acessado 5 vezes
bataria informar 5 no segundo parâmetro do método estático _verify_ da classe _Mockito_.

##Referencias

1. [Javadoc: Mockito](http://static.javadoc.io/org.mockito/mockito-core/2.8.47/org/mockito/Mockito.html#4){:target=\_blank}
