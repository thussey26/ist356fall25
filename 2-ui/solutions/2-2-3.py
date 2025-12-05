# Challenge 2-2-3

import streamlit as st

from io import StringIO # required to convert binary to text


st.title("Order File Processing")
text_file_data = st.file_uploader("Upload the order file", type=["txt"]) # create a file uploader widget

if text_file_data:
    binary_contents = text_file_data.getvalue()
    # gets the contents of file as a binary object
    text_contents = StringIO(binary_contents.decode("utf-8")).read() # decodes binary data into a string using UTF-8 encoding
    total = 0 #cumulate the sum of order amounts
    count = 0 #keep track of the orders found
    for line in text_contents.split("\n"): # go over each line of text, split at \n into list of strings
        try: #begin block to handle errors
            order = float(line) # convert line which is a string to float
            total = total + order # add order amount to total
            count = count + 1 #increment the orders found
        except ValueError:
            continue # skip lines that are not numbers
    
    st.info(f"Number of orders: {count}") #display order count in a blue box
    st.info(f"Total: ${total:.2f}")
