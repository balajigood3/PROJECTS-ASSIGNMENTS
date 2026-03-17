import streamlit as st
import pickle
import pandas as pd
import requests

df = pd.read_csv(r"C:\Balaji - AI Course\AI\AI Coding Practice\Salary_dataset.csv")
st.title("Salary Prediction")
st.subheader("Dataset Preview")
st.write(df)
st.line_chart(df["Salary"])
st.bar_chart(df["YearsExperience"])
st.area_chart(df["Salary"])
st.scatter_chart(df[["YearsExperience","Salary"]])

st.subheader("Salary Trend")
st.line_chart(df["Salary"])

st.title("AI Salary Prediction")

exp = st.number_input("Enter your experience", min_value=0.0, step=0.5)

if st.button("Predict Salary"):
    # Ensure there is a colon :8000 before the /predict
    url = f"http://127.0.0.1:8000/predict?exp={exp}"
    response = requests.get(url)
    data = response.json()
    st.success(f"Predicted Salary: {data['prediction']}")