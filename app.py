# Imports
import streamlit as st
from streamlit_chat import message
import requests

import regex as re

st.title("Chippy FastAPI")

# Streamlit input field
input_prompt = st.text_input("Enter a prompt", "What is a Large Language Model?")

data = {
    "input_prompt": input_prompt,
}

placeholder = st.empty()  # placeholder for latest message
message_history = []
message_history.append(input_prompt)

for j, message_ in enumerate(message_history):
    if j % 2 == 0:
        message(message_, is_user=True) # display all the previous message

#with placeholder.container():
#    message(message_history[-1]) # display the latest message

res = requests.post("http://localhost:8000/predict/", json=data)
cleaned_answer = re.sub("User:.+\n+Chip: ", "", res.json())
message(cleaned_answer)

## Generate output
#if st.button("Chip it!"):
#    res = requests.post("http://localhost:8000/predict/", json=data)
#    st.markdown(res.json())