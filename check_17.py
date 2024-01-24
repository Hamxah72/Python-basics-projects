from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Hamxah")
root.geometry("400x400")

def show():
    my_label = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Select if you prefer PES?", variable=var, onvalue="PES", offvalue="FIFA")
c.deselect()
c.pack()


my_button = Button(root, text="Show selection", command=show)
my_button.pack()

root.mainloop()