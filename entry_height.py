from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Hamxah")
root.geometry("400x400")

def myclick():
    hello ="Assalamu Akaikh Ya " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, "end")
    myLabel.pack(pady=10)


e = Entry(root, width=50, font=("Helvetica", 24))
e.pack(padx=10, pady=10)

mybutton = Button(root, text="Enter Your Name", command=myclick)
mybutton.pack(pady=10)



root.mainloop()