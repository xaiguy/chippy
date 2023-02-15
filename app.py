# Imports
import streamlit as st
import requests

st.title("Chippy FastAPI")

# Streamlit input field
input_prompt = st.text_input("Enter a prompt", "What is a Large Language Model?")

data = {
    "input_prompt": input_prompt,
}

# Generate output
if st.button("Chip it!"):
    res = requests.post("http://localhost:8000/predict/", json=data)
    st.markdown(res.json())