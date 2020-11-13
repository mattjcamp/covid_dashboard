# init
import pandas as pd
import requests
import matplotlib.pyplot as plt
from IPython.display import display, HTML
from pandas import DataFrame

# set parameters
days_back = 365

# get content from web APIs
us = requests.get('https://api.covidtracking.com/v1/states/daily.json')
us = us.text
us = pd.read_json(us)

# make function for the covid tracking api since they are all the same
def clean_covidtracking_api_data(df):
    
    # get subset
    df = df[['date','state','positiveIncrease','totalTestResultsIncrease'
           ,'hospitalizedCurrently','death','deathIncrease','positive']]
    
    # Rename dataset columns
    df = df.rename(columns={'positiveIncrease':'positive'
                              ,'totalTestResultsIncrease': 'tests'
                              ,'hospitalizedCurrently': 'hospitalized'
                              ,'death': 'death_total'
                              ,'deathIncrease': 'death'
                              ,'positive': 'positive_total'})
    
    # Harmonize date column
    df['date'] = df['date'].astype(str)
    df['date'] = pd.to_datetime(pd.Series(df['date']), format="%Y%m%d")
    
    # Derived Columns
    # Positivity Rate
    positive = df.loc[:,['positive']].values[0:]
    tests = df.loc[:,['tests']].values[0:]
    df['pos_rate'] = positive / tests * 100

    # Death Rate
    deaths = df.loc[:,['death_total']].values[0:]
    positive = df.loc[:,['positive_total']].values[0:]
    df['death_rate'] = (deaths / positive) * 100
    df['death_rate_est'] = (deaths / (positive * 10)) * 100
    
    return df

# fix individual files
us = clean_covidtracking_api_data(us)

us.to_csv(r'daily_covid_us.csv')

# County level data

import io

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

r = requests.get(url)
if r.ok:
    data = r.content.decode('utf8')
    df = pd.read_csv(io.StringIO(data))

df.to_csv(r'raw_download_covid_counties.csv')

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