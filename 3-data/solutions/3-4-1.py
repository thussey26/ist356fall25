'''
1. create a module `check_functions.py`
    - add the `clean_currency()` function definition to it.
    - under `if __name__=='__main__':` add the tests
    - run the code to make sure it works.
2. create your challenge file `3-4-1.py`
    - import streamlit, pandas and your clean_currency function
    - load the checks dataset into a dataframe: 
    - clean the `total amount of check` and `gratuity` columns
    - calculate the `price_per_item`  as total amount of check / total items on check
    - calcualte the `price_per_person` as total amont of check / party size
    - calculate the `items_per_person` as total items on check / party size
    - calculate the `tip_percentage` as the total amount of  gratuity/check
    - display dataframe
    - describe dataframe
    


checks dataset `https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv`

'''



import pandas as pd
import streamlit as st


from check_functions import clean_currency

st.title("Dining Check Data")

# load the checks dataset into a dataframe
checks = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv')
st.dataframe(checks, width=1000)
# transformations
checks['total_amount_of_check_cleaned'] = checks['total amount of check'].apply(clean_currency)
checks['gratuity_cleaned'] = checks['gratuity'].apply(clean_currency)

st.dataframe(checks, width=1000)
# Calculate new columns

checks['price_per_item'] = checks['total_amount_of_check_cleaned'] / checks['total items on check']
checks['price_per_person'] = checks['total_amount_of_check_cleaned'] / checks['party size']
checks['items_per_person'] = checks['total items on check'] / checks['party size']
checks['tip_percentage'] = checks['gratuity_cleaned'] / checks['total_amount_of_check_cleaned']

st.dataframe(checks, width=1000)

col1,col2,col3,col4 = st.columns(4)

col1.metric("Average Price Per Item", checks['price_per_item'].mean())
col2.metric("Average Price Per Person", checks['price_per_person'].mean())
col3.metric("Average Items Per Person", checks['items_per_person'].mean())
col4.metric("Average Tip Pct", checks['tip_percentage'].mean())

st.dataframe(checks.describe())