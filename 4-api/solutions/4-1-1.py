import requests
import pandas as pd
import numpy as np
import json
import streamlit as st

st.title('API Example API to Pandas')


uri = "https://jsonplaceholder.typicode.com/users/"

# Write your code here to call the API and display results in a dataframe


url ="https://jsonplaceholder.typicode.com/users/"
response = requests.get(url)
response.raise_for_status()#raise an error if the request failed
data = response.json()
st.write(data)

#users_df = pd.DataFrame(data)
df = pd.json_normalize(data)
st.dataframe(df)