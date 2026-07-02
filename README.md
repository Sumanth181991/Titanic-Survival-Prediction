# 🩺 Breast Cancer Detection API

An end-to-end Machine Learning API that predicts whether a breast tumor is **Benign** or **Malignant** using the Breast Cancer Wisconsin Diagnostic Dataset.

This project demonstrates the complete Machine Learning deployment lifecycle—from data preprocessing and model training to Docker containerization and deployment on Microsoft Azure Container Apps.

---

# 🚀 Project Highlights

- End-to-End Machine Learning Pipeline
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing using Scikit-learn Pipeline
- FastAPI REST API
- Pydantic Request Validation
- Interactive Swagger Documentation
- Docker Containerization
- Azure Container Registry (ACR)
- Azure Container Apps Deployment
- Public HTTPS Endpoint
- Production-ready Project Structure

---

# 📌 Project Overview

Breast cancer is one of the most common cancers worldwide. Early diagnosis plays a critical role in improving patient survival and treatment outcomes.

This project uses the Breast Cancer Wisconsin Diagnostic Dataset to train a Machine Learning model capable of classifying breast tumors as either:

- Benign
- Malignant

The trained model is exposed through a FastAPI REST API, containerized using Docker, stored in Azure Container Registry, and deployed on Azure Container Apps.

---

# 🎯 Business Problem

Healthcare professionals often need fast and reliable predictions to assist in diagnosis.

The objective of this project is to build a production-ready Machine Learning API capable of predicting breast cancer diagnoses based on thirty diagnostic measurements obtained from digitized images of breast masses.

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.10 |
| Machine Learning | Scikit-learn |
| Data Analysis | Pandas |
| Numerical Computing | NumPy |
| Model Serialization | Joblib |
| API Framework | FastAPI |
| Data Validation | Pydantic |
| API Documentation | Swagger UI |
| Containerization | Docker |
| Cloud Registry | Azure Container Registry |
| Cloud Platform | Azure Container Apps |
| Version Control | Git |
| Repository Hosting | GitHub |

---

# 📂 Repository Structure

```text
Breast-Cancer-Detection-API
│
├── app
│   ├── main.py
│   ├── predictor.py
│   ├── schemas.py
│
├── model
│   ├── pipeline.joblib
│
├── notebooks
│
├── datasets
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚙️ Machine Learning Workflow

```
Dataset
    │
    ▼
Data Cleaning
    │
    ▼
Exploratory Data Analysis
    │
    ▼
Feature Engineering
    │
    ▼
Train/Test Split
    │
    ▼
Pipeline Creation
    │
    ▼
Model Training
    │
    ▼
Model Evaluation
    │
    ▼
pipeline.joblib
    │
    ▼
FastAPI
    │
    ▼
Docker
    │
    ▼
Azure Container Apps
```

---

# 🏗️ Application Architecture

```
Client
   │
   ▼
FastAPI REST API
   │
   ▼
Pydantic Validation
   │
   ▼
Prediction Pipeline
   │
   ▼
Machine Learning Model
   │
   ▼
Prediction Response
```

---

# ☁️ Cloud Deployment Architecture

```
GitHub Repository
        │
        ▼
Docker Build
        │
        ▼
Docker Image
        │
        ▼
Azure Container Registry
        │
        ▼
Azure Container Apps
        │
        ▼
Public HTTPS Endpoint
```

---

# 🌐 REST API Endpoints

## Home

```
GET /
```

Returns

```json
{
  "message": "Breast Cancer Prediction API is running"
}
```

---

## Prediction

```
POST /predict
```

Accepts thirty diagnostic features and returns the predicted class.

---

## Swagger Documentation

```
/docs
```

Interactive API documentation generated automatically by FastAPI.

---

# 🐳 Docker Deployment

Build the Docker image

```bash
docker compose build
```

Run the application

```bash
docker compose up
```

Verify the running container

```bash
docker ps
```

---

# ☁️ Azure Deployment

Deployment Workflow

```
Local Machine
      │
      ▼
Docker Build
      │
      ▼
Azure Container Registry
      │
      ▼
Azure Container Apps
      │
      ▼
Public REST API
```

Deployment includes:

- Azure Container Registry
- Azure Container Apps
- HTTPS Endpoint
- Swagger UI
- Azure Log Analytics

---

# 📊 Machine Learning Pipeline

The project uses a Scikit-learn Pipeline to ensure consistent preprocessing and prediction during both training and inference.

Pipeline stages include:

- Data preprocessing
- Feature transformation
- Model prediction

The complete pipeline is serialized using Joblib.

---

# 📈 Model Features

The model predicts breast cancer using thirty numerical diagnostic measurements including:

- Mean Radius
- Mean Texture
- Mean Perimeter
- Mean Area
- Mean Smoothness
- Mean Compactness
- Mean Concavity
- Mean Symmetry

...and twenty-two additional diagnostic measurements.

---

# 📸 Screenshots

Add screenshots for:

- Dataset Overview
- Exploratory Data Analysis
- Model Training
- Swagger UI
- Docker Container
- Azure Container Registry
- Azure Container Apps
- Successful Prediction Response

---

# 🚀 Future Improvements

- Model Versioning
- CI/CD using GitHub Actions
- Automated Azure Deployment
- Azure Application Insights
- Logging
- Monitoring
- Authentication
- Rate Limiting
- Unit Testing
- Integration Testing
- Multiple Model Support

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

- End-to-End Machine Learning
- Model Serialization
- REST API Development
- FastAPI
- Pydantic
- Docker
- Azure Container Registry
- Azure Container Apps
- Cloud Deployment
- Git & GitHub
- Production-ready Project Structure

---

# 👨‍💻 Author

**Sumanth**

Senior Infrastructure Engineer | Azure | DevOps | Machine Learning Enthusiast

GitHub:
https://github.com/Sumanth181991

---

# ⭐ If you found this project useful, consider giving it a star.