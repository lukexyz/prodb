import streamlit as st
import pandas as pd
import os.path
import arrow
from PIL import Image
import random

from prodb.core import generate_db, insert_row


def utc_now():
    return arrow.utcnow().format('YYYY-MM-DD HH:mm:ss')


def main():
    t1, t2 = st.columns((4,1))
    t1.title('🦄 Pro db')
    dbpath = 'db.csv'
    cols = 'name mood message time_utc'.split()

    if not os.path.isfile(dbpath): df = generate_db(dbpath=dbpath, cols=cols)
    if t2.button('⬆️ Reset db'): df = generate_db(dbpath=dbpath, cols=cols)

    # ================= input ================= #
    with st.form(key='columns_in_form'):
        c1, c2, c3 = st.columns((1, 1, 4))
        name = c1.text_input('Name', 'Luke')
        emoji = '🌎 😊 😵 👹'.split(" ")
        random.shuffle(emoji)
        mood = c2.selectbox('Mood', emoji)
        message = c3.text_input('Message', 'hello from London, Uk')
        submitted = st.form_submit_button('➡️ Submit')
        if submitted:
            data = {'name':name, 'mood': mood, 
                    'message':message, 'time_utc':utc_now()}
            df = insert_row(df, data)

    df['human'] = df.time_utc.apply(lambda x: arrow.get(x).humanize())
    st.write(df[['name', 'human', 'mood', 'message']].tail(8))

    # ================= metrics ================= #
    col0, col1, col2, col3 = st.columns(4)
    file_size = os.path.getsize(dbpath)
    col0.metric(f"💾 {dbpath}", f"{df.shape[0]}", "total rows")
    col1.metric("📁 filesize", f"{file_size/1000:0.2f}", 'kb')

    f1, f2 = st.columns((4,1))
    image = Image.open('docs/assets/images/company_logo.png')
    f2.image(image)

if __name__ == '__main__':
    st.set_page_config(
        page_title="pro db",
        page_icon="🦄",
        layout="centered",
        initial_sidebar_state="auto")
    main()