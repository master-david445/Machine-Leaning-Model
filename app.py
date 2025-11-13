import streamlit as st
import numpy as np
import joblib

st.title("My ML Model App")
st.write("This app predicts an output using a trained ML model.")

# Load model safely
@st.cache_resource
def load_model():
    try:
        model = joblib.load("model.pkl")   # Make sure model.pkl is in the same folder
        return model
    except:
        st.error("Model file not found. Upload 'model.pkl' to the project directory.")
        return None

model = load_model()

# Input section
st.subheader("Enter input values")
input_value = st.number_input("Input value", value=0.0)

# Predict button
if st.button("Predict"):
    if model is None:
        st.error("Model not loaded.")
    else:
        input_array = np.array([[input_value]])
        prediction = model.predict(input_array)
        st.success(f"Prediction: {prediction[0]}")
