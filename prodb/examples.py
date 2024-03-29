# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/03_examples.ipynb (unless otherwise specified).

__all__ = ['get_json_from_query', 'get_current_weather', 'df_from_loc', 'visit_city']

# Cell
#hide
import requests
import json
import arrow
import pandas as pd
import sys; sys.path.append('../')
from .core import generate_db, insert_row

# Cell
def get_json_from_query(location):
    """Search for a city and return metadata from API"""
    url = f"https://www.metaweather.com/api/location/search/?query={location}"
    r = requests.get(url).json()
    return r[0]

# Cell
def get_current_weather(location):
    """
    inputs: location str "London"
            to find woeid i.e. 44418
    """
    res = get_json_from_query(location)
    woeid = res['woeid']
    url = f"https://www.metaweather.com/api/location/{woeid}/"
    res = requests.get(url).json()
    return res

# Cell
def df_from_loc(location,
                days_ahead=1,
                keep_cols='location the_temp readable_time created applicable_date local_time latt_long weather_state_name min_temp max_temp'.split(' ')):
    res = get_current_weather(location)
    df =  pd.DataFrame.from_records(res['consolidated_weather'][:days_ahead])
    df['location'] = location
    df['local_time'] = pd.to_datetime(res['time']).strftime('%H:%M')
    df['latt_long'] = res['latt_long']
    df['readable_time'] = df.created.apply(lambda x: arrow.get(x).humanize())
    return df[keep_cols]

# Cell
def visit_city(df, cities, dbpath):
    if isinstance(cities, str): cities = [cities]
    for city in cities:
        dx = df_from_loc(city).round(1)

        data = {'location': dx.location.item(),
                'time_utc': arrow.utcnow().format('YYYY-MM-DD HH:mm:ss'),
                'temp': dx.the_temp.item(),
                'high': dx.max_temp.item(),
                'low': dx.min_temp.item(),
                'weather_state': dx.weather_state_name.item(),
                'local_time': dx.local_time.item(),
                'latlong': dx.latt_long.item()}

        df = insert_row(df, data, dbpath)
    return df.round(1)