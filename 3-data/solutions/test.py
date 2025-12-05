import pandas as pd
import streamlit as st

def grade_attendance(participation: float) -> str:
    '''Return a grade based on the number of polls a student participated'''
    if participation == 0.0:
        return 'AB'
    elif participation < 0.5:
        return 'np'
    else:
        return '+'

roster_url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/roster.csv"
roster_df = pd.read_csv(roster_url)
#st.dataframe(roster_df)


# extract each poll
polls = []
dates =["2024-01-08", "2024-01-15", "2024-01-22", "2024-01-29"]
for date in dates:
    #read in each poll
    poll = f"https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/poll-responses-{date}.csv"
    
    poll_df = pd.read_csv(poll)
    #add lineage to each poll by adding a date column
    poll_df['date'] = date
    #add poll to polls list
    #append to polls list
    polls.append(poll_df)

# combine all polls into one dataframe 
poll_df = pd.concat(polls, ignore_index=True)   
#st.dataframe(poll_df)
#st.dataframe(roster_df)


combined_df = pd.merge(roster_df, poll_df, how='left', left_on='netid', right_on='student_id')
st.dataframe(combined_df)


# max polls count for each date
poll_counts = combined_df.pivot_table(index ='date', values ='poll_num', aggfunc='max')
st.dataframe(poll_counts)


# count of student responses by date
student_responses = combined_df.pivot_table(index='netid', columns='date', values='answer', aggfunc='count')
student_responses= student_responses.fillna(0)
st.dataframe(student_responses)


# copy student_responses to a new dataframe
student_responses2 = student_responses.copy()
# change student poll responses to percentages
for col in student_responses2.columns:
    student_responses2[col] = student_responses2[col] / poll_counts.loc[col, 'poll_num']
    
    
# every original data point in student_responses2 is replaced by the output of grade_attendance function when applied to values.
# convert the percentages to grades
for col in student_responses2.columns:
    student_responses2[col] = student_responses2[col].apply(grade_attendance)
    
st.dataframe(student_responses2)

#make a copy of student_responses2 into a new dataframe
summary = student_responses2.copy()
summary['sessions'] = len(summary.columns) # calculate total sessions
st.dataframe(summary)

summary['AB'] = summary.apply(lambda row: row.value_counts().get('AB', 0), axis=1)
summary['np'] = summary.apply(lambda row: row.value_counts().get('np', 0), axis=1)
summary['pct'] = (summary['AB'] + summary['np']) / summary['sessions']

st.dataframe(summary)

summary_with_names = pd.merge(roster_df, summary, left_on='netid', right_index=True)
st.dataframe(summary_with_names)