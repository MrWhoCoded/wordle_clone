
from pytrends.request import TrendReq
import time,csv


#opening file with words
#with open("dictionary_of_words_cleaned.txt", "rb") as words_fb:
   
#to establish the connection between pytrends and google trends.
pytrends = TrendReq(hl='en-US', tz=360) 

#list of keywords to get data 
lst_words = ["fat","hello",]
        
print (len(lst_words))

        
#building payload which will be queried to google trends.(queries all words through the list)
pytrends.build_payload(lst_words,timeframe='today 12-m') 
    
#sending request to google trends
data = pytrends.interest_over_time()
print(data) 
       
#dont understand reset index - to be checked later.
#data = data.reset_index() 

    
    

print("hello world")


