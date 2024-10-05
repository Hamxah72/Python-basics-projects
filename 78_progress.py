from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title("Hamxah")
root.geometry("600x400")

def step():
    my_progress["value"] += 10
    my_label.config(text=my_progress["value"])
    # my_progress.start(10)

    '''
    for x in range(5):
        my_progress["value"] += 20
        root.update_idletasks()
        time.sleep(1)
    '''


def stop():
    my_progress.stop()


my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode="determinate")

my_progress.pack(pady=20)


my_button = Button(root, text="Progress", command=step)
my_button.pack(padx=20)

my_button2 = Button(root, text="stop", command=stop)
my_button2.pack(padx=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()