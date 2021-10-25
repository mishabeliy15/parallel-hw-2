#!/bin/bash

eval $(minikube docker-env)
docker build -t mishabeliy15/hw2 .
kubectl apply -f deployment.yaml

#minikube kubectl -- expose deployment hw2 --type=NodePort --port=5000
kubectl create -f service.yaml

minikube kubectl -- get service

#minikube service hw2