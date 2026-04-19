# 🏦 Loan Approval Prediction System

A Machine Learning-based web application that predicts whether a loan will be **approved or rejected** based on applicant details such as income, credit score, and assets.

This project is built using a trained ML model and deployed with **Streamlit** for an interactive and real-time prediction experience.

---

## 🚀 Overview

Loan approval is a critical decision-making process in financial institutions. This project automates that process using Machine Learning, reducing manual effort and improving decision speed.

Users provide their financial and personal details, and the system instantly predicts loan approval status.

---
🚀 Live Demo

🔗 Access the deployed app here:
👉 https://your-app-link.streamlit.app

## 🧠 Machine Learning Model

* **Algorithm Used**: Decision Tree Classifier
* **Library**: Scikit-learn
* **Preprocessing**: Feature Scaling using StandardScaler

Multiple models were tested during development:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Naive Bayes
* Support Vector Machine (SVM)
* Decision Tree (Final Selected Model)

👉 The **Decision Tree model** was selected due to its superior performance and interpretability.

---

## 📊 Model Performance

* **Accuracy**: **91%**

* **Precision**:

  * Class 0: 0.88
  * Class 1: 0.92

* **Recall**:

  * Class 0: 0.86
  * Class 1: 0.93

* **F1-Score**:

  * Class 0: 0.87
  * Class 1: 0.92

* **Overall Performance**:

  * Macro Avg F1-score: 0.90
  * Weighted Avg F1-score: 0.90

This indicates a well-balanced and reliable model for prediction.

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **Machine Learning**: Scikit-learn
* **Libraries**: NumPy, Joblib

---

## 📂 Project Structure

```
├── app.py              # Streamlit application
├── model_dt.pkl        # Trained Decision Tree model
├── scaler.pkl          # Feature scaler
├── README.md           # Documentation
```

---

## ⚙️ How It Works

* User inputs financial details
* Data is converted into numerical format
* Features are scaled using a trained scaler
* Model predicts loan approval status
* Result is displayed instantly

---

## 🧾 Input Features

* Number of Dependents
* Education
* Self Employment Status
* Annual Income
* Loan Amount
* Loan Term
* CIBIL Score
* Residential Assets Value
* Commercial Assets Value
* Luxury Assets Value
* Bank Asset Value

---

## 📈 Future Improvements

* Hyperparameter tuning for better accuracy
* Add feature importance visualization
* Deploy on cloud (Streamlit Cloud / Render)
* Add user authentication system
* Store prediction history

---
