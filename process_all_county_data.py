# init
import pandas as pd
import requests
import matplotlib.pyplot as plt
from IPython.display import display, HTML
from pandas import DataFrame

df = pd.read_csv(r'raw_download_covid_counties.csv')
df = df.sort_values(by=['state','county','date'])
diff = df[['cases','deaths']].diff(periods=1)
df = df.join(diff, lsuffix='_cumm', rsuffix='_new')

df.to_csv(r'covid_by_county.csv')
