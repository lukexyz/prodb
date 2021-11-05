import streamlit as st
import pandas as pd
import os.path
import arrow
from PIL import Image
import random

def get_json_from_query(location):
    """Search for a city and return metadata from API"""
    url = f"https://www.metaweather.com/api/location/search/?query={location}"
    r = requests.get(url).json()
    return r[0]

    