import pandas as pd
import streamlit as st

st.title("Webtraffic Data")



link = 'https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log'

st.title('Web Traffic Log Analysis')
wt= pd.read_csv(link, sep='\s+',skiprows=3,header=0)


#Filtering
wt_filter=(wt['sc-status']==200) & (wt['time-taken']>500)
wt_slow =wt[wt_filter]
st.dataframe(wt_slow)

