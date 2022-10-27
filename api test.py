
from pytrends.request import TrendReq
import time
"""
pytrends = TrendReq(hl='en-US', tz=360) 

kw_list = ["slurp"] # list of keywords to get data 

pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m') 
data = pytrends.interest_over_time() 
#data = data.reset_index() 
print(type(data))
print(data)
time.sleep(30)"""

#install pytrends

#import the libraries
import pandas as pd                        
from pytrends.request import TrendReq

#create model
pytrend = TrendReq()

#provide your search terms
kw_list=['Facebook', 'Apple', 'Amazon', 'Netflix', 'Google']

#get interest by region for your search terms
pytrend.build_payload(kw_list=kw_list)
df = pytrend.interest_by_region(inc_low_vol=True, inc_geo_code=True)
print(df)
print("------------------")
print(df.iloc[102])
#print(df.loc[df["geoName"] == "India"])
time.sleep(10)
df.to_csv('data.csv')