FROM python:3.6

RUN apt-get update --fix-missing && \
    apt-get install -y curl vim nano git locales zip unzip wget && \
    pip install uwsgi uwsgitop

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz


# Replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \
    echo "export LS_OPTIONS='--color=auto'" >>~/.bashrc && \
    echo "eval "\`dircolors\`"" >>~/.bashrc && \
    echo "alias ls='ls \$LS_OPTIONS'" >>~/.bashrc && \
    echo "alias ll='ls \$LS_OPTIONS -l'" >>~/.bashrc && \
    echo "alias l='ls \$LS_OPTIONS -lA'" >>~/.bashrc


#install env dependencies
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

WORKDIR /api
COPY ./backend/requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade django
RUN pip3 install django-cors-headers
RUN pip3 install djangorestframework


ENV SHELL=/bin/bash PYTHONUNBUFFERED=1 PYTHONIOENCODING=UTF-8 LANG=en_US.UTF-8 DJANGO_STATIC_ROOT=/dkdata/static UWSGI_PROCESSES=3 HOST=0.0.0.0 API_BASE_URL=http://localhost:8000