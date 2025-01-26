from tkinter import *
import math
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier New"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    label.config(text = "Timer", font = (FONT_NAME, 30, "bold"), bg = YELLOW, fg = GREEN)
    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    check_label.config(text = "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        countdown(work_seconds)
        label.config(text = "Focus Time", font = (FONT_NAME, 30, "bold"), bg = YELLOW, fg = GREEN)
    if reps == 2 or reps == 4 or reps == 6:
        countdown(short_break_seconds)
        label.config(text="Short Break", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=PINK)
    elif reps == 8:
        countdown(long_break_seconds)
        label.config(text="Long Break", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=RED)
    elif reps == 9:
        messagebox.showinfo(title="Session Completed", message = "Congratulations you focused & worked hard for 100 mins!")
        reset()



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time

def countdown(count):

    global check_label
    count_min = math.floor(count/60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_min == 0:
        count_min = "00"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    elif count == 0:
        start_timer()
        if reps % 2 == 0:
            var = int(reps/2)
            check = "✔"*var
            check_label = Label(text = check, font = (FONT_NAME, 20, "bold"), fg = GREEN, bg = YELLOW)
            check_label.grid(column = 1, row =3)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 50, pady = 50, bg = YELLOW)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100,130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)

label = Label(text = "Timer", font = (FONT_NAME, 30, "bold"), bg = YELLOW, fg = GREEN)
label.grid(column = 1, row = 0)

start_button = Button(text = "Start", width = 10, font = (FONT_NAME, 12, "bold"), command = start_timer)
start_button.grid(column = 0, row = 2)

reset_button = Button(text = "Reset", width = 10, font = (FONT_NAME, 12, "bold"), command = reset)
reset_button.grid(column = 2, row = 2)

check_label = Label( text = "", font = (FONT_NAME, 20, "bold"), fg = GREEN, bg = YELLOW)
check_label.grid(column = 1, row =3)


window.mainloop()