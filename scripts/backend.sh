#!/bin/sh
cp /home/ubuntu/docker-compose.prod.yaml /hom/ubuntu/buserlab/docker-compose.prod.yaml
docker-compose -f docker-compose.prod.yaml restart backend