###########
# BUILDER #
###########

# pull official base image
FROM python:3-alpine as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add gcc python3-dev musl-dev jpeg-dev zlib-dev libjpeg

# lint
RUN pip install --upgrade pip
# RUN pip install flake8
# COPY . .
# RUN flake8 --ignore=E501,F401 .

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3-alpine

# create directory for the app user
RUN mkdir -p /app

ENV UID=1000
ENV GID=$UID

# create the app user
RUN addgroup -g $GID -S app && adduser -S app -G app --uid $UID

# create the appropriate directories
ENV HOME=/app
ENV APP_HOME=$HOME

WORKDIR $APP_HOME

# install dependencies
RUN apk update
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.prod.sh
CMD ["gunicorn", "bingo.wsgi:application", "--bind", "0.0.0.0:8000"]