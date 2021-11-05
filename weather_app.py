import os.path; import requests; import json; import random
import pandas as pd; import numpy as np; import arrow
from PIL import Image
import streamlit as st

from prodb.core import generate_db, insert_row, utc_now, readable_df
from prodb.examples import visit_city


def main():
    
    t1, t2 = st.columns((4,1))
    t1.title('🦄 Weather with Pro db')

    dbpath = 'weather_db.csv'
    cols = 'location temp high low weather_state latlong'.split()

    if t2.button('⬆️ Reset db'): 
        df = generate_db(dbpath=dbpath, cols=cols)
    if not os.path.isfile(dbpath): 
        df = generate_db(dbpath=dbpath, cols=cols)
    else: df = pd.read_csv(dbpath)

    with st.form(key='cities', clear_on_submit=False):
        # Note: form sequence bug still exists
        city_suggestions = ['Wellington', 'London', 'Lagos', 'Zagreb', 'Singapore', 'Alexandria', 'Bangkok']
        i = random.randint(0, len(city_suggestions))-1
        city = st.text_input(f'City{i}', city_suggestions[i])
        submitted = st.form_submit_button('➡️ Submit')
        if submitted: df = visit_city(df, city, dbpath)

    if not df.empty:
        dx = readable_df(df, max_rows=10)
        st.write(dx.drop(['latlong', 'time_utc'], axis=1).style.format("{:1}"))

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
        page_title="🌤️ Weather App",
        page_icon="🦄",
        layout="centered",
        initial_sidebar_state="auto")
    main()