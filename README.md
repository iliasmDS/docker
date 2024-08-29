# CREATING THE DOCKER IMAGE

docker build -t imougios/unipi:dashboard_app .

# PUSHING THE DOCKER IMAGE

docker login

docker push imougios/unipi:dashboard_app

# PULLING THE DOCKER IMAGE

docker pull imougios/unipi:dashboard_app

# DOCKER COMPOSE

docker-compose up

# KUBERNETES ORCHESTRATION

minikube start

kubectl apply -f mongo-deployment.yml

kubectl apply -f app-deployment.yml

kubectl get pods

kubectl get services

minikube dashboard
