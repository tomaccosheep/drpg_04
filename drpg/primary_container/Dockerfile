FROM ubuntu:latest
MAINTAINER Al Burns
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential libmysqlclient-dev vim iputils-ping dnsutils curl docker.io
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
#COPY . /app
