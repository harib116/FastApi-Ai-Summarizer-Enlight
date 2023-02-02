# Image
# User
# Entrypoint


FROM python:3.9.16-bullseye

ENV environment DEV
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /curedu/api


COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir


RUN apt update


COPY . .


CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--workers", "2"]

