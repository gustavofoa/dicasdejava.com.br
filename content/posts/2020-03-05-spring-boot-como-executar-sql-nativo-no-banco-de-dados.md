---
title: 'Spring-boot: Como executar SQL nativo no banco de dados'
date: '2020-03-05'
author: Gustavo Furtado de Oliveira Alves
category: Frameworks
tags: 'Spring-Boot, JPA, Spring Data, SQL'
image: /images/logo-spring-boot.png
---
Embora, com o Spring-boot é sempre indicado trabalhar com o banco de dados via os mapeamentos Objeto-Relacional e os *Repositorys*. Pode ser que você precise, por algum motivo, **executar um comando SQL nativo no banco de dados com Spring-boot**. Vamos ver neste post uma forma bem simples de fazer isso.

A primeira coisa, por questão de organização, eu sugiro que você crie um service para encapsular as execuções de SQL nativos. E neste service nós vamos incluir o código para executar um SQL nativo no banco de dados.

```java
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;

@Service
public class NativeScriptService {

    @PersistenceContext
    private EntityManager entityManager;

    @Transactional
    public void execute(String sql){
        entityManager.createNativeQuery(sql).executeUpdate();
    }

}
```

Bem simples né ...

Veja que estamos recebendo o comando sql como parâmetro e a forma como executamos este comando com o Spring-boot está encapsulada. Se futuramente nós quisermos mudar a forma de executar o comando SQL nativo, basta mudar nesta classe. ;)

Agora você pode usar este service para executar um script SQL nativo no seu banco de dados. Veja um exemplo.

```java
import org.springframework.beans.factory.annotation.Autowired;

public class SequenceManagerService {

    @Autowired
    private NativeScriptService nativeScriptService;

    public void resetClienteSequence(){
        nativeScriptService.execute("alter sequence CLIENTE_SEQUENCE restart");
    }

}
```

No exemplo acima, nós estamos executando um comando SQL em um banco Postgres para reiniciar a contagem de uma sequence para o valor inicial.

Mas poderia ser qualquer comando SQL nativo do seu banco de dados.

**Importante!** Use este recurso com cautela, pois os comandos nativos de um SGBD podem não funcionar em um outro SGBD. Isto cria um forte acoplamento do seu sistema ao SGBD que você está utilizando.

Gostou? Comente aí nos comentários o que você achou.

## Referências

1. [Javadoc: EntityManager.createNativeQuery(String)](https://javaee.github.io/javaee-spec/javadocs/javax/persistence/EntityManager.html#createNativeQuery-java.lang.String-){:target=_blank}
2. [Javadoc: Query.executeUpdate()](https://javaee.github.io/javaee-spec/javadocs/javax/persistence/Query.html#executeUpdate--){:target=_blank}
