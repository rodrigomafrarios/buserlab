#!/bin/sh
sudo cp ../docker-compose.prod.yaml /home/ubuntu/buserlab/docker-compose.prod.yaml
sudo docker-compose -f docker-compose.prod.yaml restart backend