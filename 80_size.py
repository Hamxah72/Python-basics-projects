from tkinter import *

root = Tk()
root.title("Hamxah")
root.geometry("600x400")

def resize(): 
    w = width_entry.get()
    h = height_entry.get()
    root.geometry(f"{w}x{h}")

width_label = Label(root, text="Width")
width_label.pack(pady=20)
width_entry = Entry(root)
width_entry.pack()

height_label = Label(root, text="Height")
height_label.pack(pady=20)
height_entry = Entry(root)
height_entry.pack()


my_button = Button(root, text="Resize", command=resize)
my_button.pack(pady=20)


root.mainloop()