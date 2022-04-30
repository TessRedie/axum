
import streamlit as st
import pandas as pd



# streamlit_app.py

import streamlit as st
import pymongo

#Connect to the server MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')


#create DB named 'MTSpam'
#db = client['Iris']



db = client["streamlipro"]
mycollection = db["iris"]

one_record = mycollection.find_one()
st.write(one_record)
all_records = mycollection.find()
st.write(all_records)
for row in all_records:
    st.write(row)