This repository contains code used for the following medium articles where we go through the deployment of a machine learning model on mlflow.

The code is organized in the following way:

├── deployments     <- Kubernets config yaml files for mlflow and locust 
├── locust-tasks    <- Functions executed as part of the load test tasks
├── notebooks       <- Example code snippets to interact with mlflow
└── scripts         <- Scripts executed by the deployed docker containers 
├── dockerfile_*    <- docker files to deploy on mlflow and locust on Kubernetes 
