from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("Hamxah")

def open():
    top = Toplevel()
    top=Tk()
    top.title("Hamxah")
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()



btn = Button(root, text="Open Second Window", command=open).pack()


# lbl = Label(top, text="Hello World!").pack()
# my_img = ImageTk.PhotoImage(Image.open("JO.png"))
# my_label = Label(top, image=my_img).pack()

mainloop()