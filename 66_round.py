from tkinter import *
import os

root = Tk()
root.title("Hamxah")
root.geometry("400x400")


def thing():
    my_label.config(text="You clicked the button...")

login_btn = PhotoImage(file="/home/hamza/Desktop/venv/hamzakinter/login.png")

img_label = Label(image=login_btn)

my_btn = Button(root, image=login_btn, command=thing, borderwidth=0)
my_btn.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)


root.mainloop()