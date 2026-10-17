import streamlit as st
import joblib


@st.cache_resource
def load_model():
    return joblib.load("model.joblib")


st.title("My Model Demo")
text = st.text_input("Enter text:")
if text:
    st.write("Prediction:", "stub-prediction")
