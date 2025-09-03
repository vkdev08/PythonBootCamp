import tkinter
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
#colourhunt website for the color pallate
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
#can use while loops along side window.mainloop()
def count_down(count):
    canvas.itemconfig(timer_text,text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)

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

count_down(5)
#Label
title_label = Label(text="Timer", font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
title_label.grid(row=0,column=1)

#buttons
start_button = Button(text="Start",highlightthickness=0,highlightbackground=YELLOW)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",highlightthickness=0,highlightbackground=YELLOW)
reset_button.grid(row=2,column=2)


#check_marks
check_mark = Label(text="✔︎",fg=GREEN,bg=YELLOW)
check_mark.grid(row=3,column=1)

window.mainloop()