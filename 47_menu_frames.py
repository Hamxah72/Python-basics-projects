from tkinter import *

root = Tk()
root.title("Hamxah")
root.geometry("400x400")

my_menu = Menu(root)
root.config(menu=my_menu)

def our_command():
    my_label = Label(root, text="You clicked a Dropdown Menu!").pack()

def file_new():
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)
    my_label = Label(file_new_frame, text="You Clicked The File >> New Menu!").pack()

def edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill="both", expand=1)
    my_label = Label(edit_cut_frame, text="You Clicked The Edit >> Cut Menu!").pack()

def hide_all_frames():
    edit_cut_frame.pack_forget()
    file_new_frame.pack_forget()

# Create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an edit menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=our_command)

# Create an option menu
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find", command=our_command)
option_menu.add_command(label="Find Next", command=our_command)

file_new_frame = Frame(root, width=400, height=400, background="purple")
edit_cut_frame = Frame(root, width=400, height=400, background="yellow")

root.mainloop()