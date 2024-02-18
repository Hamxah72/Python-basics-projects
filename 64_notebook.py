from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hamxah's Notetab")
root.geometry("500x500")

my_notebook = ttk.Notebook(root)
my_notebook.pack()

def hide():
    my_notebook.hide(1)

def show():
    my_notebook.add(my_frame2, text="Red Tab")

def select():
    my_notebook.select(1)

my_frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
my_frame2 = Frame(my_notebook, width=500, height=500, bg="red")

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="Blue Tab")
my_notebook.add(my_frame2, text="Red Tab")

# Hide a tab 
my_button1 = Button(my_frame1, text="Hide Tab 2", command=hide)
my_button1.pack(pady=10)

# Show a tab 
my_button1 = Button(my_frame1, text="Show Tab 2", command=show)
my_button1.pack(pady=10)

# Navigate to tab 2
my_button1 = Button(my_frame1, text="Navigate to tab 2", command=select)
my_button1.pack(pady=10)

root.mainloop()