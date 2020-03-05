---
title: 'Java: Como converter LocalDate e LocalDateTime em Date e vice-versa'
date: '2018-06-28'
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: Java 8, conversão, Date
image: /images/logo-java.png
---

Este post demostra como converter `java.time.LocalDate` e `java.time.LocalDateTime`
em `java.util.Date` e vice-versa.

## LocalDate para Date

O código abaixo mostra como converter `java.time.LocalDate`
em `java.util.Date` e de volta para `java.time.LocalDate`.

```java
package br.com.dicasdejava.util;

import java.time.LocalDate;
import java.time.ZoneId;
import java.util.Date;

public class ConverterLocalDateParaDate {

	public static void main(String[] args) {

		LocalDate localDate = LocalDate.of(2018, 6, 28);
		System.out.println("LocalDate = " + localDate);

		Date date1 = Date.from(localDate.atStartOfDay(ZoneId.systemDefault()).toInstant());
		System.out.println("Date      = " + date1);

		localDate = date1.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
		System.out.println("LocalDate = " + localDate);

	}
}
```

Saída:

```
LocalDate = 2018-06-28
Date      = Thu Jun 28 00:00:00 BRT 2018
LocalDate = 2018-06-28
```

## LocalDateTime para Date

Agora o código que mostra a conversão de `java.time.LocalDateTime`
em `java.util.Date` e de volta para `java.time.LocalDateTime`.

```java
package br.com.dicasdejava.util;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.Date;

public class ConverterLocalDateTimeParaDate {

	public static void main(String[] args) {

		LocalDateTime localDate = LocalDateTime.of(2018, 6, 28, 19, 18);
		System.out.println("LocalDateTime = " + localDate);

		Date date1 = Date.from(localDate.atZone(ZoneId.systemDefault()).toInstant());
		System.out.println("Date      = " + date1);

		localDate = date1.toInstant().atZone(ZoneId.systemDefault()).toLocalDateTime();
		System.out.println("LocalDate = " + localDate);

	}
}
```

Saída:

```
LocalDateTime = 2018-06-28T19:18
Date          = Thu Jun 28 19:18:00 BRT 2018
LocalDateTime = 2018-06-28T19:18
```


Referências:

1. [JavaDoc: LocalDate](https://docs.oracle.com/javase/8/docs/api/java/time/LocalDate.html){:target=\_blank}
1. [JavaDoc: LocalDateTime](https://docs.oracle.com/javase/8/docs/api/java/time/LocalDateTime.html){:target=\_blank}
1. [JavaDoc: Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html){:target=\_blank}
1. [JavaDoc: Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html){:target=\_blank}
1. [JavaDoc: ZoneId](https://docs.oracle.com/javase/8/docs/api/java/time/ZoneId.html){:target=\_blank}