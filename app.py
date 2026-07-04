import streamlit as st
import pandas as pd
import joblib
import sklearn

# Load saved model
model = joblib.load("credit_risk_model.pkl")

# Title
st.title("🏦 Credit Risk Prediction")

st.write("Enter applicant details to predict credit risk.")

age = st.number_input("Age", min_value = 18, max_value = 100, value = 25)
income = st.number_input("Income", min_value= 0, value = 50000)
home = st.selectbox("Home Ownership",["Rent", "Own", "Mortgage", "Other"])
emp_length = st.number_input("Employement Length (Years)", value = 5)
intent = st.selectbox(
    "Loan Purpose",["Personal", "Education", "Medical", "Venture", "Debt Consolidation", "Home Improvement"])
amount = st.number_input("Loan Amount",min_value= 0 ,value = 10000)
rate = st.number_input("Interest Rate",min_value= 0.0, value = 12.5)
percent_income = st.number_input("Percent Income",min_value= 0.0, max_value= 1.0, value = 0.20, step = 0.01)
default = st.selectbox("Previous Default", ["No","Yes"])
cred_length = st.number_input("Credit History Length", min_value= 0, value = 5)

# Prediction
if st.button("Predict"):

    input_df = pd.DataFrame({
        "Age":[age],
        "Income":[income],
        "Home":[home],
        "Emp_length":[emp_length],
        "Intent":[intent],
        "Amount":[amount],
        "Rate":[rate],
        "Percent_income":[percent_income],
        "Default":[default],
        "Cred_length":[cred_length]
    })


    prediction = model.predict(input_df)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Credit Risk")
    else:
        st.success("✅ Low Credit Risk")

    # show entered details
    with st.expander("📄 View Applicant Details"):
        st.dataframe(input_df, use_container_width=True)    

    