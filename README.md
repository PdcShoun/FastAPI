# FastAPI by Kubernetes

First create namespace
```
kubectl create ns python 
```
Run Run Run
```
kubectl apply -f kube.yaml -n python 
```
Get pod
```
kubectl get pods -n python
```
Don't forget to forward port
```
kubectl port-forward <my-app-name> 8000:8000
```
Stop
```
kubectl delete -f kube.yaml -n python
```