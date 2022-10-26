import json

#to extract data from file.
all_words = json.load(open("D:\python_my programs\wordle automation proj\dictionary_of_words.json", "r"))
all_words_items = list(all_words.items())#to prevent due to changing dictionary size during iteration.(?)

for wordmeaning in all_words_items:
    if len(wordmeaning[0]) not in range(3,8): # to check if the words are not of length 3-7.
        all_words_items.remove(wordmeaning)

with open("D:\python_my programs\wordle automation proj\dictionary_of_words_cleaned.txt", "w") as new_dict:
    for wordmeaning in all_words_items:
        print(wordmeaning)
        new_dict.write(str(wordmeaning))

print("end of program")
