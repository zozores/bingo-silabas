###########
# BUILDER #
###########

# baixa a imagem base como builder
FROM python:3-alpine as builder

# define diretorio de trabalho
WORKDIR /usr/src/app

# define variaveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# instala dependencias
RUN apk update \
    && apk add gcc python3-dev musl-dev jpeg-dev zlib-dev libjpeg

# lint
RUN pip install --upgrade pip
# RUN pip install flake8
# COPY . .
# RUN flake8 --ignore=E501,F401 .

# instala dependencias do projeto
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# baixa a imagem base
FROM python:3-alpine

# define diretorio da aplicacao
ENV APP_HOME=/app

# cria diretorio da aplicacao
RUN mkdir -p $APP_HOME

# define as variaveis com UID e GID do usuario app
# para poderem ser sobreescritas se necessario
ENV UID=1000
ENV GID=$UID

# cria o usuario app
RUN addgroup -g $GID -S app && adduser -S app -G app --uid $UID

# define diretorio do usuario app sendo o mesmo do APP_HOME
ENV HOME=$APP_HOME

# define o APP_HOME como diretorio de trabalho
WORKDIR $APP_HOME

# instala dependencias puxando do builder
RUN apk update
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copia o projeto da aplicacao
COPY . $APP_HOME

# da permissao para o usuario app em todo o diretorio APP_HOME
RUN chown -R app:app $APP_HOME

# troca para o usuario app
USER app

# roda o gunicorn
CMD ["gunicorn", "bingo.wsgi:application", "--bind", "0.0.0.0:8000"]