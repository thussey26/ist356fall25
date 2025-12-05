#  Challenge 2-2-2


import streamlit as st

# initialize a session state
if 'total'not in st.session_state:
    st.session_state.total = 0.0
if 'amount' not in st.session_state:
    st.session_state.amount = 0.0
if 'history' not in st.session_state:
    st.session_state.history = []

    
#Add title and inputs
st.title("Order Total")
amount = st.number_input("Amount", value = st.session_state.amount)
btn_add = st.button("Add to Total")
btn_clear = st.button("Clear")

#Add amount
if btn_add:
    st.session_state.history.append(amount)
    st.session_state.total = sum(st.session_state.history)
    st.write(f"TOTAL: {st.session_state.total}")
    st.write("HISTORY")
    for h in st.session_state.history:
        st.write(h)

if btn_clear:
    st.session_state.history = []
    st.session_state.total = 0.0
    st.session_state.amount = 0.0
    st.write(f"st.session_state.total:.2f")
    st.rerun()
