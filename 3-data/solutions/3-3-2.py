import streamlit as st
import pandas as pd
import requests
import numpy as np


base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/"
months = ['jan', 'feb', 'mar', 'apr']

st.title("Who's not Buying from MiniMart?")
month = st.selectbox('Select Month:', months)

purchases = pd.read_csv(f"{base}/purchases-{month}.csv")

# Code here...

customers = pd.read_csv(f"{base}/customers.csv")
combined = pd.merge(customers, purchases, left_on='customer_id', right_on= 'customer_id', how='left')
st.dataframe(combined)
cols= ['customer_id', 'firstname', 'lastname']
did_not_buy = combined["order_id"].isnull()
customers_who_did_not_buy = combined[did_not_buy][cols]
st.dataframe(customers_who_did_not_buy, hide_index=True)