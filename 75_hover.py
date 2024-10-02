from tkinter import *

root = Tk()
root.title("Hamxah")
root.geometry("800x600")


def change(e):
    my_pic = PhotoImage(file="/home/hamza/Pictures/IG_SShorts/Vini1.png/")
    my_label.config(image=my_pic)
    my_label.image = my_pic

def change_back(e):
    my_pic = PhotoImage(file="/home/hamza/Pictures/IG_SShorts/JO.png/")
    my_label.config(image=my_pic)
    my_label.image = my_pic

def do_something():
    Label2 = Label(root, text="You clicked the button")
    Label2.pack()

my_pic = PhotoImage(file="/home/hamza/Pictures/IG_SShorts/JO.png/")
my_label = Button(root, image=my_pic,command=do_something)
my_label.pack(pady=20)


my_label.bind("<Enter>", change)
my_label.bind("<Leave>", change_back)


root.mainloop()