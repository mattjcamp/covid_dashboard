# init
import pandas as pd
import requests
import matplotlib.pyplot as plt
from IPython.display import display, HTML
from pandas import DataFrame

df = pd.read_csv(r'daily_covid_all_counties.csv')
df = df.sort_values(by=['state','county','date'])
diff = df[['cases','deaths']].diff(periods=1)
df = df.join(diff, lsuffix='_today', rsuffix='_delta')

#df = df[(df['date'] > '2020-03-18')

df.head(25)

# df.to_csv(r'covid_by_county.csv')
