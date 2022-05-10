<h1 align="center"> Magic The Gathering - Back-end</h1>
<p align="center">Magic The Gathering, um crud de jogo simples e objetivo.</p>
<div align="center">
  <img src="https://img.shields.io/static/v1?label=Licence&message=MIT&color=2874F0"/>
  <img src="https://img.shields.io/static/v1?label=Python&message=3.10.4&color=ffd343"/>
  <img src="https://img.shields.io/static/v1?label=FastAPI&message=0.77.0&color=009485"/>
  <img src="https://img.shields.io/static/v1?label=Sqlalchemy&message=1.4.36.0&color=212529"/>
</div>

<!--ts-->
   * [Pré Requisitos](#pre-requisitos)
   * [Instalação](#instalacao)
      * [Clonando o repositório](#clone-repositorio)
      * [Criando a base de dados](#criar-base-dados)
      * [Navegando entre diretórios](#navegacao)
      * [Criando variáveis de ambiente](#dotenv)
      * [Instalando as dependências](#dependencias)
   * [Rotas Acessíveis](#rotas)
      * [Gerando um novo link](#genereteLink)
      * [Acessando o novo link](#accessLink)
      * [Estatisticas do link](#statistics)
   * [Tests (em breve)](#testes)
   * [Tecnologias](#tecnologias)
   * [Trabalhos Futuros](#trabalhos-futuros)
<!--te-->

<h4 align="center"> 
	🚧  Magic The Gathering  🚀 Em Fase Final...  🚧
</h4>

# Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com),
[Python](https://www.python.org),
[MySQL Community](https://dev.mysql.com/downloads/),
[MySQL workbench](https://dev.mysql.com/downloads/workbench/) ou [Dbeaver](https://dbeaver.io/download/),
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

# Instalação
## Clone este repositório
$ git clone <https://github.com/DeividhyTonetti/MTG.git>

## Crie uma base de dados MySQL
Existem "N" forma de realizar essa criação, a maneira que eu acho mais fácil é utilizar a ferramenta MySQL Workbech. <br>
-> Crie ou entre em uma connection já existente; <br>
-> Na lateral esquerda (navigator) clique com o botão direiro na parte vazia; <br>
-> Clique em create schema; <br>
-> Preencha o campo name e aplique. <br>

## Navegue até a pasta do projeto via terminal terminal/cmd
$ cd (diretório...)

# Rotas acessíveis
  ## Para observar a documentação
   ### /docs 

  ## Criar a carta
   ### /card/create
   	É necessário informar name, user_name, edition, foil, price
  ## Listar todas as cartas
   ### /listCard/{name_card}/{name_user}
   	É necessário informar o name_card, name_user
	
  ## Listar uma única carta
   ### /card/listAllCards
   	É necessário informar o name_user
	
  ## Atualizar a carta
   ### /card/editCard/{name_card}
     	É necessário informar o name_card, name_user, quantity (opcional), price(opcional)

  ## Deletar a carta
   ### /card/editCard/{name_card}
     	É necessário informar o name_card, name_user
  
## Crie um arquivo chamado .env na raiz do projeto e insira as seguintes variáveis de ambiente:
### Database
    DB_HOST= Nome do HOST - Exemplo: localhost
    DB_USER= Nome do Usuário - Exemplo: root  
    DB_PASS= Senha do banco - Exemplo: 123456789
    DB_NAME= Nome do banco criado - Exemplo enclink
  
### Pota
    PORT= Número da porta - Exemplo: 3000
  
### Name
    APP_NAME= Nome do projeto - Exemplo: MTG
  
### Desenvololvimento ou produção
    NODE_ENV=dev  (dev | production)
    APP_URL=http://localhost 
### Pota
    PORT= Número da porta - Exemplo: PORT=8000
  
### Instale as dependências do projeto
	$ pip install -r requirements.txt

### Execute a aplicação em modo de desenvolvimento
	$ uvicorn main:app --reload

# O servidor inciará na porta que você escolheu
Acesse no seu navegador <http://localhost:PORTA>

# Utilizando as rotas no navegador
Acesse no seu navegador <http://localhost:PORTA/docs>
Neste momento é possivel visualizar todas as rotas utilizadas no projeto, além disso, também é possivel acessar e testar essas as rotas.

# 
### 🛠 Tecnologias

As seguintes ferramentas e bibliotecas foram usadas na construção do projeto:

- [FastApi](https://fastapi.tiangolo.com)
- [Sqlalchemy](https://docs.sqlalchemy.org/en/14/)

### Autor
---

<a href="https://www.linkedin.com/in/deividhytonetti6/">
 <img style="border-radius: 50%;" src=https://avatars.githubusercontent.com/u/34030150?s=96&v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Deividhy Tonetti</b></sub></a> <a href="https://github.com/DeividhyTonetti" title="Rocketseat">🚀</a>


Feito com ❤️ por Deividhy J. Tonetti 👋🏽 Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Deividhy-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/deividhytonetti6/)](https://www.linkedin.com/in/deividhytonetti6/) 
[![Hotmail Badge](https://img.shields.io/badge/-deividhytonetti@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:deividhytonetti@gmail.com)](mailto:deividhytonetti@gmail.com)
