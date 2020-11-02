
import pandas
from dplython import (DplyFrame, X, diamonds, select, sift, sample_n,
    sample_frac, head, arrange, mutate, group_by, summarize, DelayFunction) 


diamonds >> head(5)

diamonds >> select(X.carat, X.cut, X.price) >> head(5)

d = (diamonds >> 
    sift(X.carat > 4) >> 
    select(X.carat, X.cut, X.depth, X.price) >>
    head(2))

(diamonds >> 
  mutate(carat_bin=X.carat.round()) >> 
  group_by(X.cut, X.carat_bin) >> 
  summarize(avg_price=X.price.mean()))
  
test =  df['deaths'] < 0
less_than_zero = df[test]
print(less_than_zero.shape)
print(less_than_zero.head())

test

#df['deaths_fixed'] = df['deaths_new'].apply(lambda x: 'True' if x <= 0 else 'False')
