from tkinter import *
from tkinter import ttk
import wordle_automation

def window_switcher():
    global row, attempt_word, wordle_word
    attempt_word = ""
    row = [1]
    wordle_automation.create_word_file(no_of_words.get())
    wordle_word = wordle_automation.pick_word(wordle_automation.file_name)
    print(wordle_word)
    window.destroy()
    _game_window()

def attempt_cleaner():
    global attempt_word
    attempt_word = ""
    for entry in entries:
        if entry.get() != "":
            attempt_word += entry.get().lower()
    #print("HERE")
    
def attempt_verify():
    global attempt_word, hint
    attempt_cleaner()
    
    hint = wordle_automation.hints(attempt_word, wordle_word)
    print(hint)
    
    entry_disable(row)
    attempt_word = ""
                    
def entry_disable(row):
    global counter
    counter = 0
    if (row[-1]+1) <= no_of_words.get() + 1:
        for x in range(1, (row[-1]+1)):
            counter+=1
            for y in range(1, no_of_words.get() + 1):
                attempt_box = Entry(game_window, justify = CENTER, font=('Arial bold',17), width = 3)
                attempt_box.grid(row = x, column = y, padx = 2, pady = 2)
                attempt_box.insert(0, attempt_word[y - 1])
                #attempt_box_color()
                flag = int(hint[y - 1])
                if flag == 1:
                    attempt_box.config(disabledbackground = "#67CB00")
                elif flag == -1:
                    attempt_box.config(disabledbackground = "#FFEB00")
                elif flag == 0:
                    attempt_box.config(disabledbackground = "grey")
                    
                attempt_box.config(state = DISABLED)
    #if counter <= 6:
    #    counter = 0                     
    row.append((row[-1]+1))
                       
def give_up():
    quit()

def start_window():

    global window, no_of_words
    
    window = Tk()

    window.title("Wordle")
    window.geometry("250x180")

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
    
    global entries, attempt_box, game_window, attempt

    #print(no_of_words.get())
    
    entries = []

    game_window = Tk()
    game_window.title("Wordle")
    game_window.geometry("310x250")
    
    header = Label(game_window, text = "You have {} attempts!".format(no_of_words.get()), width = 16, font = ('Arial',14))
    header.grid(row = 0, column = 2, pady = 5, columnspan = 4)
    
    for x in range(1, no_of_words.get() + 1):
        for y in range(1, no_of_words.get() + 1):
            attempt = StringVar()
            attempt_box = Entry(game_window, textvar = attempt, justify = CENTER, font=('Helvatical bold',17), width = 3)
            attempt_box.grid(row = x, column = y, padx = 2, pady = 2)
            entries.append(attempt_box)
    
    
    give_up_button = Button(game_window, text = "Give up", width = 7, font = ('Arial',13), command = give_up)
    give_up_button.grid(row = 7 + (no_of_words.get() - 2), column = 4 + (no_of_words.get() - 5), padx = 2, pady = 7, columnspan = 2)
    
    attempt_button = Button(game_window, text = "attempt", width = 7, font = ('Arial',13), command = attempt_verify)
    attempt_button.grid(row = 7 + (no_of_words.get() - 2), column = 1 + (no_of_words.get() - 5), padx = 2, pady = 7, columnspan = 2)
    
    dummy1 = Label(game_window, text = "           ")
    dummy1.grid(row = 0, column = 0)

    #dummy2 = Label(game_window, text = "           ")
    #dummy2.grid(row = 1, column = 1)

    #dummy3 = Label(game_window, text = "           ")
    #dummy3.grid(row = 0, column = 4)
    
    game_window.mainloop()
    
start_window()
