# Spam Detector Project

Welcome to the Spam Detector project! This project aims to classify emails as either 'spam' or 'ham' using machine learning techniques. Below is a detailed guide on each of the project's components.

## Table of Contents

1. [Data Cleaning](#1-data-cleaning)
2. [Exploratory Data Analysis (EDA)](#2-eda)
3. [Text Preprocessing](#3-text-preprocessing)
4. [Model Building](#4-model-building)
5. [Evaluation](#5-evaluation)
6. [Improvement](#6-improvement)
7. [Website](#7-website)
8. [Deployment](#8-deployment)

---

### 1. Data Cleaning

In this step, we perform cleaning operations on the dataset to ensure it is ready for analysis. We handle missing values, remove duplicates, and perform any necessary transformations.

### 2. Exploratory Data Analysis (EDA)

EDA involves visualizing and understanding the characteristics of the dataset. Using libraries like `numpy`, `pandas`, `matplotlib`, and `seaborn`, we generate insightful plots and summary statistics.

### 3. Text Preprocessing

Text preprocessing involves preparing the text data for model training. We use the `nltk` library for tasks such as tokenization, removing stopwords, and performing stemming or lemmatization.

### 4. Model Building

In this phase, we apply various machine learning models to train on the preprocessed data. The models used are:
- Support Vector Classifier (SVC)
- K-Nearest Neighbors (KN)
- Naive Bayes (NB)
- Decision Tree Classifier (DT)
- Logistic Regression (LR)
- Random Forest Classifier (RF)
- AdaBoost Classifier (AdaBoost)
- Bagging Classifier (BgC)
- Extra Trees Classifier (ETC)
- Gradient Boosting Decision Tree (GBDT)
- XGBoost (xgb)

### 5. Evaluation

We evaluate the performance of each model using appropriate metrics. The best performing model will be selected for deployment.

### 6. Improvement

Based on the evaluation results, we may fine-tune hyperparameters or try advanced techniques to enhance the model's performance.

### 7. Website

An HTML page (`index.html`) has been created to provide a user-friendly interface for the spam detector.

### 8. Deployment

The final step involves deploying the model. We save the trained model as `model.joblib` and the vectorizer as `vectorizer.joblib` for later use.

---

## Usage

To get started with the project, follow the instructions below:

### Installation

```bash
pip install -r requirements.txt
```

### Running the App

```bash
python app.py
```

This command starts the Flask application, allowing you to access the spam detector through the web interface.

---


