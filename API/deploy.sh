#!/bin/bash

eval "$(ssh-agent -s)" &&
ssh-add -k ~/.ssh/id_rsa &&
cd /home/ubuntu/deploy/project_e_commerce
git pull

source ~/.profile
echo "$DOCKERHUB_PASS" | docker login --username $DOCKERHUB_USER --password-stdin
sudo docker stop e_commerce
sudo docker rm e_commerce
sudo docker rmi dzinsyah/e_commerce
sudo docker run  -d --name e_commerce -p 8000:8000 -t dzinsyah/e_commerce:latest