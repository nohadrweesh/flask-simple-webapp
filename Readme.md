# Run the app using docker

- docker build -t flask-simple-webapp .
- docker run -p 8081:8080 -e APP_COLOR=blue flask-simple-webapp

# Use dockerized version with Kubernetes

- k apply -f configmap.yml 
- k apply -f pod_definition.yaml 