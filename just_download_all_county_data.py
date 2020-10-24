# init
import pandas as pd
import requests
import matplotlib.pyplot as plt
from IPython.display import display, HTML
from pandas import DataFrame
import io

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

r = requests.get(url)
if r.ok:
    data = r.content.decode('utf8')
    df = pd.read_csv(io.StringIO(data))

df.to_csv(r'daily_covid_all_counties.csv')
