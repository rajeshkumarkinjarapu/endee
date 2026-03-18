import streamlit as st
from src.rag_pipeline import generate_response

st.set_page_config(page_title="AI Crop Advisor", layout="centered")

st.title("🌱 AI Crop Advisor")
st.write("Enter soil and weather details to get crop recommendation")

# Inputs
N = st.number_input("Nitrogen (N)", min_value=0.0)
P = st.number_input("Phosphorus (P)", min_value=0.0)
K = st.number_input("Potassium (K)", min_value=0.0)
temp = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("pH")
rainfall = st.number_input("Rainfall (mm)")

# Button
if st.button("Get Recommendation"):

    input_data = [N, P, K, temp, humidity, ph, rainfall]

    result = generate_response(input_data)

    st.success("✅ Recommendation Generated")

    st.text(result)