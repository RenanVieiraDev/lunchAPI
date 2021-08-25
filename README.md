# lunchAPI

API para a votação de restaurante do dia, a api foi desenvolvida com o framework Django,
tem a principal função o gerenciamento das escolhas do local onde a equipe predende
almoçar naquele determinado dia, a votação por padrão acontece entre o horario de
09:00 ate as 11:50, o administrador poderá fazer a inserção dos restaurantes
pelo painel adm do framework Django, com as opções de colocar os pratos do dia 
para cada dia da semana.

## Requisito do sistema para localhost:
  * python 3
  * venv
  * asgiref==3.4.1
  * Django==3.2.6
  * djangorestframework==3.12.4
  * pytz==2021.1
  * sqlparse==0.4.1
 
 ### instalação e runserver
   Para a instalação você precisará dar o comando **python -m venv ./venv** para instalar
   o ambiente virtual venv, após a instalação será necessario dar o comando de instalação
   de dependencias, dentro da pasta raiz do projeto de o comando **pip install requirements.txt**
   ambiente configurado agora vamos ativar o ambiente virtual,
   no windows de o comando **venv\Scripts\activate**
   no linux de o comando **source venv\Scripts\activate**
   após ativar o ambiente de o comando **python manage.py runserver**
   Deverá aparecer uma msg com o link de acesso para o servidor
   por padrão é o http://127.0.0.1:8000/
   cole na url do navegador e veja quais são as rotas disponiveis.
  
  ### End Points da API
    Rotas V1
    
     http://127.0.0.1:8000/v1/loginUser/<phoneUser>/<passwordUser>/ 
      Rota para realização de autorização dos usuarios que iram realizar a votação,
       o metodo usado é o (POST), todos os parametros são obrigatorios
       phoneUser (obrigatorio) = aqui sera informado o celular do usuario cadastrado
       passwordUser (obrigatorio) = aqui sera informado a senha do usuario cadastrado
       O retorno de erro é recebido caso o usuario não exista ou contiver a informação errada.
      
     http://127.0.0.1:8000/v1/listRestaurantsOfDay/
       Está rota pega todos os restaurantes que estão abertos para votação, o metodo usado
        para o recebimento das informações é o (GET)
        não a parametros nesta rota.
        
     http://127.0.0.1:8000/v1/users_list/
      Está rota lista todos os usuarios cadastrados, o metodo usado é o (GET)
        não a parametros nesta rota.
     
     http://127.0.0.1:8000/v1/rankingOfToday/
      Esta rota lista os 3 primeiros colocados rank dos restaurantes mais vodatos no dia,
      o metodo usado é o (GET)
        não a parametros nesta rota.
     
     http://127.0.0.1:8000/v1/rankingOfToday/
      Esta rota mostra o restaurante vencedor no dia,
      o metodo usado é o (GET)
        não a parametros nesta rota.
        
     http://127.0.0.1:8000/v1/resetRestaurantToVoteingToday/listRestaurantsId/
      Rota para realização do resete dos restaurantes que iram ser colocados para votação neste dia,
       o metodo usado é o (GET), todos os parametros são obrigatorios
       listRestaurantsId (obrigatorio) = aqui é passado uma lista de ID's dos restaurantes a serem resetados,
       a cada id escolhido é necessario separalos com uma (,) virgula
       ex: 1,2,3,4,5
       todos os restaurantes escolhidos entre automaticamente para a lista de votação do dia atual.
   
      http://127.0.0.1:8000/v1/voting/<idRestaurant>/<idUser>/
       Esta rota trata da ação de inserir um voto no restaurante escolhido, está rota trata
       da validação de inicio da votação,fim da votação e se o usuario já realizou um voto
       neste dia, então caso o usuario já tenha realizado uma votação hoje será enviado
       um objeto error para a identificação, o metodo usado é o (PUT).
       idRestaurant (obrigatorio) Aqui é inserido um unico id de um dos restaurantes que o usuario deseja votar.
       idUser (obrigatorio) Aqui é inserido o id do usuario que está votando no restaurante escolhido.
    
       
    
 ### considerações
  Aplicação desenvolvida como forma de estudo inicial do python.
  by:Renan Vieira
  
