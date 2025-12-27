# 🚀 Salary Prediction API  
### End-to-End Machine Learning Model Serving with FastAPI, Docker, Kubernetes (kind), and Helm

---

## 📌 Overview

This project demonstrates a **complete, real-world MLOps workflow** starting from **training a machine learning model** to **deploying and managing it on Kubernetes using Helm**.

The focus of this project is not only on building a machine learning model, but on **how ML models are actually deployed and served in production systems**.

You will learn:
- How model training and model serving are separated
- How FastAPI is used for inference
- How Docker packages ML applications
- How Kubernetes runs and scales services
- How Helm manages deployments, upgrades, and scaling

---

## 🧠 What this project does

- Trains a **Linear Regression** model to predict salary based on years of experience
- Saves the trained model as `model.pkl`
- Loads the model into a FastAPI application
- Exposes REST endpoints for prediction
- Packages the application into a Docker image
- Deploys the image to Kubernetes using Helm
- Scales and manages the application using Helm commands

---

## 🛠️ Prerequisites

Ensure the following tools are installed:

- Python 3.9+
- Docker
- kubectl
- kind (Kubernetes in Docker)
- Helm

---

## ▶️ How to run this project (Windows – PowerShell)

This section lists **all the commands** a user needs to run **after downloading this project** to fully start and run the application using **Docker, Kubernetes (kind), and Helm**.

> ⚠️ All commands below are for **Windows PowerShell**  

---

### 🧿 Clone the repository and move into project directory

```powershell
git clone <repository-url>
```

### 🧿 Build Docker image

```powershell
docker build -t salary-fastapi .
```

Verify image exists:

```powershell
docker images
```

### 🧿 Cleanup commands

Uninstall Helm release:
```powershell
helm uninstall salary-fastapi
```
Delete all Kubernetes resources:
```powershell
kubectl delete all --all
```

### 🧿 Verify cleanup

Check that the Helm release is removed:
```powershell
helm list
```

Check that all Kubernetes resources are deleted:
```powershell
kubectl get all
```

### 🧿 Deploy application using Helm

First, run a dry-run to verify Helm templates:
```powershell
helm template salary-fastapi helm/salary-fastapi
```

If YAML is rendered correctly, install the Helm release:
```powershell
helm upgrade --install salary-fastapi helm/salary-fastapi
```



### 🧿 Verify Kubernetes deployment

```powershell
helm list
kubectl get pods
kubectl get svc
```

### 🧿 Scale application using 

Scale up:
```powershell
helm upgrade salary-fastapi helm/salary-fastapi --set replicaCount=3
```

Scale down:
```powershell
helm upgrade salary-fastapi helm/salary-fastapi --set replicaCount=1
```

### 🧿 Verify scaling

Check the number of running pods:
```powershell
kubectl get pods
```

## ✅ Conclusion

This project showcases a **real-world ML deployment workflow**, covering model training, API-based serving, containerization, and Kubernetes deployment managed with Helm. It demonstrates how machine learning models are moved from experimentation to **scalable, production-ready services**.

Completing this project builds a strong foundation in **MLOps and ML engineering**, and serves as a solid portfolio example for deploying ML models using modern cloud-native tools.

