import streamlit as st
import pandas as pd
import requests
import numpy as np



st.title("Excel to JSON")

uploaded_file = st.file_uploader("Upload an EXCEL file", type=["xlsx"]) # for only Excel files

if uploaded_file:
    df = pd.read_excel(uploaded_file.getvalue()) #read and return bytes
    st.dataframe(df) #display the dataframe
    
    json_file = df.to_json(orient="records", index=False) #convert df to json, each row will be a json object, exclude index
    json_filename = uploaded_file.name.split(".")[0] + ".json" #generate a file name mydata.xlsx becomes mydata.json
    download = st.download_button(f"Download {json_filename}", data=json_file, file_name=json_filename)

# Describe the code above 
