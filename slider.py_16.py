from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Hamxah")
root.geometry("400x400")


vertical = Scale(root, from_=0, to=400)
vertical.pack()

def slide2():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(horizontal.get()))

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()



my_label = Label(root, text=vertical.get()).pack()
my_label = Label(root, text=horizontal.get()).pack()

def slide():
    my_label = Label(root, text=vertical.get()).pack()
    root.geometry(str(vertical.get()) + "x400")



my_btn = Button(root, text="Click Me!", command=slide).pack()
my_btn2 = Button(root, text="Click Me!", command=slide2).pack()




root.mainloop()