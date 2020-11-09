#!/bin/sh
docker-compose -f docker-compose.prod.yaml up -d backend
docker-compose -f docker-compose.prod.yaml up -d nginx
docker-compose -f docker-compose.prod.yaml restart backend
#docker-compose -f docker-compose.prod.yaml restart nginx