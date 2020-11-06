#!/bin/sh
./manage.py migrate --noinput
DJANGO_DEBUG=1 ./manage.py runserver 0.0.0.0:8000