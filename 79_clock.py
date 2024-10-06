from tkinter import *
import time

root = Tk()
root.title("Hamxah")
root.geometry("600x400")


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%a")
    time_zone = time.strftime("%Z")

    my_label.config(text=hour + ":" + minute + ":" + second)
    my_label.after(1000, clock) 

    my_label2.config(text=time_zone + " " + day)


def update():
    my_label.config(text="Bravo")

my_label = Label(root, text="", font=("Helvetica",50), fg="blue", bg="black")
my_label.pack(pady=20)

my_label2 = Label(root, text="", font=("Helvetica", 30))
my_label2.pack(pady=20)

clock()

my_label.after(5000, update)

root.mainloop()