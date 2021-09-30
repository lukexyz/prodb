# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['say_hello', 'generate_db', 'insert_row']

# Cell
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'

# Cell
#hide
import pandas as pd
import arrow
from time import gmtime, strftime

# Cell

def generate_db(prefill=False):
    if prefill:
        df = pd.DataFrame({'name': ['Sam', 'Grant'],
                           'location': ['UK', 'NZ'],
                           'score': [0, 30],
                           'time_utc' : [arrow.utcnow().format('YYYY-MM-DD HH:mm:ss'),
                                         arrow.utcnow().format('YYYY-MM-DD HH:mm:ss')]})
    else:
        df = pd.DataFrame(columns=['name', 'location', 'score', 'time_utc'])
    df.to_csv('db.csv', index=None)


# Cell

def insert_row(df, data, db_path='db.csv'):
    new_row = pd.Series({'time_utc' : arrow.utcnow().format('YYYY-MM-DD HH:mm:ss'),
                         'name':data['name'],
                         'location': data['location'],
                         'score': data['score']})
    df = df.append(new_row, ignore_index=True)
    df.to_csv(db_path, index=None)
    return df
