#!/bin/sh
sudo docker pull rodrigomafra/buserlab_backend
sudo docker pull rodrigomafra/buserlab_nginx
sudo docker pull rodrigomafra/buserlab_postgres
sudo cp ../docker-compose.prod.yaml /home/ubuntu/buserlab/docker-compose.prod.yaml
sudo docker-compose -f docker-compose.prod.yaml restart backend