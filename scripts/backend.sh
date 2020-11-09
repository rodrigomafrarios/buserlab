#!/bin/sh
sudo cp /home/ubuntu/docker-compose.prod.yaml /hom/ubuntu/buserlab/docker-compose.prod.yaml
sudo docker-compose -f docker-compose.prod.yaml restart backend