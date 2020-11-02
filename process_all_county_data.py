# init
import pandas as pd
import requests
import matplotlib.pyplot as plt
from IPython.display import display, HTML
from pandas import DataFrame

df = pd.read_csv(r'raw_download_covid_counties.csv')
df = df.sort_values(by=['state','county','date'])

df.to_csv(r'temp.csv')

diff = df[['cases','deaths']].diff(periods=1)


test =  diff['deaths'] < 0
less_than_zero = diff[test]
print(less_than_zero.shape)
print(less_than_zero.head())

#cases  deaths
#72895      1.0    -1.0
#103870     0.0    -1.0
#160272     9.0    -1.0
#589543     7.0    -1.0
#1934   -2140.0   -31.0

df = df.join(diff, lsuffix='_cumm', rsuffix='_new')

#df.to_csv(r'covid_by_county.csv')
