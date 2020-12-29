# Flask app demo project #
######This is a demo project that uses a flask app which connects to mysql server both hosted on kubernetes.<br />

To run this project execute below commands using [minikube](https://minikube.sigs.k8s.io/docs/start/).<br />

# minikube start <br />
# eval $(minikube docker-env) <br />
# cd Flask_/resources/ <br />

execute both deployment files inside mysql and flaskapp folders respectively using k8s. <br />
example : # kubectl create -f mysql-svc-deploy.yaml # this will deploy all the configuration for k8s cluster. <br />
 # minikube service flask-web-svc     # will deploy the service outside cluster uses host browser for access. <br/>


## Helm Chart commands =========================================================

######Execute below commands in minikube:
# cd Flask_
# minikube start <br />
# eval $(minikube docker-env) <br />
# cd Flask_/ <br />
# helm install flaskapp helmcharts/
#####To verify the deployment
# helm list
# kubectl get all
-----------------------------------------------------------------------------------------------------
