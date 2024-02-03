from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Hamxah")
root.geometry("400x400")

def myDelete():
    myLabel.pack_forget()
    myLabel.destroy()
    mybutton['state'] = NORMAL
    print(mybutton.winfo_exists())


def myclick():
    global myLabel
    hello ="Assalamu Akaikh Ya " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, "end")
    myLabel.pack(pady=10)
    mybutton['state'] = DISABLED


e = Entry(root, width=50, font=("Helvetica", 24))
e.pack(padx=10, pady=10)

mybutton = Button(root, text="Enter Your Name", command=myclick)
mybutton.pack(pady=10)

deletebutton = Button(root, text="Delete Text", command=myDelete)
deletebutton.pack(pady=10)

root.mainloop()