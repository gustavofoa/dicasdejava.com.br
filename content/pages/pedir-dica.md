title: Pedir dica!
slug: pedir-dica

O objetivo do blog **{ Dicas de Java }**
é ajudar pessoas a aprenderem java com dicas simples de como
implementar soluções para problemas comuns do dia-a-dia do programador.

Mas pode ser que você não encontre a solução para um problema que você está tendo neste momento.

Se quiser saber como fazer alguma coisa em java e você não encontrou no site.
Basta preencher o formulário abaixo pedindo a sua **Dica de Java**.

<form action="https://formspree.io/gustavo@dicasdeprogramacao.com.br" method="POST">
  <div class="form-row">
    <div class="form-group col-md-6">
        <label for="name">Nome</label>
        <input type="text" class="form-control" id="name" placeholder="Ex: José">
    </div>
    <div class="form-group col-md-6">
        <label for="email">Seu E-mail</label>
        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Ex: jose@dicasdejava.com.br">
        <small id="emailHelp" class="form-text text-muted">Não vamos compartilhar o seu email com ninguém!</small>
    </div>
  </div>
  <div class="form-group">
    <label for="texto">Descreva a sua dúvida</label>
    <textarea class="form-control" id="texto" rows="6" placeholder="Quero aprender a fazer ... em Java."></textarea>
  </div>
  <button type="submit" class="btn btn-primary">Enviar</button>
</form>