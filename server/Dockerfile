FROM python:3.7-slim

RUN apt-get update && apt-get install -y python3-dev build-essential

WORKDIR /opt/fastapi-app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /var/log/fastapi-app/

COPY . /opt/fastapi-app
