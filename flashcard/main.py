BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
from pandas import *


#----------------------UI---------------------
window = Tk()
window.config(height=626, width=900, bg=BACKGROUND_COLOR, padx=50, pady=50)

cardback_img = PhotoImage(file="./images/card_back.png")
cardfront_img = PhotoImage(file="./images/card_front.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

canvas = Canvas(height=526, width=800, highlightthickness=0)
canvas_image = canvas.create_image(0, 0, anchor=NW, image = cardfront_img)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)


rand_eng_word = ""
jebana_mac = []


#---------DATA

with open(file="./data/Spanish Phrases and Vocab.csv") as data_file:
    data = read_csv("./data/Spanish Phrases and Vocab.csv")
    english_word = data["english_word"].to_list()
    spanish_word = data["spanish_word"].to_list()

def generate_word():
    rand_eng_word = random.choice(english_word)
    canvas.itemconfig(canvas_image, image = cardfront_img)
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=f"{rand_eng_word}")
    word_index = english_word.index(rand_eng_word)
    jebana_mac.append(word_index)

def translation():
    word_index = jebana_mac[0]
    matching_spanish_translation = spanish_word[word_index]
    index_in_data = spanish_word.index(matching_spanish_translation)
    canvas.itemconfig(language, text="Spanish")
    canvas.itemconfig(word, text=f"{matching_spanish_translation}")
    canvas.itemconfig(canvas_image, image = cardback_img)
    jebana_mac.clear()


language = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text=f"{rand_eng_word}", font=("Arial", 50, "bold"))

#------BUTTONS---
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

wrong_button = Button(text="Translation", highlightthickness=0, command=translation)
wrong_button.grid(row=1, column=0)

right_buttton = Button(text="New word", highlightthickness=0, command=generate_word)
right_buttton.grid(row=1, column=1)




























window.mainloop()
