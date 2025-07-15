import streamlit as st
import pandas as pd
import joblib 

model=joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud Detection Prediction App")
st.markdown("This app predicts whether a transaction is fraudulent or not based on the input features.")
st.markdown("Please enter the transaction details and use predict buttoons")

st.divider()

transaction_type=st.selectbox("Transaction Type", [ "PAYMENT", "TRANSFER","CASH_OUT"])
amount=st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg=st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig=st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalancedest=st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalancedest=st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

#to run it write this command  streamlit run fraud_detection.py


if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalancedest,
        "newbalanceDest": newbalancedest
        
    }])
    
    prediction = model.predict(input_data)[0]
    
    st.subheader(f"Prediction :'{int(prediction)}'" )  
    
    if prediction == 1:
       st.error("This transaction is likely to be fraudulent.")
    else:
         st.success("This transaction is likely to be legitimate.")   
