import streamlit as st
import pandas as pd
import os.path
from random import randrange
from prodb.core import generate_db, insert_row

st.title('🦄 Prodb demo')
dbpath = 'db.csv'
if not os.path.isfile(dbpath): generate_db()
if st.button('⬆️ Reset db'): generate_db()

df = pd.read_csv(dbpath)

# ================= input ================= #

form = st.form(key='my-form')
name = form.text_input('Enter your name', 'Luke')
score = form.number_input('Enter score', 5*randrange(0, 21))
submit = form.form_submit_button('➡️ Insert row')

if submit:
    data = {'name':name, 'location': 'NZ', 'score':score}
    df = insert_row(df, data)


st.write(df.tail(10))

col0, col1, col2 = st.columns(3)
file_size = os.path.getsize(dbpath)
col1.metric(f"💾 {dbpath}", f"{df.shape[0]}", "total rows")
col2.metric("📁 filesize", f"{file_size/1000:0.2f}", 'kb')
