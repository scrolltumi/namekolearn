FROM python:3.7-slim-stretch

RUN apt-get update && \
    apt-get install --yes build-essential autoconf libtool pkg-config \
    libgflags-dev libgtest-dev clang libc++-dev automake git libpq-dev

WORKDIR /app

# COPY requirements.txt ./ 
# RUN pip install -r requirements.txt

RUN pip install nameko

COPY . .


