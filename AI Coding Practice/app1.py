import streamlit as st
import requests
import datetime

st.title("💰 AI Salary Prediction SaaS")

# session history
if "history" not in st.session_state:
    st.session_state.history = []

exp = st.number_input("Enter Years of Experience", min_value=0.0)

if st.button("Predict Salary"):

    url = f"http://127.0.0.1:8000/predict?exp={exp}"
    response = requests.get(url)
    result = response.json()

    salary = result["prediction"]

    # store history
    record = {
        "experience": exp,
        "salary": salary,
        "time": str(datetime.datetime.now())
    }

    st.session_state.history.append(record)

    st.success(f"Predicted Salary: ₹{salary:.2f}")

# show history
st.subheader("📜 Prediction History")

for item in st.session_state.history:
    st.write(
        f"Exp: {item['experience']} → ₹{item['salary']:.2f} at {item['time']}"
    )