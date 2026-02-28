import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Salary Prediction")

    st.write("We need some information")

    countries = le_country.classes_
    educations = le_education.classes_

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", educations)
    experience = st.slider("Years of Professional Experience", 0, 50, 5)

    if st.button("Predict Salary"):
        country_encoded = le_country.transform([country])[0]
        education_encoded = le_education.transform([education])[0]

        X = np.array([[country_encoded, education_encoded, experience]])

        salary = regressor.predict(X)

        st.subheader(f"The estimated salary is ${salary[0]:,.0f}")

