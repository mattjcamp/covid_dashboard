# init
import pandas as pd
import requests
import matplotlib.pyplot as plt
from IPython.display import display, HTML
from pandas import DataFrame

df = pd.read_csv(r'daily_covid_all_counties.csv')

df.to_csv(r'daily_covid_all_counties.csv')

diff = df[['cases','deaths']].diff(periods=-1)
