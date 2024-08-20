from tkinter import *
from time import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARK_GREEN = "#008000"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

    countdown(25 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):

    count_min = math.floor(count / 60)
    count_secs = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_secs}")

    if count > 0:
        window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW, highlightthickness=0 )
timer_label.grid(column=1, row=0)

check_mark = Label(text='✔', bg=YELLOW, highlightthickness=0, fg=GREEN, font=(FONT_NAME, 20, 'bold'))
check_mark.grid(column=1, row=3)

image_png = PhotoImage(file='/home/daler/code/100-days-of-code/code/day-28/pomodoro-start/tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=image_png)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', highlightthickness=0, bg=DARK_GREEN, font=(FONT_NAME, 15, 'bold'), command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text='Reset', highlightthickness=0, bg=RED, font=(FONT_NAME, 15, 'bold'))
reset_button.grid(column=2, row=3)

window.mainloop()