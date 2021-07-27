# short_url
API encurtadora de URL's.
https://shortyme.herokuapp.com/

#### Observação
Ao acessar o link do app o heroku irá retira-lo do seu repouso, por isso aguarde alguns segundos até ele ser iniciado por gentileza.

## Sumário

- [Motivação](#motivacao)
- [Documentação](#documentacao)
- [A API](#a-api)
- [O Banco de Dados](#o-banco-de-dados)
- [Instalando Dependências e Executando o Projeto](#instalando-dependencias-e-executando-o-projeto)
- [Docker](#docker)
- [Heroku](#heroku)
- [A Fazer](#a-fazer)

## Motivação
Com diversos sites para encurtar URL's, como o famoso Bitly, e sua utilização diária em grandes URL's decidi realizar um projeto com a mesma ideia principal, porém de forma diferente. Com meus constantes estudos em framworks web, ORM e API's decidi adaptar a ideia para isso, afim de programar utilizando novas tecnologias.

## Documentação
Para ler a documentação basta acessar o link do app no inicio do README e clicar "Docs" ou acesse diretamente clicando [aqui](https://shortyme.herokuapp.com/swagger/)

## A API
A API foi construída utilizando o web framework Sanic. Ela possui apenas uma rota principal, sendo ela a forma de cadastrar URL's e receber a mesma de forma curta, caso ela já esteja cadastrada o retorno será de um aviso. Acessando a URL encurtada, você será redirecionado ao site da URL original.

## O Banco de Dados
Para armazenar as URL's originais foi utilizado um banco de dados em PostgreSQL, trabalhando nele através da ORM Pony, criando a tabela, inserindo os dados e realizando as consultas.

## Instalando Dependências e Executando o Projeto
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
```
$ pip -r install requirements.txt
```
Com todas as dependências instaladas basta digitar:
```
$ uvicorn app:app
```

### Observações
Lembrando que o projeto possui o Uvicorn para sua implementação em ASGI e o Gunicorn para sua WSGI.
Pelo Sanic utilizar-se dos conceitos Asynchronous o recomendado é executar através do Uvicorn(como demonstrado acima). Caso queira executar com o Gunicorn, o Sanic recomenda a utilização do seguinte comando, porém ele avisa que será perdido bastante beneficio de desempenho
Comando do Sanic pelo Gunicorn:
```
$ gunicorn myapp:app --bind 0.0.0.0:1337 --worker-class sanic.worker.GunicornWorker
```
Assim como o Sanic, o Uvicorn também possui seu próprio "work class" para a utilização, dito como tendo todos o beneficios do Uvicorn.
O comando para executa-lo é:
```
$ gunicorn example:app -w 4 -k uvicorn.workers.UvicornWorker
```

## Docker
O Projeto possui um arquivo Dockerfile para a criação de sua imagem no Docker. Para criar a imagem basta digitar o comando no Terminal:
```
$ docker build -t short-url .
```
E para executar a imagem:
```
$ docker run -p 8000:8000 short-url
```

## Heroku
O projeto possui também um Procfile do Heroku para o seu deploy bem como possui uma versão no ar([clique aqui](https://shortyme.herokuapp.com/)).

## A Fazer
- "Lapidar" a API, melhorando as respostas em JSON
- Traduzir para o Inglês
