# FastAPI by Kubernetes

First create namespace
```
kubectl create ns python 
```
Run Run Run
```
kubectl apply -f kube.yaml -n python 
```
Stop
```
kubectl delete -f kube.yaml -n python
```