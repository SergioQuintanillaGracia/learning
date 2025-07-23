import math
from tkinter import *
from tkinter import ttk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "DejaVu Serif"
FONT_NAME_TIMER = "Noto Sans"
FONT_NAME_CHECKMARKS = "Hack"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps

    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    root.lift()

    reps += 1

    if reps % 2 == 1:
        # Odd repetition, work time
        countdown(work_sec)
        title.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        # Time to do a long break
        countdown(long_break_sec)
        title.config(text="Break", fg=RED)
    else:
        # Even repetition and not time to do long break, it's time to do a short break
        countdown(short_break_sec)
        title.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    count_str = f"{count_min}:{count_sec:02d}"

    canvas.itemconfig(timer_text, text=count_str)
    if count > 0:
        timer = root.after(2, countdown, count - 1)
    else:
        start_timer()

        # Add the correct amount of checkmarks
        checkmark_count = math.floor(reps / 2)  # Every 2 reps, we do a 25-min cycle
        checkmarks.config(text="✔" * checkmark_count)

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")
root.title("Pomodoro")
root.config(padx=60, pady=50, bg=YELLOW)

title = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME_TIMER, 30, "bold"))
canvas.grid(row=1, column=1)

button_start = ttk.Button(text="Start", width=6, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = ttk.Button(text="Reset", width=6, command=reset_timer)
button_reset.grid(row=2, column=2)

checkmarks = Label(font=(FONT_NAME_CHECKMARKS, 20, "bold"), bg=YELLOW, fg=GREEN)
checkmarks.grid(row=3, column=1)

root.mainloop()