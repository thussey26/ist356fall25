import requests
import json
import pandas as pd 
import streamlit as st

st.title("LLM Spell Checker v2")

text = st.text_area("Enter your text:")

if st.button("Spell Check"):
    with st.spinner("Searching misspellings..."):
        prompt = '''
        I would like you to check input text for spelling errors, suggest corrections, and output the corrected text.
        
        Output must be in a machine-readable format. 
        EXAMPLE 1
        {
            "text": "trhis is a test",
            "corrected-text" : "this is a test",
            "corrections": [
                {
                    "word": "trhis",
                    "correction": "this"
                }
            ]
        }


        EXAMPLE 2
        {
            "text": "I lyke cheez!",
            "corrected-text" : "I like cheese!",
            "corrections": [
                {
                    "word": "lyke",
                    "correction": "like"
                },
                {
                    "word": "cheez",
                    "correction": "cheese"
                }
            ]
        }
        
        Here is the Text to check for spelling errors:
     
        '''
