# dicasdejava.com.br

Blog sobre java.

## Dependências do projeto

É preciso ter o node e o python3 instalado na maquina para que seja possa rodar o sistema.

## Rodando o projeto

Após ter feito com clone do projeto com para a maquina local com o comando `git clone git@github.com:gustavofoa/dicasdepython.com.br.git` será necessário instalar o gulp globalmente utilizando o comando `npm install -g gulp`.

Instalado o gulp globalmente acesse a pasta do projeto rode o comando `npm install` para ser instalado as dependências do node, crie uma virtualenv para rodar o sistema em python com o comando `python3 -m  venv venv`, ative a virtualenv como o comando `source venv/bin/activate`, agora instale as dependências do python usando `pip3 install -r requirements.txt`.

Após todas as dependências instaladas podemos rodar projeto com o comando `gulp serve` esse comando irá gerar os arquivos e subir um servidor no enderço **<http://localhost:1337>**
