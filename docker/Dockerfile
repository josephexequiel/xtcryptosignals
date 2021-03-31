FROM python:3.8.8-alpine3.13

RUN python -m pip install --upgrade pip setuptools setuptools_rust
RUN apk add --no-cache \
    alpine-sdk \
    zlib \
    libjpeg-turbo-dev \
    libpng-dev \
    freetype-dev \
    lcms2-dev \
    libwebp-dev \
    harfbuzz-dev \
    fribidi-dev \
    tcl-dev \
    tk-dev \
    openssl-dev \
    libffi-dev \
    gcc \
    python3-dev \
    musl-dev \
    cargo \
    bash

WORKDIR /xtcryptosignals

ADD ./ ./

RUN pip install -r requirements.txt
RUN pip install -e .

ENV FLASK_ENV=docker
ENV SETTINGS_APP=/xtcryptosignals/xtcryptosignals/config/server.docker.env
