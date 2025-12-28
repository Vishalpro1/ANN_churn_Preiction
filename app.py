import streamlit as st
import numpy as np
import joblib
import tensorflow as tf

# ===============================
# Load model and scaler
# ===============================
model = tf.keras.models.load_model(r"C:\Users\hp\Downloads\ann_model.keras")
scaler = joblib.load(r"C:\Users\hp\Downloads\scaler.pkl")

st.title("-----Customer Churn Prediction (ANN)----")

# ===============================
# Input fields
# ===============================
CreditScore = st.number_input("Credit Score", min_value=300, max_value=900, value=650)

Geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
Gender = st.selectbox("Gender", ["Female", "Male"])

Age = st.number_input("Age", min_value=18, max_value=100, value=35)
Tenure = st.slider("Tenure (years)", 0, 10, 3)
Balance = st.number_input("Balance", min_value=0.0, value=50000.0)
NumOfProducts = st.selectbox("Number of Products", [1, 2, 3, 4])
HasCrCard = st.selectbox("Has Credit Card", ["Yes", "No"])
IsActiveMember = st.selectbox("Is Active Member", ["Yes", "No"])
EstimatedSalary = st.number_input("Estimated Salary", min_value=0.0, value=60000.0)

# ===============================
# Encoding (MUST match training)
# ===============================
geo_map = {"France": 0, "Spain": 1, "Germany": 2}
gender_map = {"Female": 0, "Male": 1}

# ===============================
# Prediction
# ===============================
if st.button("Predict Churn"):
    input_data = np.array([[
        CreditScore,
        geo_map[Geography],
        gender_map[Gender],
        Age,
        Tenure,
        Balance,
        NumOfProducts,
        1 if HasCrCard == "Yes" else 0,
        1 if IsActiveMember == "Yes" else 0,
        EstimatedSalary
    ]])

    # Debug (optional but safe)
    st.write("Input shape:", input_data.shape)

    # Scaling
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)
    prob = float(prediction[0][0])

    if prob > 0.5:
        st.error(f"❌ Customer WILL churn (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Customer will NOT churn (Probability: {prob:.2f})")
