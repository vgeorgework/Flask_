This is a demo project that uses a flask app that connects to mysql server both is hosted on kubernetes.<br />
To run this project execute below commands using minikube.<br />
#minikube start <br />
#eval $(minikube docker-env) <br />
#cd Flask_/resources/ <br />

execute both deployment files inside mysql and flaskapp folders respectively using k8s. <br />
example : kubectl create -f mysql-svc-deploy.yaml # this will deploy all the configuration for k8s cluster. <br />
#minikube service flask-web-svc     # will deploy the service outside cluster uses host browser for access. <br/>

