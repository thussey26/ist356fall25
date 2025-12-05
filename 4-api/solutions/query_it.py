import pandas as pd
import requests
import streamlit as st

APIKEY = "ec25dc1e1297cfba51838bd3"
st.title("Query It")

file = st.file_uploader("Upload a CSV file", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.write(df)
    
    # message sent to the AI model. This builds the prompt 
    question = st.text_input("Enter a question to ask about the data:")
    if question:
        prompt = 'With the following data:\n'
        prompt += df.to_string(index=False) # converted to text form (no row numbers),
        prompt += "\n\n"
        prompt += "Answer the following question:\n"    
        prompt += question
        
        url = "https://cent.ischool-iot.net/api/genai/generate"
        response = requests.post(url, data={"query": prompt}, headers={"X-API-KEY": APIKEY}) 
        response.raise_for_status()
        results = response.json()
        st.write(results)  