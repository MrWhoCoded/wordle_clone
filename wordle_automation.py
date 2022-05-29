#swarup,Yasser Ahmed - 20.5.2022
#to find answer of wordle question.

#to get list of words from a dictionary of english words from json file.
#dictionary key/value pair is in the form word/meaning.
import json
from difflib import get_close_matches
from collections import Counter#to get common words
import random

#NOTE: can add meanings also as a clue....maybe


#to get file of words(NOTE: should be under condition)
def create_word_file(no_of_ltr):
    global file_name, num_words

    #to extract data from file.
    all_words = json.load(open("D:\python_my programs\dictionary_of_words.json", "r"))

    #to create unique file name for each set of words with specific length
    file_name = "dict_no_ltr-"+ no_of_ltr +".txt"

    #new file is created(NOTE: idealy should have condition to not replace/replicate once created)
    #NOTE 2: file name can be defined outside function or should be returned such that other functions can use the name.
    with open(file_name,'w+', encoding='utf-8') as words:

        #adding words of required length into new list
        for i in all_words.keys():
            if (len(i)) == int(no_of_ltr):
                words.write(i+'\n')

    return file_name

    #divides the number of words into 5 in order of commonality.
def word_difficulty(common_words, dif_lvl):
    words_per_lvl = int(len(common_words)/5)

    #gives range of words from most difficult to the easiest.
    count=1#to count which level for loop is on
    for lvl in range(5):
        lst_dif = common_words[lvl:(lvl+1)*words_per_lvl]

        if count == dif_lvl:
            return list(lst_dif)
        else:
            count +=1



#to pick a random word from word file
#figure out how to get the program to only pick out common words

def pick_word(file_name,dif_lvl):
    global  wordle_word


    with open(file_name, 'r', encoding='utf-8') as words:
        global wordle_word, common_words

        lst_words = words.read().splitlines()

    #create a new list in order of common words from original list
    lst_words = Counter(lst_words)#makes the list readable by the module
    common_words = lst_words.most_common()

    #gets set of words according to the level inputted
    lst_dif=word_difficulty(common_words, dif_lvl)

    #to pick a random number in the range of 0 to total words with required lenght
    random_num = random.randint(0, len(lst_dif))

    #word to guess-
    wordle_word = lst_dif[random_num]
    wordle_word = wordle_word[0]#to assign value to variable as a string

    return wordle_word

#coding for hints
#-1 : yellow
#0 : grey
#1 : green

def hints(guess_word,wordle_word):
    hint_lst=[]
    for letter in guess_word:
        print(len(hint_lst))
        #for green entry(i.e when the letter is in the correct position and value)
        if letter == wordle_word[len(hint_lst)]:
            hint_lst.append(1)
        #for yellow output(i.e when the letter is in the word but wrong position)
        elif letter in wordle_word:
            hint_lst.append(-1)
        #for grey output(i.e when the letter is not in the word)
        elif letter not in wordle_word:
            hint_lst.append(0)


    return hint_lst














#inputs
no_of_ltr = '5'
dif_lvl = 1
guess_word = "alter"
create_word_file(no_of_ltr)
print(pick_word(file_name,dif_lvl))

#wordle_word = "alter"
hint_lst = hints(guess_word,wordle_word)
print(hint_lst)
