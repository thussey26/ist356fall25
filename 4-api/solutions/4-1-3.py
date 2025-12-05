'''
Geocodes 

curl -X 'GET' \
  'https://cent.ischool-iot.net/api/google/geocode?location=syracuse%20university' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: ec25dc1e1297cfba51838bd3'
  
  
  
  Weather
  
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/weather/current?units=imperial%20&lon=-76&lat=43' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: ec25dc1e1297cfba51838bd3'


'''


import pandas as pd
import numpy as np  
import requests
import json

import streamlit as st
from time import sleep


st.title("Geocode and Weather API Example")
location = st.text_input("Enter a location to get current weather:")
if st.button("Get Weather"):
    with st.spinner('Fetching data...'):
         sleep(2)  # simulate a delay for better UX     

    url = "https://cent.ischool-iot.net/api/google/geocode"
    querystring = {"location":location}
    headers = {'X-API-KEY': 'ec25dc1e1297cfba51838bd3'}
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()
    geocode = response.json()
    #st.write(geocode)
    lon = geocode['results'][0]['geometry']['location']['lng']
    lat = geocode['results'][0]['geometry']['location']['lat']


    url1 = "https://cent.ischool-iot.net/api/weather/current"
    querystring1 = {"units":"imperial","lon":lon,"lat":lat}
    response1 = requests.get(url1, headers=headers, params=querystring1)
    response1.raise_for_status()
    weather = response1.json()
    #st.write(weather)
    temp =weather['current']['temperature_2m']
    st.metric(label="Current Temperature (°F)", value=f"{temp} °F" )






