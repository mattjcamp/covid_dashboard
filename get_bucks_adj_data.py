# init
import pandas as pd
import requests
import matplotlib.pyplot as plt
from IPython.display import display, HTML
from pandas import DataFrame

# set parameters
days_back = 365

def get_county_data(zipcode):

    # we can only get the past 7 days for bucks county with this API
    d = requests.get('https://localcoviddata.com/covid19/v1/cases/newYorkTimes?zipCode=19067&daysInPast=7')
    d = d.text
    d = pd.read_json(d)
    d = d.counties[0].get("historicData")
    d = DataFrame (d,columns=['date','deathCt','positiveCt'])
    d['date'] = pd.to_datetime(pd.Series(d['date']), format="%Y-%m-%d")

    # derive positive and death for bucks
    diff = d[['deathCt','positiveCt']].diff(periods=-1)
    d2 = d.join(diff, lsuffix='_caller', rsuffix='_other')
    d2 = d2.rename(columns={'deathCt_caller':'death_total'
                        ,'positiveCt_caller':'positive_total'
                        ,'deathCt_other':'death'
                        ,'positiveCt_other':'positive'})
    
    return d2

b = get_county_data(19067)

b


b.to_csv(r'test.csv')
