FROM python:3.8-slim-buster as base

MAINTAINER Mykhailo Bilyi "mykhailo.bilyi@nure.ua"

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./web /usr/src/app
WORKDIR /usr/src/app

EXPOSE 5000

CMD ["python3", "server.py"]
