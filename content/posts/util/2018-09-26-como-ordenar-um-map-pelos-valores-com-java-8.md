title: Como ordenar um map pelos valores com Java 8+
date: 2018-09-26
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: Java 8, Map, ordenação
image: /images/logo-java.png

O **Java 8** trouxe muitas coisas úteis para o desenvolvento Java.
Neste post vamos ver uma forma elegante de ordenar um Map pelos valores usando o `stream`,
uma das funcionalidades introduzidas com o Java 8.

Primeiro, vamos criar um `Map` de exemplo com a população do Brasil por estado, em uma ordem aleatória.

No código abaixo nós criamos um método que retorna o Map com a população do Brasil por estado.

```java
public static Map<String, Integer> getPopulacaoPorEstado(){
	final Map<String, Integer> populacaoBrasil = new HashMap<>();
	populacaoBrasil.put("Santa Catarina", 7075494);
	populacaoBrasil.put("Rio Grande do Sul", 11329605);
	populacaoBrasil.put("Mato Grosso do Sul", 2748023);
	populacaoBrasil.put("Tocantins", 1555229);
	populacaoBrasil.put("Roraima", 576568);
	populacaoBrasil.put("Minas Gerais", 21040662);
	populacaoBrasil.put("São Paulo", 45538936);
	populacaoBrasil.put("Maranhão", 7035055);
	populacaoBrasil.put("Rio de Janeiro", 17159960);
	populacaoBrasil.put("Ceará", 9075649);
	populacaoBrasil.put("Acre", 869265);
	populacaoBrasil.put("Paraíba", 3996496);
	populacaoBrasil.put("Alagoas", 3322820);
	populacaoBrasil.put("Piauí", 3264531);
	populacaoBrasil.put("Pernambuco", 9496294);
	populacaoBrasil.put("Rio Grande do Norte", 3479010);
	populacaoBrasil.put("Amapá", 829494);
	populacaoBrasil.put("Pará", 8513497);
	populacaoBrasil.put("Mato Grosso", 3441998);
	populacaoBrasil.put("Rondônia", 1757589);
	populacaoBrasil.put("Goiás", 6921161);
	populacaoBrasil.put("Espírito Santo", 3972388);
	populacaoBrasil.put("Paraná", 11348937);
	populacaoBrasil.put("Sergipe", 2278308);
	populacaoBrasil.put("Amazonas", 4080611);
	populacaoBrasil.put("Distrito Federal", 2974703);
	populacaoBrasil.put("Bahia", 14812617);
	return populacaoBrasil;
}
```

## Ordenação ascendente do Map com Java

Para ordenar o `Map` acima em ordem crescente com Java 8 nós fazemos assim.

```java
final Map<String, Integer> populacaoBrasil = getPopulacaoPorEstado();

final Map<String, Integer> populacaoOrdenada = populacaoBrasil.entrySet()
		.stream()
		.sorted(Map.Entry.comparingByValue())
		.collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, (e1, e2) -> e1, LinkedHashMap::new));

populacaoOrdenada.forEach((key, value) -> System.out.println(value + " - " + key));
```

E a saída deste código é essa:

```
576568 - Roraima
829494 - Amapá
869265 - Acre
1555229 - Tocantins
1757589 - Rondônia
2278308 - Sergipe
2748023 - Mato Grosso do Sul
2974703 - Distrito Federal
3264531 - Piauí
3322820 - Alagoas
3441998 - Mato Grosso
3479010 - Rio Grande do Norte
3972388 - Espírito Santo
3996496 - Paraíba
4080611 - Amazonas
6921161 - Goiás
7035055 - Maranhão
7075494 - Santa Catarina
8513497 - Pará
9075649 - Ceará
9496294 - Pernambuco
11329605 - Rio Grande do Sul
11348937 - Paraná
14812617 - Bahia
17159960 - Rio de Janeiro
21040662 - Minas Gerais
45538936 - São Paulo
```

