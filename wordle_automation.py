#swarup,Yasser Ahmed - 20.5.2022
#to find answer of wordle question.

#to get list of words from a dictionary of english words from json file.
#dictionary key/value pair is in the form word/meaning.
import json
import random

#NOTE: can add meanings also as a clue....maybe


#to get file of words(NOTE: should be under condition)
def create_word_file(no_of_ltr):
    global file_name, num_words

    #to extract data from file.
    all_words = json.load(open("dictionary_of_words.json", "r"))

    #to create unique file name for each set of words with specific length
    file_name = "dict_no_ltr-"+ str(no_of_ltr) +".txt"

    #NOTE 2: file name can be defined outside function or should be returned such that other functions can use the name.
    with open(file_name,'w+', encoding='utf-8') as words:

        #adding words of required length into new list
        for i in all_words.keys():
            if (len(i)) == int(no_of_ltr):
                words.write(i+'\n')



#to pick a random word from word file
def pick_word(file_name):
    global  wordle_word, common_words


    with open(file_name, 'r', encoding='utf-8') as words:
        #global wordle_word, common_words

        lst_words = words.read().splitlines()


    #to pick a random number in the range of 0 to total words with required lenght
    random_num = random.randint(0, len(lst_words))
    #word to guess-
    wordle_word = lst_words[random_num].lower()

    return wordle_word

#coding for hints
#-1 : yellow
#0 : grey
#1 : green

def hints(guess_word,wordle_word):
    hint_lst=[]
    
    for letter in guess_word:
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
#no_of_ltr - number of letters in the word
#guess_word - word guessed by user



'''
no_of_ltr = '5'
guess_word = "alter"
create_word_file(no_of_ltr)
print(pick_word(file_name,dif_lvl))

hint_lst = hints(guess_word,wordle_word)
print(hint_lst)
'''
