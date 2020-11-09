#!/bin/sh
cp /home/ubuntu/docker-compose.prod.yaml .
docker-compose -f docker-compose.prod.yaml backend restart
docker restart -f docker-compose.prod.yaml nginx restart