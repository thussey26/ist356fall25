import requests
import json
import pandas as pd
import streamlit as st

st.title("Employee JSON")

link = "https://raw.githubusercontent.com/mafudge/datasets/master/json-samples/employees.json"
response = requests.get(link)


st.write(employees)
employees_df = pd.json_normalize(employees)
employees_df = pd.json_normalize(employees, record_path=['employees'], meta=['dept'])
st.dataframe(employees_df)