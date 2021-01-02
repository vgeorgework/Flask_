# Flask app demo project #
#### This is a demo project that uses a flask app which connects to mysql server both hosted on kubernetes.

###### To run this project execute below commands using [minikube](https://minikube.sigs.k8s.io/docs/start/).<br />

```
# minikube start
# eval $(minikube docker-env)
# cd Flask_/resources/ 
```

Execute both deployment files inside mysql and flaskapp folders respectively using k8s. <br />
Example :`# kubectl create -f mysql-svc-deploy.yaml ` this will deploy all the configuration for k8s cluster. <br />
`# minikube service flask-web-svc`     # will deploy the service outside cluster uses host browser for access. <br/>

## Helm Chart commands 

###### Execute below commands in minikube: 
```
# minikube start
# eval $(minikube docker-env)
# cd Flask_/ 
# helm install flaskapp helmcharts/
# minikube service flask-web-svc
```
## To verify the deployment:
```
# helm list 
# kubectl get all 
```
## To run helm chart with dynamic values:
```
# helm install --set db.username=testuser,db.password=user@123 flaskapp helmcharts/
```


