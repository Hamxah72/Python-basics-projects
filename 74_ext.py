from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title("Hamxah")
root.geometry("600x400")

def open_program():
    my_program = filedialog.askopenfilename()
    my_label.config(text=my_program)
    # Open the program
    os.system(my_program)

my_button = Button(root, text="Open Program", command=open_program)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)


root.mainloop()