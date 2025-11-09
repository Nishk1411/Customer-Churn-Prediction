# 📞 Telecom Customer Churn Prediction App

[![Streamlit](https://img.shields.io/badge/Platform-Streamlit-blue?logo=streamlit)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow?logo=python)](https://www.python.org/)
[![Deployed App](https://img.shields.io/badge/Live_App-Open-green?logo=streamlit)](https://customer-churn-prediction-lam24bp6gqxgx6bhtg6cgf.streamlit.app/)

A simple and interactive **Streamlit web app** that predicts whether a telecom customer is likely to **churn** (leave the service) based on their account information and service usage.  
Built using **Python**, **Streamlit**, and an **XGBoost model** trained on customer data.

---

## 🚀 **Live Demo**
👉 **[Click here to use the app](https://customer-churn-prediction-lam24bp6gqxgx6bhtg6cgf.streamlit.app/)**

---

## 🧠 **Model Overview**
- **Model Used:** XGBoost Classifier  
- **Training Dataset:** Customer churn dataset (`data.csv`)  
- **Target Variable:** `Churn` (1 = churned, 0 = retained)  
- **Performance Metrics:** Accuracy, F1-score, ROC-AUC (achieved during notebook training)

---

## 💡 **App Features**
- Interactive UI built with **Streamlit**
- Input customer features such as:
  - Gender, Senior Citizen, Partner, Dependents  
  - Internet, Phone, and Streaming Services  
  - Contract type, Billing method, and Charges  
- Displays:
  - **Predicted Outcome:** Churn / No Churn  
  - **Prediction Probabilities**

---

## 📂 **Project Structure**
