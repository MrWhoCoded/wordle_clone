import json, pickle

#to extract data from file.
all_words_cleaned ={}
all_words = json.load(open("D:/12E yasser and swarup project/worlde_clone-main (1)/worlde_clone-main/dictionary_of_words.json", "r"))

all_words_items = all_words.items()#to prevent due to changing dictionary size during iteration.(?)

for word,meaning in all_words_items:
    if len(word) in range(4,8):#to check if the words are not of length 4-7.
        if word.islower() and word.isalpha():
            all_words_cleaned[word] = meaning 
    else:
        continue

print (len(all_words_cleaned.keys()))
print("cleaning done")

'''
#rewriting edition dictionary in a new binary file.
with open("D:/12E yasser and swarup project/worlde_clone-main (1)/worlde_clone-main/dictionary_of_words_cleaned.txt", "wb") as new_dict:
         pickle.dump(all_words_cleaned,new_dict)

print(all_words_cleaned)
print("end of program")
'''
#--------------------------------------------------------------------------------------------
#to segregate the words in the dictionary based on number of letters.
while True :
    no_of_ltr = str(input("enter the number of letter of the words =>"))
    #to create unique file name for each set of words with specific length
    file_name = str(no_of_ltr)+"letter words.txt"

    #NOTE 2: file name can be defined outside function or should be returned such that other functions can use the name.
    with open(file_name,'w+', encoding='utf-8') as words:

        #adding words of required length into new list
        for i in all_words_cleaned.keys():
            if (len(i)) == int(no_of_ltr):
                words.write(i+'\n')

quit()
#-----------------------------------------------------------------------------------------
#to establish the connection between pytrends and google trends.

pytrends = TrendReq(hl='en-US', tz=360) 

#list of keywords to get data 
lst_words = list(all_words_cleaned.keys())
                
#building payload which will be queried to google trends.(queries all words through the list)
pytrends.build_payload(lst_words,timeframe='today 12-m') 

#sending request to google trends
data = pytrends.interest_over_time()
#print(data) 
       
#dont understand reset index - to be checked later.
data = data.reset_index() 
