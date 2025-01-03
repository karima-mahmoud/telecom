import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Upload Data", " Input to prediction"])

if page == "Upload Data":
    st.title("Upload and Visualize Data")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.write(data.head())

        st.write("Tenure Distribution")
        plt.figure(figsize=(10, 6))
        sns.histplot(data['tenure'], bins=30)
        st.pyplot(plt)

        st.write("Monthly Charges vs Churn")
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=data['Churn'], y=data['MonthlyCharges'])
        st.pyplot(plt)

elif page == "Manual Input":
    st.title("Manual Input for Churn Prediction")

 
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    tenure = st.number_input("Tenure", min_value=0, max_value=100, value=1)
    Contract = st.selectbox("Contract", [0, 1, 2])  
    PaperlessBilling = st.selectbox("Paperless Billing", [0, 1])
    MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, max_value=1000.0, value=0.0)
    TotalCharges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=0.0)

    if st.button("Predict"):
        input_data = pd.DataFrame({
            'SeniorCitizen': [SeniorCitizen],
            'tenure': [tenure],
            'Contract': [Contract],
            'PaperlessBilling': [PaperlessBilling],
            'MonthlyCharges': [MonthlyCharges],
            'TotalCharges': [TotalCharges]
        })

        #input_data = input_data.astype(float)

        prediction = model.predict(input_data)
        st.write("Churn Prediction:", "Yes" if prediction[0] == 1 else "No")
