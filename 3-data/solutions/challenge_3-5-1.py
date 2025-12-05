import pandas as pd
import streamlit as st

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv"

#st.dataframe(pd.read_csv(url))


st.title("Exam Scores Data")

options =['Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups']
exams = pd.read_csv(url)
#st.dataframe(exams, width=1000)

choice = st.selectbox("Select a study option", options)
summary = exams.groupby(choice).agg({'Class_Section':'count', 'Student_Score':'mean'})
st.dataframe(summary)
