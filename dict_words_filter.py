import json,pickle

#to extract data from file.
all_words = json.load(open("dictionary_of_words.json", "r"))
all_words_items = all_words.items()#to prevent due to changing dictionary size during iteration.(?)

for word,meaning in all_words_items:
    if len(word)  in range(3,8): # to check if the words are not of length 3-7.
        pass
    if not word.isupper():
        pass
    if not word.isspace():
        pass
    if not word.isapha()
        pass
    else:          
        del all_words[(word,meaning)]#removes the defective nested list from main list. 


with open("dictionary_of_words_cleaned.txt", "wb") as new_dict:
         pickle.dump(all_words,new_dict)


print("end of program")
