# Bingo das Sílabas

Projeto educacional e um passatempo para as crianças e toda a família, desenvolvido em [Python](https://www.python.org) usando o [Django](https://www.djangoproject.com).
Disponível em https://bingosilabas.ozorest.me

## Como rodar localmente

### Fazendo o git clone

`git clone https://github.com/ozorest/bingo-silabas.git`

`cd bingo-silabas`

`python manage.py runserver`

E navegue para http://127.0.0.1:8000

### Usando a imagem do docker

`docker run -d --name bingo -p 8000:8000 ozorest\bingosilabas`

E navegue para http://127.0.0.1:8000

Se preferir usar o `docker-compose` tem um arquivo ([docker-compose.yml](https://raw.githubusercontent.com/ozorest/bingo-silabas/master/docker-compose.yml)) pronto aqui na raiz do repositorio 
