# import tkinter
from tkinter import *


window = Tk()
window.title("My Program")
# window.geometry("500x300")
window.minsize(500, 300)

#My Label
mylabel = Label(text="My Label",font=("Arial",20,"italic"))
mylabel.pack() #this is important to showup the label on window
# mylabel["text"] = "This is my label"
# mylabel.config(text="This is my label") - these both are diff ways to do the same




#Button
def button_clicked():
    mylabel.config(text=input.get())

button = Button(text="My Button",command=button_clicked)
button.pack()


#Entry
input = Entry(width=10)
input.pack()


window.mainloop()
