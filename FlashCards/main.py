from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
try:
    data = pandas.read_csv("./data/Words_To_Learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    canvas.itemconfig(card_background, image = card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/Words_To_Learn.csv", index = False)
def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_background, image = card_back_img)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func = flip_card)

canvas = Canvas(height=526, width=800, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400,263, image=card_front_img)

card_title = canvas.create_text(400, 150, text = "", font = ("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "", font = ("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan = 2)

cross_image = PhotoImage(file = "./images/wrong.png")
unknown_button = Button(image = cross_image, highlightthickness=0, command = next_card)
unknown_button.grid(column = 0, row = 1)

correct_image = PhotoImage(file = "./images/right.png")
known_button = Button(image = correct_image, command = is_known)
known_button.grid(column = 1, row = 1)

next_card()

window.mainloop()