#!/bin/sh
#To execute this script the host machine needs to installed minikube, helm, git and kubectl
minikube start
eval $(minikube docker-env)
git clone https://github.com/vgeorgework/Flask_.git
cd Flask_
git checkout helmchart
helm install --set db.username=testuser,db.password=user@123 flaskapp helmcharts/
kubectl get all
echo "sleeper executed for around 2 mins for cluster creation............................................................."
sleep 5
echo " you can abort this step and have the control or you can wait for some time while we create the cluster......................................................"
sleep 5
echo "checking the pod status................................................................"
kubectl get po
sleep 5
echo "depending upon your connection it may take less time ..............................................................."
sleep 10
echo "checking the pod status again ! ................................................................ "
kubectl get po
sleep 20
kubectl get all
sleep 1m
echo "checking with kubectl get all ...................................................... "
sleep 5
kubectl get all
echo "executing service command in minikube ..................................................................."
sleep 5
minikube service flask-web-svc
