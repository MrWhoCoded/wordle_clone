from pytrends.request import TrendReq
import time,csv

#to send api request to google trends api to find the frequency of word usage.
for no_of_ltr in range(4,8):
    
    #to create file name for each set of words with specific length
    file_name = str(no_of_ltr)+"letter words.txt"

    #file name can be defined outside function or should be returned such that other functions can use the name.
    with open(file_name,'r+', encoding='utf-8') as word_file:
        lst_words = word_file.readlines()
        
        #var to keep count
        index = 0 
        word_list = []
        word = lst_words[index]
        word_list.append(word)
        
        
            
        #to establish the connection between pytrends and google trends.
        pytrends = TrendReq(hl='en-US', tz=360) 
        

        #building payload which will be queried to google trends.(queries all words through the list)
        pytrends.build_payload(word_list, timeframe='today 12-m') 
            
        #sending request to google trends
        data = pytrends.interest_over_time()
        
        time.sleep(5)

        #dont understand reset index - to be checked later.
        data = data.reset_index() 
        
        
        print(data)
        print ("ran")
            
                             