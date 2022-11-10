import json,pickle

#to extract data from file.
all_words_cleaned ={}
all_words = json.load(open("D:/12E yasser and swarup project/worlde_clone-main (1)/worlde_clone-main/dictionary_of_words.json", "r"))


all_words_items = all_words.items()#to prevent due to changing dictionary size during iteration.(?)

for word,meaning in all_words_items:
    if len(word)  in range(3,8): # to check if the words are not of length 3-7.
        pass
    elif not word.isupper():
        pass
    elif not word.isspace():
        pass
    elif  word.isalpha():
        print(word)
        all_words_cleaned[word]= meaning 
    else:
        continue

print("yessir1")
print (all_words_cleaned)

quit()
#rewriting edition dictionary in a new binary file.
with open("dictionary_of_words_cleaned.txt", "wb") as new_dict:
         pickle.dump(all_words_cleaned,new_dict)

print(all_words_cleaned)
print("end of program")
