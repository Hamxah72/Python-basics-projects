from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Hamxah")
root.geometry("400x400")


# Sometimes called option boxes.

def show():
    my_label = Label(root, text=clicked.get()).pack()

option = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set(option)

drop = OptionMenu(root, clicked, *option)
drop.pack()

my_button = Button(root, text="Show Selection", command=show).pack()


root.mainloop()