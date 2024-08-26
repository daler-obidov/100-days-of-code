from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("code/day-31/words.csv")
learn = data.to_dict(orient='records')

current_card = {}
flip_timer = None

def next_card():
    global current_card, flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    current_card = random.choice(learn)
    canvas.itemconfig(card_title, text='Korean', fill='Black')
    canvas.itemconfig(card_word, text=current_card['Korean'], fill='Black')
    canvas.itemconfig(card_background, image=card_front) 
    flip_timer = window.after(5000, func=change_card)

def change_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_image)

# def learned

window = Tk()
window.title('Card Game')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_back_image = PhotoImage(file='/home/daler/code/100-days-of-code/code/day-31/images/card_back.png')
card_front = PhotoImage(file="/home/daler/code/100-days-of-code/code/day-31/images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front)

canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))

image2 = PhotoImage(file='/home/daler/code/100-days-of-code/code/day-31/images/wrong.png')
wrong_button = Button(image=image2, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

image3 = PhotoImage(file='/home/daler/code/100-days-of-code/code/day-31/images/right.png')
check_button = Button(image=image3, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
check_button.grid(row=1, column=1)

word_entry = Entry(window, font=('Ariel', 15))
word_entry.grid(row=1, column=0, columnspan=2)

next_card()

window.mainloop()
