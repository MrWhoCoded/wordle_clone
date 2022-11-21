from tkinter import *
from tkinter import ttk
import csv
import wordle_automation
import os, sys

complete_attempt_word = ""
hints = []
counter = 0
attempt_words = []

def window_switcher():
    global row, attempt_word, wordle_word, complete_attempt_words, complete_attempt_word
    attempt_word = ""
    complete_attempt_words = []
    complete_attempt_word = ""
    row = [1]
    wordle_automation.create_word_file(no_of_words.get())
    wordle_word = wordle_automation.pick_word(wordle_automation.file_name)
    print(wordle_word)
    window.destroy()
    _game_window()

def attempt_cleaner():
    global attempt_word, entries, attempt_words, complete_attempt_words, complete_attempt_word
    complete_attempt_word = ""
    for entry in entries:
        if len(entry.get()) != 0:
            complete_attempt_word += entry.get().lower()
            attempt_word = complete_attempt_word[-(no_of_words.get()):]
            attempt_words = list(attempt_word)
            complete_attempt_words.append(attempt_word)
    
def attempt_verify():
    global attempt_word, hints, entries
    attempt_cleaner()
    
    hint = wordle_automation.hints(attempt_word, wordle_word)
    hints.append(hint)
    
    entry_disable(row)
    
                    
def entry_disable(row):
    global complete_attempt_word, counter
    if set(hints[-1]) == {1}:
        print("you won")
        disable_hint_list = [0, 0, 0, 0, 0]
        disable_words = " " * no_of_words.get()
        attempt_no = len(hints)
        for i in range(no_of_words.get() - attempt_no):
            hints.append(disable_hint_list)
            complete_attempt_words.append(disable_words)
        
        with open("games_won.txt", "r+") as file:
            content = file.read()
            file.truncate(0)
            file.write(str(int(content) + 1))
        
        for x in range(1, no_of_words.get() + 1):
            for y in range(1, no_of_words.get() + 1):
                attempt_box = Entry(game_window, justify = CENTER, font=('Arial bold',17), width = 3)
                attempt_box.grid(row = x, column = y, padx = 2, pady = 2)
                attempt_box.insert(0 ,complete_attempt_words[x - 1][y - 1])
                flag = int(hints[x - 1][y - 1])
                if flag == 1:
                    attempt_box.config(disabledbackground = "#67CB00")
                elif flag == -1:
                    attempt_box.config(disabledbackground = "#FFEB00")
                elif flag == 0:
                    attempt_box.config(disabledbackground = "grey")
                
                attempt_box.config(state = DISABLED)
                
    else: 
        if (row[-1]+1) < no_of_words.get() + 1:    
            for x in range(1, (row[-1]+1)):
                for y in range(1, no_of_words.get() + 1):
                    attempt_box = Entry(game_window, justify = CENTER, font=('Arial bold',17), width = 3)
                    attempt_box.grid(row = x, column = y, padx = 2, pady = 2)
                    attempt_box.insert(0 ,complete_attempt_words[x - 1][y - 1])
                    flag = int(hints[x - 1][y - 1])
                    if flag == 1:
                        attempt_box.config(disabledbackground = "#67CB00")
                    elif flag == -1:
                        attempt_box.config(disabledbackground = "#FFEB00")
                    elif flag == 0:
                        attempt_box.config(disabledbackground = "grey")
                    
                    attempt_box.config(state = DISABLED)
        else:
            game_window.quit()
            return game_over()
            
    counter += 4                   
    row.append((row[-1]+1))

def give_up():
    quit()
    
def play_again():
    os.execv(sys.executable, ['python'] + sys.argv)
    
def game_over():
    
    game_over_window = Tk()
    
    game_over_window.geometry("180x160")
    
    dummy4 = Label(game_over_window, text = "     ")
    dummy4.grid(row = 0, column = 0)
    
    dummy5 = Label(game_over_window, text = "     ")
    dummy5.grid(row = 1, column = 1)
    
    lost = Label(game_over_window, text = "YOU LOST!", font = ('Arial', 12, "bold"))
    lost.grid(row = 2, column = 2)
    
    play_again_button = Button(game_over_window, text = "Play again", command = play_again)
    play_again_button.grid(row = 3, column = 2)
    
    quit_button = Button(game_over_window, text = "quit", command = give_up)
    quit_button.grid(row = 4, column = 2)
    
    game_over_window.mainloop()

