import json,pickle

#to extract data from file.
all_words_cleaned ={}
all_words = json.load(open("dictionary_of_words.json", "r"))
all_words_items = all_words.items()#to prevent due to changing dictionary size during iteration.(?)

for word,meaning in all_words_items:
    if len(word)  in range(3,8): # to check if the words are not of length 3-7.
        pass
    if not word.isupper():
        pass
    if not word.isspace():
        pass
    if not word.isalpha():
        pass
    else:          
        all_words_cleaned[word]=meaning 


#rewriting edition dictionary in a new binary file.
with open("dictionary_of_words_cleaned.txt", "wb") as new_dict:
         pickle.dump(all_words_cleaned,new_dict)

print(all_words_cleaned)
print("end of program")
