# Parallel and Distributed computing: HW № 2
## To run container:
- `docker build -t hw2 .`
- `docker run -it -p 5000:5000 hw2`
## To factorize number:
- `curl --location --request GET 'localhost:5000/factorize?n=100&x=38' \`
- n = max simple number
- x = number to factorize
## Build && Deploy:
- `./deploy.sh` - deploy
- `minikube service hw2` - get IP of service
## High load:
- `./high-load.sh 10000 "http://127.0.0.1:52446/factorize?n=10000000&x=66786756778"`