# -----------------------------
# Streamlit App: Telecom Churn Prediction
# -----------------------------

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained XGBoost model
model = pickle.load(open("xgb_model.pkl", "rb"))

st.title("📞 Telecom Customer Churn Prediction")
st.markdown("""
Predict whether a customer is likely to churn based on their account and usage details.
""")

# -----------------------------
# Step 2: User Input
# -----------------------------
def user_input_features():
    gender = st.selectbox("Gender", ["Female", "Male"])
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Has Partner?", ["Yes", "No"])
    Dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)
    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
    Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check",
                                                    "Bank transfer (automatic)", "Credit card (automatic)"])
    MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, max_value=1000.0, value=70.0)
    TotalCharges = st.number_input("Total Charges", min_value=0.0, max_value=5000.0, value=1500.0)

    # Encode categorical features manually as done in preprocessing
    def encode_binary(val):
        return 1 if val in ["Yes", "Male"] else 0

    data = {
        'gender': encode_binary(gender),
        'SeniorCitizen': SeniorCitizen,
        'Partner': encode_binary(Partner),
        'Dependents': encode_binary(Dependents),
        'tenure': tenure,
        'PhoneService': encode_binary(PhoneService),
        'MultipleLines': 0 if MultipleLines in ["No", "No phone service"] else 1,
        'InternetService': 0 if InternetService=="No" else (1 if InternetService=="DSL" else 2),
        'OnlineSecurity': 0 if OnlineSecurity=="No" or OnlineSecurity=="No internet service" else 1,
        'OnlineBackup': 0 if OnlineBackup=="No" or OnlineBackup=="No internet service" else 1,
        'DeviceProtection': 0 if DeviceProtection=="No" or DeviceProtection=="No internet service" else 1,
        'TechSupport': 0 if TechSupport=="No" or TechSupport=="No internet service" else 1,
        'StreamingTV': 0 if StreamingTV=="No" or StreamingTV=="No internet service" else 1,
        'StreamingMovies': 0 if StreamingMovies=="No" or StreamingMovies=="No internet service" else 1,
        'Contract': 0 if Contract=="Month-to-month" else (1 if Contract=="One year" else 2),
        'PaperlessBilling': encode_binary(PaperlessBilling),
        'PaymentMethod': 0 if PaymentMethod=="Electronic check" else
                         (1 if PaymentMethod=="Mailed check" else (2 if PaymentMethod=="Bank transfer (automatic)" else 3)),
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges
    }

    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# -----------------------------
# Step 3: Make Prediction
# -----------------------------
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

st.subheader("Prediction")
st.write("Churn" if prediction[0]==1 else "No Churn")

st.subheader("Prediction Probability")
st.write(f"No Churn: {prediction_proba[0][0]:.2f}")
st.write(f"Churn: {prediction_proba[0][1]:.2f}")
