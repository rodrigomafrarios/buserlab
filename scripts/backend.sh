#!/bin/sh
docker-compose -f docker-compose.prod.yaml backend restart
docker restart -f docker-compose.prod.yaml nginx restart