import streamlit as st
import requests

# Backend API URL
API_URL = "https://chronic-kidney-disease-1-epqe.onrender.com/predict"

st.set_page_config(
    page_title="Chronic Kidney Disease Prediction",
    page_icon="🩺",
    layout="centered"
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

if st.button("🔍 Predict"):

    data = {
        "id": int(id),
        "sg": float(sg),
        "al": int(al),
        "pc": pc,
        "sod": float(sod),
        "hemo": float(hemo),
        "pcv": int(pcv),
        "rc": float(rc),
        "htn": htn,
        "dm": dm,
        "appet": appet,
        "pe": pe
    }

    try:
        response = requests.post(API_URL, json=data, timeout=60)

        if response.status_code == 200:

            result = response.json()

            if result["Prediction"] == "CKD":
                st.error("🚨 Patient has Chronic Kidney Disease (CKD)")
            else:
                st.success("✅ Patient does NOT have Chronic Kidney Disease")

            st.subheader("Prediction Details")

            st.write(f"**Prediction:** {result['Prediction']}")
            st.write(f"**CKD Probability:** {result['CKD Probability']}")
            st.write(f"**Not CKD Probability:** {result['Not CKD Probability']}")

        else:
            st.error(f"API Error: {response.status_code}")
            st.write(response.text)

    except Exception as e:
        st.error(f"Connection Error: {e}")
