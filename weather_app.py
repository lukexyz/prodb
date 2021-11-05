import os.path; import requests; import json; import random
import pandas as pd; import numpy as np; import arrow
from PIL import Image
import streamlit as st

from prodb.core import generate_db, insert_row, utc_now, readable_df
from prodb.examples import visit_city


def main():
    t1, t2 = st.columns((4,1))
    t1.title('🦄 Pro db - WEATHER APP')

    dbpath = 'weather_db.csv'
    cols = 'location temp high low weather_state latlong'.split()

    if t2.button('⬆️ Reset db'): 
        df = generate_db(dbpath=dbpath, cols=cols)
    if not os.path.isfile(dbpath): 
        df = generate_db(dbpath=dbpath, cols=cols)
    else: df = pd.read_csv(dbpath)

    with st.form(key='columns_in_form'):
        city_suggestions = ['wellington', 'London', 'Lagos', 'Zagreb', 'Singapore', 'Alexandria', 'Bangkok']
        random.shuffle(city_suggestions)
        cities = st.text_input('City', city_suggestions[0])
        submitted = st.form_submit_button('➡️ Submit')
        if submitted: df = visit_city(df, cities, dbpath)
    
    #df = visit_city(df, cities)
    st.write(readable_df(df, max_rows=10))

    dx = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(dx)

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
        page_title="Weather App",
        page_icon="🌤️",
        layout="centered",
        initial_sidebar_state="auto")
    main()