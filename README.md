# short_url
API encurtadora de URL's

## Sumário

- [Motivação](#motivacao)
- [A API](#a-api)
- [O Banco de Dados](#o-banco-de-dados)
- [Instalando Dependências e Executando o Projeto](#Instalando-dependencias-e-executando-o-projeto)
- [Docker](#docker)
- [Heroku](#heroku)
- [A Fazer](#a-fazer)

##Motivação
Com diversos sites para encurtar URL's, como o famoso Bitly, e sua utilização diária em grandes URL's decidi realizar um projeto com a mesma ideia principal, porém de forma diferente. Com meus constantes estudos em framworks web, ORM e API's decidi adaptar a ideia para isso, afim de programar utilizando novas tecnologias.

##A API
A API foi construída utilizando o web framework Sanic. Ela possui apenas uma rota principal, sendo ela a forma de cadastrar URL's e receber a mesma de forma curta, caso ela já esteja cadastrada o retorno será de um aviso. Acessando a URL encurtada, você será redirecionado ao site da URL original.

##O Banco de Dados
Para armazenar as URL's originais foi utilizado um banco de dados em PostgreSQL, trabalhando nele através da ORM Pony, criando a tabela, inserindo os dados e realizando as consultas.

##Instalando Dependências e Executando o Projeto
Primeiramente clone o repositório do projeto:
```
git clone https://github.com/fabiobarkoski/short-url.git
```
Em seguida crie o ambiente virtual e o rode:
```
$ python -m venv env
$ env/Scripts/activate
```
Após instale as dependências dentro do `requirements.txt`:
  $ pip -r install requirements.txt
Com todas as dependências instaladas basta digitar:
  $ uvicorn app:app

###Observações
Lembrando que o projeto possui o Uvicorn para sua implementação em ASGI e o Gunicorn para sua WSGI, ambos para o ambiente de produção. Por o Sanic utilizar-se dos conceitos Asynchronous o recomendado é executar através do Uvicorn.

##Docker
O Projeto possui um arquivo Dockerfile para a criação de sua imagem no Docker. Para criar a imagem basta digitar o comando no Terminal:
  $ docker build -t short-url .
E para executar a imagem:
  $ docker run -p 8000:8000 short-url  

##Heroku

##A Fazer
- "Lapidar" a API, melhorando as respostas em JSON
