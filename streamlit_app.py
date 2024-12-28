import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns


model = joblib.load('trained_model.pkl')

# إعداد الصفحات
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Upload Data", "Manual Input", "Visualizations"])

if page == "Upload Data":
    st.title("Upload Data for Churn Prediction")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.write(data.head())

        if st.button("Predict"):
            predictions = model.predict(data)
            data['Churn Prediction'] = predictions
            st.write("Predictions:")
            st.write(data)

elif page == "Manual Input":
    st.title("Manual Input for Churn Prediction")

    # إدخال القيم يدويًا
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    tenure = st.number_input("Tenure", min_value=0, max_value=100, value=1)
    Contract = st.selectbox("Contract", [0, 1, 2])  # افترض أن القيم المشفرة هي 0, 1, 2
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
        prediction = model.predict(input_data)
        st.write("Churn Prediction:", "Yes" if prediction[0] == 1 else "No")

elif page == "Visualizations":
    st.title("Data Visualizations")

    # مثال على التصورات
    st.write("Tenure Distribution")
    sns.histplot(df_encoded['tenure'], bins=30)
    st.pyplot(plt)

    st.write("Monthly Charges vs Churn")
    sns.boxplot(x=df_encoded['Churn'], y=df_encoded['MonthlyCharges'])
    st.pyplot(plt)
