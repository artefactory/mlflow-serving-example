### Mlflow serving example

This repository contains code used in [this series of articles](https://medium.com/artefact-engineering-and-data-science/serving-ml-models-at-scale-using-mlflow-on-kubernetes-bf27258775e7)
 in which we go through the deployment of a machine learning model on mlflow.


The code is organized in the following way:
```
├── deployments     <- Kubernets config yaml files for mlflow and locust 
├── locust-tasks    <- Functions executed as part of the load test tasks
├── notebooks       <- Example code snippets to interact with mlflow
├── scripts         <- Scripts executed by the deployed docker containers 
├── dockerfile_*    <- docker files to deploy mlflow and locust on Kubernetes 
```
### How to contribute ?
All contributions, ideas and bug reports are welcome! We encourage you to open an issue for any change you would like to make on this project.

