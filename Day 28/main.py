import tkinter
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
reps = 0
#colourhunt website for the color pallate
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
#can use while loops along side window.mainloop()
def count_down(count):
    global timer
    count_min = int(count/60)
    count_sec = count%60
    canvas.itemconfig(timer_text,text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        timer = window.after(1000, count_down,count-1)
    else:
        start_timer()
        check = "✔︎"
        check_mark.config(text=check*(reps//2))
# ---------------------------- UI SETUP ------------------------------- #

#window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

#canvas - for images on window
canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100 ,112,image=tomato_img) #expects an image of Photoimage to create one on canvas
timer_text = canvas.create_text(100,140,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

#Label
title_label = Label(text="Timer", font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
title_label.grid(row=0,column=1)

#buttons
start_button = Button(text="Start",highlightthickness=0,highlightbackground=YELLOW,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",highlightthickness=0,highlightbackground=YELLOW,command=reset_timer)
reset_button.grid(row=2,column=2)


#check_marks
check_mark = Label(fg=GREEN,bg=YELLOW)
check_mark.grid(row=3,column=1)

window.mainloop()