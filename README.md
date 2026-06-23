# Titanic Survival Prediction

An end-to-end Machine Learning Classification project that predicts passenger survival on the Titanic using a Decision Tree Classifier.

---

# Project Overview

This project demonstrates the complete Machine Learning workflow, starting from loading raw data to building, evaluating, and tuning a predictive model.

The objective is not only to build a classification model but also to understand every stage of the Machine Learning pipeline and follow industry best practices.

---

# Business Problem

Given passenger information such as age, gender, passenger class, fare, and embarkation details, predict whether the passenger survived the Titanic disaster.

This is a **Binary Classification** problem.

Target Variable:

* **0** → Not Survived
* **1** → Survived

---

# Dataset Information

* Dataset: Titanic Dataset (Kaggle)
* Total Records: 891
* Total Features: 11
* Target Variable: Survived

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook
* Git
* GitHub

---

# Machine Learning Workflow

1. Load Dataset
2. Dataset Overview
3. Exploratory Data Analysis (EDA)
4. Data Cleaning
5. Feature Selection
6. Train-Test Split
7. Data Preprocessing
8. Decision Tree Model
9. Model Evaluation
10. Hyperparameter Tuning
11. Feature Importance
12. Decision Tree Visualization

---

# Model Performance

The Decision Tree Classifier was trained using a preprocessing pipeline built with `ColumnTransformer` and `Pipeline`.

Evaluation Metrics:

* Accuracy Score
* Confusion Matrix
* Classification Report

Hyperparameter tuning was performed using **GridSearchCV**.

---

# Repository Structure

```text
Titanic-Survival-Prediction/
│
├── datasets/
├── notebooks/
├── README.md
├── requirements.txt
├── LICENSE
└── .github/
    └── workflows/
```

---

# Future Improvements

* Compare multiple classification algorithms.
* Perform feature engineering.
* Apply Cross Validation.
* Deploy the model using Flask or FastAPI.
* Containerize using Docker.
* Build an end-to-end CI/CD pipeline.

---

# Author

**Sumanth A**

Senior Infrastructure Engineer transitioning into Machine Learning and Artificial Intelligence through hands-on projects following industry-standard engineering practices.
