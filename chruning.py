# -*- coding: utf-8 -*-
"""chruning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PZ-CE_u2HkPEMf8Q_I3I6sRPnyR1HfcB
"""


import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model('model.h5')

def predict(tenure, monthly_charges, total_charges, internet_service, online_security, device_protection, streaming_tv, tech_support, contract, payment_method):
    # Normalize the input data
    data = {
        'tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'DeviceProtection': device_protection,
        'StreamingTV': streaming_tv,
        'TechSupport': tech_support,
        'Contract': contract,
        'PaymentMethod': payment_method
    }

    # Make the prediction
    prediction = model.predict([list(data.values())])
    return prediction[0][0]

st.title('Churn Prediction App')

tenure = st.number_input('Tenure', min_value=0, max_value=100)
monthly_charges = st.number_input('Monthly Charges', min_value=0)
total_charges = st.number_input('Total Charges', min_value=0)
internet_service = st.selectbox('Internet Service', ['Fiber optic', 'DSL', 'No'])
online_security = st.selectbox('Online Security', ['Yes', 'No', 'No internet service'])
device_protection = st.selectbox('Device Protection', ['Yes', 'No', 'No internet service'])
streaming_tv = st.selectbox('Streaming TV', ['Yes', 'No'])
tech_support = st.selectbox('Tech Support', ['Yes', 'No'])
contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
payment_method = st.selectbox('Payment Method', ['Electronic check', 'Bank transfer', 'Credit card/debit card'])

if st.button('Predict Churn Probability'):
    prediction = predict(tenure, monthly_charges, total_charges, internet_service, online_security, device_protection, streaming_tv, tech_support, contract, payment_method)
    prediction_probability = prediction * 100
    st.success('Churn Probability: {}%'.format(prediction_probability))

