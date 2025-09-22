import os
import requests
import streamlit as st
from sklearn.datasets import load_wine

API_URL = os.getenv("API_URL", "http://api:8000")

st.set_page_config(page_title="Wine Predictor", layout="centered")
st.title("Wine Class Prediction")

data = load_wine()
inputs = {}
st.subheader("Enter the signs")
for name in data.feature_names:
    col_idx = data.feature_names.index(name)
    default = float(data.data[:, col_idx].mean())
    inputs[name] = st.number_input(name, value=default)
    
if st.button("Predict"):
    try:
        resp = requests.post(f"{API_URL}/predict", json={"data": inputs}, timeout=10)
        resp.raise_for_status()
        pred = resp.json()["prediction"]
        st.success(f"Prediction class: {pred}")
    except Exception as e:
        st.error(f"Error: {e}")
