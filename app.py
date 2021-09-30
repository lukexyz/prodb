import streamlit as st
import pandas as pd
import os.path
import arrow

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
        c1, c2, c3 = st.columns(3)
        name = c1.text_input('Enter name', 'Luke')
        mood = c2.selectbox('Mood', ('😊', '😵', '👹'))
        message = c3.text_input('Message', 'hello')
        submitted = st.form_submit_button('➡️ Submit')
        if submitted:
            data = {'name':name, 'mood': mood, 'message':message}
            df = insert_row(df, data)

    df['human'] = df.time_utc.apply(lambda x: arrow.get(x).humanize())
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