
# init
import pandas as pd
import requests
import matplotlib.pyplot as plt
from IPython.display import display, HTML
from pandas import DataFrame

df = pd.read_csv(r'raw_download_covid_counties.csv')
df = df.sort_values(by=['state','county','date'])

# Get Deltas
diff = df[['cases','deaths']].diff(periods=1)
df = df.join(diff, lsuffix='_cumm', rsuffix='_new')

# Fix First County Error
df.loc[df.groupby(['state','county'])['cases_new'].head(1).index, 'cases_new'] = 0
df.loc[df.groupby(['state','county'])['deaths_new'].head(1).index, 'deaths_new'] = 0

# Fix Negative Cases
df.loc[df['cases_new'] < 0, 'cases_new'] = 0
df.loc[df['deaths_new'] < 0, 'deaths_new'] = 0

# Write to CSV for Tableau visualization
df.to_csv(r'covid_by_county.csv')
