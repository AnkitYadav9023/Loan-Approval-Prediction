import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('model_dt.pkl')
scaler = joblib.load('scaler.pkl')

# Page config
st.set_page_config(page_title="Loan Approval Predictor", page_icon="🏦", layout="centered")

st.title("🏦 Loan Approval Prediction")
st.markdown("Fill in the details below to check loan approval status.")
st.divider()

# Input form
with st.form("loan_form"):
    col1, col2 = st.columns(2)

    with col1:
        no_of_dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, step=1)
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["No", "Yes"])
        income_annum = st.number_input("Annual Income (₹)", min_value=0.0, step=10000.0)
        loan_amount = st.number_input("Loan Amount (₹)", min_value=0.0, step=10000.0)
        loan_term = st.number_input("Loan Term (months)", min_value=1, max_value=360, step=1)

    with col2:
        cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, step=1)
        residential_assets_value = st.number_input("Residential Assets Value (₹)", min_value=0.0, step=10000.0)
        commercial_assets_value = st.number_input("Commercial Assets Value (₹)", min_value=0.0, step=10000.0)
        luxury_assets_value = st.number_input("Luxury Assets Value (₹)", min_value=0.0, step=10000.0)
        bank_asset_value = st.number_input("Bank Asset Value (₹)", min_value=0.0, step=10000.0)

    submitted = st.form_submit_button("🔍 Predict Loan Approval", use_container_width=True)

# Prediction
if submitted:
    try:
        education_val = 1 if education == "Graduate" else 0
        self_employed_val = 1 if self_employed == "Yes" else 0

        data = np.array([[
            no_of_dependents,
            education_val,
            self_employed_val,
            income_annum,
            loan_amount,
            loan_term,
            cibil_score,
            residential_assets_value,
            commercial_assets_value,
            luxury_assets_value,
            bank_asset_value
        ]])

        data_scaled = scaler.transform(data)
        prediction = model.predict(data_scaled)[0]

        st.divider()
        if prediction == 1:
            st.success("## ✅ Loan Approved!")
            st.balloons()
        else:
            st.error("## ❌ Loan Rejected!")

    except Exception as e:
        st.warning(f"⚠️ Error: {str(e)}")