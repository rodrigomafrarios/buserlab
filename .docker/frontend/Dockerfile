FROM python:3.6

ENV HOST 0.0.0.0

RUN apt-get update --fix-missing && \
    apt-get install -y curl nano

RUN cd /tmp && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y nodejs