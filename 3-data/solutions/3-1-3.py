import streamlit as st
import pandas as pd
import numpy as np

st.title('Customers')
customers = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv')
st.dataframe(customers)



radio = st.radio('Gender:', options=['M', 'F'], index =0) # M as the default
cols = st.multiselect('Columns:', options=customers.columns) # select columns
gender_index = customers['Gender'] == radio # Boolean mask correspond to the radio button.
#if user select male then will return True for all rows where gender is M
st.dataframe(customers[gender_index][cols])