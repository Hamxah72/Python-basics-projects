from tkinter import *


root = Tk()
root.title("Hamxah")
root.geometry("400x400")

def button_hover(event):  # Add 'event' parameter to handle the event
    my_button["bg"] = "white"
    status_label.config(text="I'm Hovering Over The Button!")

def button_hover_leave(event):
    my_button["bg"] = "lightgray"
    status_label.config(text="")


my_button = Button(root, text="Click Me", font=("Helvetica", 28))
my_button.pack(pady=50)

status_label = Label(root, text="", bd=1, relief=SUNKEN, anchor=E)
status_label.pack(fill=X, side=BOTTOM, ipady=2)

my_button.bind("<Enter>", button_hover)  # Binding the event
my_button.bind("<Leave>", button_hover_leave)

root.mainloop()
