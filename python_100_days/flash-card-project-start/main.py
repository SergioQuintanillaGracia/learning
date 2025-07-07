from random import choice
from tkinter import *
import pandas as pd
import pandas.errors

BACKGROUND_COLOR = "#B1DDC6"

data = []
lang_foreign = None
lang_main = None
curr_word = None
flip_card_after_timer = None
finished = False


def read_data():
    """Initializes data in the form: [{'French': 'partie', 'English': 'part'}, ...]"""

    global data, lang_foreign, lang_main

    try:
        dataframe = pd.read_csv("data/words_to_learn.csv")
    except (FileNotFoundError, pandas.errors.EmptyDataError):
        dataframe = pd.read_csv("data/french_words.csv")

    data = dataframe.to_dict(orient="records")
    languages = dataframe.columns.values.tolist()
    lang_foreign = languages[0]
    lang_main = languages[1]


def button_wrong_pressed():
    new_word()


def button_right_pressed():
    if not finished:
        data.remove(curr_word)
        dataframe = pd.DataFrame(data)
        dataframe.to_csv("data/words_to_learn.csv", index=False)

        new_word()


def new_word():
    global curr_word, flip_card_after_timer, finished

    if flip_card_after_timer:
        root.after_cancel(flip_card_after_timer)

    if len(data) == 0:
        finished = True

    if not finished:
        curr_word = choice(data)
        card.itemconfig(card_bg_image, image=card_front_image)
        card.itemconfig(text_lang, text=lang_foreign, fill="black")
        card.itemconfig(text_word, text=curr_word[lang_foreign], fill="black")

        flip_card_after_timer = root.after(3000, flip_card)
    else:
        card.itemconfig(card_bg_image, image=card_front_image)
        card.itemconfig(text_lang, text="Finished", fill="black")
        card.itemconfig(text_word, text="Congratulations!", fill="black")


def flip_card():
    global curr_word
    card.itemconfig(card_bg_image, image=card_back_image)
    card.itemconfig(text_lang, text=lang_main, fill="white")
    card.itemconfig(text_word, text=curr_word[lang_main], fill="white")


read_data()

root = Tk()
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")
root.title("Flashy")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_bg_image = card.create_image(800 / 2, 526 / 2, image=card_front_image)
card.grid(row=0, column=0, columnspan=2)

text_lang = card.create_text(400, 140, text="Language", font=("Ariel", 30, "italic"))
text_word = card.create_text(400, 250, text="Word", font=("Ariel", 60, "bold"))

wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, command=button_wrong_pressed)
button_wrong.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image, highlightthickness=0, command=button_right_pressed)
button_right.grid(row=1, column=1)

new_word()

root.mainloop()
