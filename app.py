import streamlit as st
import pandas as pd
import os.path
from random import randrange
from prodb.core import generate_db, insert_row

def main():
    st.title('🦄 Pro db')
    dbpath = 'db.csv'
    if not os.path.isfile(dbpath): generate_db()
    if st.button('⬆️ Reset db'): generate_db()

    df = pd.read_csv(dbpath)

    # ================= input ================= #

    # upto: fix submission code sequence
    with st.form(key='columns_in_form'):
        c1, c2 = st.columns(2)
        name = c1.text_input('Enter name', 'Luke')
        score = c2.number_input('Enter score', 5)
        submitted = st.form_submit_button('➡️ Submit row')
        if submitted:
            data = {'name':name, 'location': 'NZ', 'score':score}
            df = insert_row(df, data)

    st.write(df.tail(8))

    col0, col1, col2, col3 = st.columns(4)
    file_size = os.path.getsize(dbpath)
    col2.metric(f"💾 {dbpath}", f"{df.shape[0]}", "total rows")
    col3.metric("📁 filesize", f"{file_size/1000:0.2f}", 'kb')

if __name__ == '__main__':
    st.set_page_config(
        page_title="pro db",
        page_icon="🦄",
        layout="centered",
        initial_sidebar_state="auto")
    main()