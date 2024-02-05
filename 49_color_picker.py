from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Hamxah")
root.geometry("400x400")

def color():
    my_color = colorchooser.askcolor()[1]  # Extracting the hexadecimal color value
    my_label = Label(root, text=f"RGB: {my_color}", pady=10).pack()
    my_label_2 = Label(root, text="You Picked A Color!", font=("Helvetica", 32), bg=my_color).pack()

my_button = Button(root, text="Pick A Color", command=color).pack()

root.mainloop()
