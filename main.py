from tkinter import *
from random import choice
import pandas

# ---------------------------- EDIT ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
COLUMN1 = "Malayalam"
COLUMN2 = "Malu"
ANSWER = "English"

WORDS_TO_LEARN = "data/words_to_learn.csv"
SOURCE_FILE = "data/Malu-EN.csv"

FRONT_LANGUAGE = "MALAYALAM"
BACK_LANGUAGE = "ENGLISH"

title = ""
sub_title = ""
word = ""
# ---------------------------- LOAD DATA ---------------------------- #

try:
    data = pandas.read_csv(WORDS_TO_LEARN)
except FileNotFoundError:
    data = pandas.read_csv(SOURCE_FILE)

to_learn = data.to_dict(orient="records")
current_card = {}


# ---------------------------- FUNCTIONS ---------------------------- #
def next_card():
    global current_card, flip_timer, title, sub_title, word
    window.after_cancel(flip_timer)  # Reset timer for each new card

    current_card = choice(to_learn)

    canvas.itemconfig(card_title, text=FRONT_LANGUAGE, fill="black")  # Title
    canvas.itemconfig(card_sub_title, text=current_card[COLUMN1], fill="black")  # Original Language
    canvas.itemconfig(card_word, text=current_card[COLUMN2], fill="black")  # Pronounce In English
    canvas.itemconfig(card_img, image=front_image)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Flip the card to show the English translation."""
    canvas.itemconfig(card_title, text=BACK_LANGUAGE, fill="white")
    canvas.itemconfig(card_sub_title, text=current_card[ANSWER], fill="white") #The translation of the word in English
    canvas.itemconfig(card_word, text=current_card[COLUMN2], fill="white") #Pronounce In English
    canvas.itemconfig(card_img, image=back_image)


def is_know():
    """Remove known words and save updated list."""
    to_learn.remove(current_card)

    updated_data = pandas.DataFrame(to_learn)
    updated_data.to_csv("data/words_to_learn.csv", index=False)
    print(len(to_learn))
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Learning Malayalam- 100 Words")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# --- Canvas (Flashcard) --- #
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# ---Front--Image
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

card_img = canvas.create_image(400, 263, image=front_image)

# ---Front--Text
card_title = canvas.create_text(400, 140, text=title, font=("Ariel", 30, "italic"))
card_sub_title = canvas.create_text(400, 220, text=sub_title, font=("Ariel", 30, "bold"))
card_word = canvas.create_text(400, 300, text=word, font=("Ariel", 30, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


# --- Buttons -----
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

Button(image=right_img, command=is_know, bg=BACKGROUND_COLOR, highlightthickness=0).grid(column=1, row=1)
Button(image=wrong_img, command=next_card, bg=BACKGROUND_COLOR, highlightthickness=0).grid(column=0, row=1)

next_card()

window.mainloop()
