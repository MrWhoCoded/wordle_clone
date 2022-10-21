#to extract data from file.
all_words = json.load(open("dictionary_of_words.json", "r"))
for word in all_words.keys():
    if word.iscapital() == True:
        all_words[word].pop()
    if word.isspace() == True:
        all_words[word].pop()
    if word.issymbol() == True:
        all_words[word].pop()

with open("dictionary_of_words_cleaned.json", "w") as new_dict:
    for word,meaning in all_words.items():
        new_dict.write(word,meaning)
        
    
