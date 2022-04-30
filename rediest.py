
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
mycollection = db.iris.find({})



#one_record = mycollection.find_one()
#st.write(one_record)
#all_records = mycollection.find()
st.write(mycollection)
for row in mycollection:
    st.write(row)
