
import streamlit as st
import pandas as pd



# streamlit_app.py

import streamlit as st
import pymongo
from pymongo import MongoClient

#Connect to the server MongoDB
#client = pymongo.MongoClient('mongodb://localhost:27017/')

client = MongoClient()
db = client['db']

db = client["streamlipro"]
mycollection = db['iris']
st.write(mycollection)
all_records = mycollection.find()

list_cursor = list(all_records)
data = pd.DataFrame(list_cursor, columns= ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species'])
st.write(data)
