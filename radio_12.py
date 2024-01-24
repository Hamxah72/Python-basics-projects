from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Hamxah")

# r = IntVar()
# r.set("2")


CHOPPINGS = [
    ("Rice", "Rice"),
    ("Beans", "Beans"),
    ("Tuwo", "Tuwo"),
    ("Danwake", "Danwake"),
    
]


munches = StringVar()
munches.set("Rice")

for text, topping in CHOPPINGS:

    Radiobutton(root, text=text, variable=munches, value=topping).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

# myLabel = Label(root, text=munches.get())
# myLabel.pack()
 
myButton = Button(root, text="Click Me!", command=lambda: clicked(munches.get()))
myButton.pack()

mainloop()