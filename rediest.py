
import streamlit as st
import pandas as pd



# streamlit_app.py

import streamlit as st
import pymongo

#Connect to the server MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
MONGODB_DATABASES = {
    "default": {
        "name": 'api',
        "host": 'mongo',
       "port": 27017
    },
}


#create DB named 'MTSpam'
#db = client['Iris']



db = client["streamlipro"]
mycollection = db['iris']
st.write(mycollection)
all_records = mycollection.find()

list_cursor = list(all_records)
st.write(list_cursor)
