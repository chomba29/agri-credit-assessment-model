import streamlit as st
import pandas as pd
from predict.py import predict_default_probability, make_decision

st.title("Loan Default Prediction System")

st.header("Enter Applicant Information")

# Create input form
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 80, 35)
    months_mobile = st.number_input("Months as mobile user", 0, 120, 24)
    transaction_volume = st.number_input("Transaction volume (6mo USD)", 0, 150000, 1500)
    # ... add all 26 features

# Create DataFrame from inputs
applicant_data = pd.DataFrame({
    'age': [age],
    'months_as_mobile_user': [months_mobile],
    # ... all 26 features
})

if st.button("Predict Default Risk"):
    prob = predict_default_probability(applicant_data)[0]
    risk, decision = make_decision(prob)
    
    st.success(f"Default Probability: {prob:.2%}")
    st.info(f"Risk Level: {risk}")
    st.warning(f"Decision: {decision}")