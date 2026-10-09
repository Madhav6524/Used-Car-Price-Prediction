# 🚗 Used Car Price Prediction System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-FF4B4B?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-MLPRegressor-F7931E?style=for-the-badge&logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

An end-to-end Machine Learning web application designed to estimate used car prices based on vehicle specifications, historical market data, and feature engineering. Built using **Artificial Neural Networks (MLPRegressor)**, **Scikit-Learn Pipelines**, and an interactive **Streamlit UI**.

---

## 📌 Project Overview

Determining the accurate market value of a pre-owned vehicle involves evaluating multiple complex variables such as age, mileage, engine capacity, power output, brand reputation, and transmission type. 

This project processes processed CarDekho vehicle data, cleans and imputes missing attributes, trains an **Artificial Neural Network (ANN / Multi-Layer Perceptron)** regression model, and serves an interactive web dashboard where buyers and sellers can input car specifications to receive instant price estimates in Indian Rupees (₹).

---

## ✨ Key Features

- **Interactive Streamlit Web Interface**: Seamless user controls including sidebar selectors, sliders, and dynamic inputs.
- **Dynamic Specification Filtering**: Interactive filtering based on brand and specific car models.
- **Scikit-Learn Pipeline Integration**: Integrated feature encoding (`OneHotEncoder`), feature scaling (`StandardScaler`), and preprocessing into a serialized model pipeline (`ann_model.pkl`).
- **Artificial Neural Network (ANN)**: Multi-Layer Perceptron Regressor trained with custom hidden layer architectures `(128, 64, 32, 16)` for high-accuracy non-linear regression.
- **Real-Time Price Estimation**: Instantly calculates and displays estimated car resale prices.

---

## 🛠️ Technology Stack

- **Frontend & Web Framework**: [Streamlit](https://streamlit.io/)
- **Machine Learning**: [Scikit-Learn](https://scikit-learn.org/) (`MLPRegressor`, `Pipeline`, `ColumnTransformer`, `OneHotEncoder`, `StandardScaler`)
- **Data Manipulation**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Model Serialization**: `joblib`
- **Environment**: Python 3.9+ / Jupyter Notebook

---

## 📂 Repository Structure

```text
.
├── cardekho.py              # Interactive Streamlit Web Application
├── car_main.ipynb           # Data Preprocessing, EDA & Model Training Notebook
├── cardekho_imputated.csv   # Preprocessed CarDekho Dataset
├── ann_model.pkl            # Trained Scikit-Learn ANN Pipeline Model
├── requirements.txt         # Project Dependencies
├── .gitignore               # Git Ignore Rules
└── README.md                # Project Documentation
```

---

## 📊 Dataset Features & Specifications

The machine learning model uses the following key vehicle features:

| Feature Name | Type | Description |
| :--- | :--- | :--- |
| `brand` | Categorical | Manufacturer brand (e.g., Maruti, Hyundai, BMW) |
| `model` | Categorical | Specific vehicle model name |
| `vehicle_age` | Numerical | Age of the vehicle in years |
| `km_driven` | Numerical | Total distance driven in kilometers |
| `seller_type` | Categorical | Individual, Dealer, or Trustmark Dealer |
| `fuel_type` | Categorical | Petrol, Diesel, CNG, LPG, Electric |
| `transmission_type` | Categorical | Manual or Automatic |
| `mileage` | Numerical | Fuel efficiency in km/l |
| `engine` | Numerical | Engine displacement in CC |
| `max_power` | Numerical | Maximum engine power output in HP |
| `seats` | Categorical | Seating capacity |

---

## ⚡ Quickstart Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Madhav6524/Used-Car-Price-Prediction.git
cd Used-Car-Price-Prediction
```

### 2. Create and Activate Virtual Environment (Recommended)
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the Streamlit Web App
```bash
streamlit run cardekho.py
```
Open your browser at `http://localhost:8501` to use the application.

---

## 🧠 Model Architecture & Training

The Artificial Neural Network model architecture comprises:
- **Preprocessing ColumnTransformer**:
  - One-Hot Encoding for categorical features (`brand`, `model`, `fuel_type`, `transmission_type`, `seller_type`) with unknown category handling.
  - Standard Scaling for numerical features (`vehicle_age`, `km_driven`, `mileage`, `engine`, `max_power`, `seats`).
- **ANN Architecture (`MLPRegressor`)**:
  - Hidden Layers: `(128, 64, 32, 16)` neurons
  - Activation Function: `relu`
  - Optimizer: `adam` (Learning rate init: `0.005`)
  - Max Iterations: `1000`

---

## 🤝 Author & Contact

**Madhav Patel**  
📧 Email: [madhav.20ff@gmail.com](mailto:madhav.20ff@gmail.com)  

---
*If you find this repository helpful, feel free to give it a ⭐ star!*
