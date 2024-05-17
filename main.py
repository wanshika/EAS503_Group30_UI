import streamlit as st
import json
import requests


st.title('Stock Prediction Model')

# add sub title
st.header("Group 30")
st.header("Members: ")
st.subheader("Wanshika Patro")
st.subheader("Ashutosh Panigrahi")
st.subheader("Samidha Bhosale")
st.subheader("Nachiket Dabhade")


# Sidebar
st.sidebar.title('Input Features')

input_example = {
  "G_Open": 111.16,
  "G_High": 113.77,
  "G_Close": 112.03,
  "G_Low": 110.72,
  "Google_Volume": 23922.0,
  "A_Open": 134.79,
  "A_High": 137.76,
  "A_Close": 135.35,
  "A_Low": 133.91,
  "Apple_Volume": 73409.2
}

inputs = {}
for key in input_example.keys():
    inputs[key] = st.sidebar.text_input(key,input_example[key])


# When the user clicks the predict button, the model will be called

if st.sidebar.button('Predict'):
    response = requests.post('http://143.198.24.173.8080:8080/inference', json=inputs)
    prediction = response.json()
    
    st.write(f"Prediction: ,{prediction['prediction']}")

    