## Ordenação descendente do Map com Java

E para ordenar o `Map` acima em ordem decrescente com Java 8 nós fazemos assim.

```java
final Map<String, Integer> populacaoBrasil = getPopulacaoPorEstado();

final Map<String, Integer> populacaoOrdenada = populacaoBrasil.entrySet()
		.stream()
		.sorted(Map.Entry.comparingByValue().reversed())
		.collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, (e1, e2) -> e1, LinkedHashMap::new));

populacaoOrdenada.forEach((key, value) -> System.out.println(value + " - " + key));
```

E a saída deste código é essa:

```
45538936 - São Paulo
21040662 - Minas Gerais
17159960 - Rio de Janeiro
14812617 - Bahia
11348937 - Paraná
11329605 - Rio Grande do Sul
9496294 - Pernambuco
9075649 - Ceará
8513497 - Pará
7075494 - Santa Catarina
7035055 - Maranhão
6921161 - Goiás
4080611 - Amazonas
3996496 - Paraíba
3972388 - Espírito Santo
3479010 - Rio Grande do Norte
3441998 - Mato Grosso
3322820 - Alagoas
3264531 - Piauí
2974703 - Distrito Federal
2748023 - Mato Grosso do Sul
2278308 - Sergipe
1757589 - Rondônia
1555229 - Tocantins
869265 - Acre
829494 - Amapá
576568 - Roraima
```

## Explicação

Se você veio até este post querendo mais do que o código que faz a ordenação continue lendo,
agora vamos tentar entender o que está acontecendo com o código de ordenação com Java 8 apresentado.

A primeira coisa que temos que perceber é que nós usamos `stream` para fazer a ordenação.
Precisamos do Stream para fazer operações de agregação e comparação. E a interface `Collection` recebeu um método para retornar um Stream a partir do no Java 8.

Mas, infelizmente a interface `Map` não é uma filha de `Collection`, por isso
nós precisamos obter o `Set` de `Map.Entry` do map.
Ou seja, a coleção (set) de objetos que representam a combinação de chave/valor do Map. Fazemos isso através do método `.entrySet()` da interface `Map`.

De posse de um `Set` nós podemos obter o Stream para fazer a ordenação, basta utilizar o método `.stream()` do `Set`.

O `Stream` nos oferece um método para ordenação que recebe um `Comparator`: `.sorted(Comparator<? super T> comparator)`.

Coincidentemente a classe `Map.Entry` tem um método `comparingByValue()` que retorna um Comparator já implementado
que compara o os valores do Map em ordem natural, ou seja ascendente.

Por fim, nós podemos coletar (`.collect`) o resultado do Stream em um outro `Map`, mas dessa vez utilizando a implementação `LinkedHashMap` para manter a ordenação que o Stream nos entrega.

E para utilizar um Comparator que traz a ordem inverida, podemos obter um Comparator invertido através do método `.reverse()` da interface `Collection`.

Gostou? Alguma dúvida? Utilize a área de comentários aqui em baixo.

## Referências:

1. [Wikipedia: Lista de unidades federativas do Brasil por população](https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_popula%C3%A7%C3%A3o){:target=\_blank}
2. [Javadoc: Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html){:target=\_blank}
3. [Javadoc: Map.Entry](https://docs.oracle.com/javase/8/docs/api/java/util/Map.Entry.html){:target=\_blank}
4. [Javadoc: Map.Entry.comparingByValue](https://docs.oracle.com/javase/8/docs/api/java/util/Map.Entry.html#comparingByValue--){:target=\_blank}
5. [Javadoc: Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html){:target=\_blank}
6. [Javadoc: Collection.stream](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html#stream--){:target=\_blank}
7. [Código-fonte do exemplo](https://github.com/gustavofoa/examples.dicasdejava.com.br/blob/master/src/main/java/br/com/dicasdejava/util/OrdenarMapPorValores.java){:target=\_blank}