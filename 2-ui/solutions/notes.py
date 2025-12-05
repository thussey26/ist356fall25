import streamlit as st

st.title("Session State Basics.")

# Check if it is session state variable exists

'a_counter' not in st.session_state
st.session_state['a_counter'] = 0
st.write(st.session_state)

for the_values in st.session_state.values():
    st.write({the_values})





