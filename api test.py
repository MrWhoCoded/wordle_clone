from pytrends.request import TrendReq
pytrends = TrendReq()

timeframes = ['2020-12-14 2021-01-25']
pytrends.build_payload(['python'],cat = 0, geo = 'IN', gprop = 'youtube', timeframe = timeframes[0])
print(pytrends.interest_over_time())
