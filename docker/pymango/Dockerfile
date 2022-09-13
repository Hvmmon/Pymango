FROM ubuntu:focal

RUN apt-get update && \
    apt-get install apt-utils && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.7 python3.7-dev python3.7-distutils python3-pip

WORKDIR /app
COPY requirements.txt .
RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.7 /usr/bin/python
RUN rm -f /usr/bin/python3 && ln -s /usr/bin/python3.7 /usr/bin/python3

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn==19.9.0

ADD ./pymango /app/pymango
ADD ./docker /app/docker
ADD ./ml /app/ml

RUN mkdir -p /app/pymango/pymango/static
