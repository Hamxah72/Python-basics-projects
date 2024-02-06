from tkinter import *
from PIL import Image, ImageTk
from random import randint
import os

root = Tk()
root.title("Hamxah Flashcard!")
root.geometry("500x600")


def states():
    hide_all_frames()
    state_frame.pack(fill=BOTH, expand=1)
    my_label = Label(state_frame, text="States").pack()


    # Create a list of state names
    our_states = [
        "Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"
    ]

    # Generatea random number
    rando = randint(0, len(our_states)-1)
    state = "/home/hamza/Desktop/venv/hamzakinter/States/" + our_states[rando] + ".png"

    # Create our state images
    global state_image
    state_image = ImageTk.PhotoImage(Image.open(state))
    show_state = Label(state_frame, image=state_image)
    show_state.pack(pady=15)

    # Create a button to randomize state images
    rando_button = Button(state_frame, text="Next State",command=states)
    rando_button.pack(pady=10)



def state_capitals():
    hide_all_frames()
    state_capitals_frame.pack(fill=BOTH, expand=1)
    my_label = Label(state_capitals_frame, text="Capitals").pack()



def hide_all_frames():
    # Loop thru and destroy all children in prev frames
    for widget in state_frame.winfo_children():
        widget.destroy()

    for widget in state_capitals_frame.winfo_children():
        widget.destroy()

    state_frame.pack_forget()
    state_capitals_frame.pack_forget()


# Create our menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create geography menu items
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="States Capitals", command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)


# Create our frames
state_frame = Frame(root, width=500, height=500)
state_capitals_frame = Frame(root, width=500, height=500)


# print("Current Working Directory:", os.getcwd())


root.mainloop()