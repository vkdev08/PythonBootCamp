from tkinter import *

#window
window = Tk()
window.title("Miles to Kilometer converter")
window.minsize(width=300, height=100)
window.config(padx=40, pady=20)

#labels
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles", width=5)
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

output_label = Label(text="0")
output_label.grid(column=1, row=1)

#logic
def miles_to_km():
    miles = int(user_input.get())
    km = miles * 1.60934
    km_in_str = f"{km:.2f}"
    output_label.config(text=km_in_str)

#button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

#input
user_input = Entry(width=5)
user_input.insert(END, string="0")
user_input.grid(column=1, row=0)

window.mainloop()