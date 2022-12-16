from pytrends.request import TrendReq
import time,csv
import pandas as pd
import traceback

def sort_word(word,val):

    if val > 70: #easy word
        with open("easy_" + file_name, "a") as fl_easy:
            fl_easy.write(word)

    if 50 < val < 70: #medium word
        with open("medium_" + file_name, "a") as fl_medium:
            fl_medium.write(word)

    if val < 50: #hard word
        with open("hard_" + file_name, "a") as fl_hard:
            fl_hard.write(word)

dummmy_dict = {}
#to send api request to google trends api to find the frequency of word usage.
for no_of_ltr in range(5,8):
    
    #to create file name for each set of words with specific length
    file_name = str(no_of_ltr)+"letter words.txt"

    #file name can be defined outside function or should be returned such that other functions can use the name.
    with open(file_name,'r+', encoding='utf-8') as word_file:
        all_words = word_file.readlines()

    #to establish the connection between pytrends and google trends.
    pytrends = TrendReq(hl='en-US', tz=360)
            
    index = 0
    word_lst = []
    len_lst = len(all_words)
    print(len_lst)
    
    while index < 200: #len starts from 1 and index starts from 0.

        try:
            #var to keep count
            word = all_words[index]
            print('Checking for: index=',index,' word=',word)
            word_lst.append(word)
    
            #building payload which will be queried to google trends.(queries all words through the list)
            pytrends.build_payload(word_lst, timeframe='today 12-m') 

            #sending request to google trends
            data = pytrends.interest_over_time()
            #print('date',data)
           
            data = data.reset_index()

            dataframe = pd.DataFrame(data)
            #print(dataframe.iloc[:, 1])
            name = dataframe.iloc[:, 1].name
            #val = round(int(dataframe.iloc[:, 1].mean()),2)
            val = dataframe.iloc[:,1].mean()
            valr = round(int(val),2)
            #print('val ',val,' valr ',valr)
            
            dummmy_dict[name] = val
            
            index += 1
            print('Mean of usage for ',word,"is ", val)

            word_lst = []

            sort_word(word,val)

        except Exception:
            #traceback.print_exc()
            word_lst = []
            time.sleep(2)
            
        #index does not chage so word is repeated. 
            
print(dummmy_dict)            
