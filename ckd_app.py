import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("Chronic Kidney Disease.pkl")
encoders = joblib.load("label_encoders.pkl")

# Page settings
st.set_page_config(
    page_title="Chronic Kidney Disease Prediction",
    page_icon="🩺"
)

st.title("🩺 Chronic Kidney Disease Prediction")
st.write("Enter patient details to predict whether the patient has CKD or not.")

# User Inputs

id = st.number_input("Patient ID", min_value=0, value=101)

sg = st.number_input("Specific Gravity", value=1.020, format="%.3f")

al = st.selectbox("Albumin", [0, 1, 2, 3, 4, 5])

pc = st.selectbox("Pus Cell", ["normal", "abnormal"])

sod = st.number_input("Sodium", value=138.0)

hemo = st.number_input("Hemoglobin", value=14.5)

pcv = st.number_input("Packed Cell Volume", value=44)

rc = st.number_input("Red Blood Cell Count", value=5.2)

htn = st.selectbox("Hypertension", ["yes", "no"])

dm = st.selectbox("Diabetes Mellitus", ["yes", "no"])

appet = st.selectbox("Appetite", ["good", "poor"])

pe = st.selectbox("Pedal Edema", ["yes", "no"])


# Prediction
if st.button("🔍 Predict"):

    data = pd.DataFrame([{
        "id": id,
        "sg": sg,
        "al": al,
        "pc": pc,
        "sod": sod,
        "hemo": hemo,
        "pcv": pcv,
        "rc": rc,
        "htn": htn,
        "dm": dm,
        "appet": appet,
        "pe": pe
    }])

    # Encode categorical columns
    categorical_cols = [
        "pc",
        "htn",
        "dm",
        "appet",
        "pe"
    ]

    for col in categorical_cols:
        data[col] = encoders[col].transform(data[col])

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.error("🚨 Patient has Chronic Kidney Disease (CKD)")
    else:
        st.success("✅ Patient does NOT have Chronic Kidney Disease")