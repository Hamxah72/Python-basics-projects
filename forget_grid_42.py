from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Hamxah")
root.geometry("400x400")

myLabel = Label(root)

'''def myDelete():
    myLabel.grid_forget()
    # myLabel.destroy()
    mybutton['state'] = NORMAL
    # print(mybutton.winfo_exists())
'''

def myclick():
    global myLabel
    myLabel = Label(root)
    myLabel.destroy()

    hello ="Assalamu Akaikh Ya " + e.get()
    myLabel = Label(root, text=hello)

    e.delete(0, "end")
    myLabel.grid(row=3, column=0, pady=10)
    # mybutton['state'] = DISABLED


e = Entry(root, width=17, font=("Helvetica", 30))
e.grid(row=0, column=0, pady=10)

mybutton = Button(root, text="Enter Your Name", command=myclick)
mybutton.grid(row=1, column=0, pady=10)

# deletebutton = Button(root, text="Delete Text", command=myDelete)
# deletebutton.grid(row=2, column=0, pady=10)

root.mainloop()