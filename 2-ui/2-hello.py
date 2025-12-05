import streamlit as st

st.title("... and you are.")
#name ='test'
st.write(f'Name is {name}') # gives a name error
name = st.text_input("And you are?")

if name:
    st.write(f"Hello, {name}!")
#else:
    #st.write("Enter a name")