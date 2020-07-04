FROM python:3-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install --upgrade pip
    
COPY . .
RUN pip install -r requirements.txt \
    && apk del build-deps

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]