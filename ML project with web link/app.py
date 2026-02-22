import streamlit as st
import joblib
import numpy as np

# file directory
file_dir = r"c:\Balaji\Balaji AI\New folder\Project\For Job\General\ML\\"
# Load model
model = joblib.load(file_dir + "linear_regression_model.pkl")

st.title("Linear Regression Prediction App")

feature1 = st.number_input("Enter Feature 1")
feature2 = st.number_input("Enter Feature 2")
feature3 = st.number_input("Enter Feature 3")
feature4 = st.number_input("Enter Feature 4")
feature5 = st.number_input("Enter Feature 5")
feature6 = st.number_input("Enter Feature 6")
feature7 = st.number_input("Enter Feature 7")
feature8 = st.number_input("Enter Feature 8")
feature9 = st.number_input("Enter Feature 9")
feature10 = st.number_input("Enter Feature 10")
feature11 = st.number_input("Enter Feature 11")
feature12 = st.number_input("Enter Feature 12")
feature13 = st.number_input("Enter Feature 13")

if st.button("Predict"):
    prediction = model.predict([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10, feature11, feature12, feature13]])
    st.success(f"Prediction: {prediction[0]}")