def start_window():

    global window, no_of_words, complete_attempt_word, hints, counter, attempt_words
    
    complete_attempt_word = ""
    hints = []
    counter = 0
    attempt_words = []
    
    window = Tk()

    window.title("Wordle")
    window.geometry("250x180")
    
    photo = PhotoImage(file = "Wordle_2021_Icon.png")
    window.iconphoto(False, photo)

    wordle_label = Label(window, text = "Wordle")
    wordle_label.grid(row = 1, column = 3)
    wordle_label.config(font=('Helvatical bold',25))

    no_of_words_label = Label(window, text = "No_of_words")
    no_of_words_label.grid(row = 2, column = 3)
    no_of_words_label.config(font=('Helvatical bold',15))

    no_of_words = IntVar()
    no_of_words_choosen = ttk.Combobox(window, width = 10, textvariable = no_of_words)
    no_of_words_choosen["values"] = tuple([i for i in range(4, 8, 1)])
    no_of_words_choosen.grid(row = 3, column = 3)
    no_of_words_choosen.current()

    start_button = Button(window, text = "Start", width = 10, command = window_switcher)
    start_button.grid(row = 4, column = 3)

    dummy1 = Label(window, text = "           ")
    dummy1.grid(row = 0, column = 0)

    dummy2 = Label(window, text = "           ")
    dummy2.grid(row = 1, column = 1)

    dummy3 = Label(window, text = "           ")
    dummy3.grid(row = 0, column = 4)

    window.mainloop()

def _game_window():
    
    global entries, attempt_box, game_window, attempt, games_won

    #print(no_of_words.get())
    
    entries = []
    width = None #+ (no_of_words.get() * 10)
    height = None #+ (no_of_words.get() * 10)
    high_score  = None
    
    with open("geometry.csv", "r") as file:
        dimensions = list(csv.reader(file))
        
        width = dimensions[no_of_words.get() - 3][0]
        height = dimensions[no_of_words.get() - 3][1]
        
    with open("games_won.txt", "r") as file:
        content = file.read()
        high_score = "".join(content.split())

    game_window = Tk()
    game_window.title("Wordle")
    game_window.geometry("{}x{}".format(width, height))
    
    photo = PhotoImage(file = "Wordle_2021_Icon.png")
    game_window.iconphoto(False, photo)
    
    header = Label(game_window, text = "You have {} attempts!".format(no_of_words.get()), width = 16, font = ('Arial',14))
    header.grid(row = 0, column = 2, pady = 5, columnspan = 4)
    
    for x in range(1, no_of_words.get() + 1):
        for y in range(1, no_of_words.get() + 1):
            attempt = StringVar()
            attempt_box = Entry(game_window, textvar = attempt, justify = CENTER, font=('Helvatical bold',17), width = 3)
            attempt_box.grid(row = x, column = y, padx = 2, pady = 2)
            entries.append(attempt_box)
    
    
    give_up_button = Button(game_window, text = "Quit", width = 7, font = ('Arial',13), command = give_up)
    give_up_button.grid(row = 7 + (no_of_words.get() - 2), column = no_of_words.get() - 1, padx = 2, pady = 1, columnspan = 2)
    
    attempt_button = Button(game_window, text = "attempt", width = 7, font = ('Arial',13), command = attempt_verify)
    attempt_button.grid(row = 7 + (no_of_words.get() - 2), column = 1, padx = 2, pady = 1, columnspan = 2)
    
    games_won = Label(game_window, text = "games won:{}".format(high_score), font = ('Arial',12))
    games_won.grid(row = 8 + (no_of_words.get() - 2), column = 1, padx = 2, pady = 1, columnspan = 3)
    
    dummy1 = Label(game_window, text = "           ")
    dummy1.grid(row = 0, column = 0)

    #dummy2 = Label(game_window, text = "           ")
    #dummy2.grid(row = 1, column = 1)

    #dummy3 = Label(game_window, text = "           ")
    #dummy3.grid(row = 0, column = 4)
    
    game_window.mainloop()
    
start_window()