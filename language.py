from tkinter import *
import pandas as pd
from random import *
import tkinter.font as font


root = Tk()
root.title('Potae - Wordgame')
root.iconbitmap(r'C:\Users\Tae\Desktop\future skill\pythonProject\china.ico')
root.geometry("550x500")
FONT1 = ('4711_AtNoon_Regular', 20)


df = pd.read_excel(r'C:\Users\Tae\Desktop\future skill\pythonProject\data.xlsx')
words = list(map(tuple, df.to_numpy()))

# get a count of our word list
count = len(words)
def next():
    global hinter, hint_count
    # Clear the screen after next
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    # Reset Hint
    hinter = ""
    hint_count = 0
    # Create random selection
    global random_word
    random_word = randint(0, count-1)
    # Update label with chinese word
    chinese_word.config(text=words[random_word][0])

def answer():
    if my_entry.get() == words[random_word][2]:
        answer_label.config(text=f"Correct! {words[random_word][0]} is {words[random_word][2]}")
    else:
        answer_label.config(text=f"Incorrect! {words[random_word][0]} is not {my_entry.get()}")

hinter = ""
hint_count = 0

def hint():
    hint_label.config(text=f"{words[random_word][1]}")
    #global  hint_count
    #global hinter
    #if hint_count < len(words[random_word][2]):
        #hinter = hinter + words[random_word][2][hint_count]
        #hint_label.config(text=hinter)
        #hint_count +=1

chinese_word = Label(root, text="", font=("Helvetica", 36))
chinese_word.pack(pady=50)

answer_label = Label(root, text="", font = FONT1)
answer_label.pack(pady=20)

my_entry = Entry(root, font = FONT1)
my_entry.pack(pady=20)

# Create Button

button_frame = Frame(root)
button_frame.pack(pady=20)


answer_button = Button(button_frame, text="Answer", font="Helvetica 15", command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button = Button(button_frame, text="Next Word", font="Helvetica 15", command=next)
next_button.grid(row=0, column=1)

hint_button = Button(button_frame, text="Hint", font="Helvetica 15", command=hint)
hint_button.grid(row=0, column=2, padx=20)

# Create hint label
hint_label = Label(root, text="", font=("Helvetica", 28))
hint_label.pack(pady=15)

# Run next function when program start
next()

root.eval('tk::PlaceWindow . center')
root.mainloop()
