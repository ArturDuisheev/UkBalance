FROM python:3.10.9-alpine3.17

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN adduser --disabled-password --gecos '' appuser

WORKDIR /app

RUN apk update && \
    apk add --no-cache \
        musl-dev \
        gcc \
        libc-dev \
        libffi-dev \
        openssl-dev

COPY ./requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

USER appuser

COPY . /app/
