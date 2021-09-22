import streamlit as st
import pandas as pd
from prodb.core import generate_db, insert_row

st.header('Original dataframe')
if st.button('♻️ Reset db'): generate_db()

df = pd.read_csv('db.csv')

# ================= input ================= #

form = st.form(key='my-form')
name = form.text_input('Enter your name', 'Luke')
score = form.number_input('Enter score', 10)
submit = form.form_submit_button('Submit')

if submit:
    data = {'name':name, 'location': 'NZ', 'score':score}
    df = insert_row(df, data)


st.write(df.tail(10))

