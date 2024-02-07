from tkinter import *
from PIL import Image, ImageTk
from random import randint
import os

root = Tk()
root.title("Hamxah Flashcard!")
root.geometry("500x600")

def state_answer():
    answer = answer_input.get()
    answer = answer.replace(" ", "")

    if answer.lower() == our_states[rando].lower():
        response = "Correct!"
    else:
        response = "Incorrect!"

    answer_label.config(text=response)


def states():
    hide_all_frames()
    state_frame.pack(fill=BOTH, expand=1)
    my_label = Label(state_frame, text="States").pack()


    # Create a list of state names
    global our_states
    our_states = [
        "Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe", "Kano", "Kaduna", "Katsina", "Jigawa", "Kebbi", "Sokoto", "Zamfara" 
    ]

    # Generatea random number
    global rando
    rando = randint(0, len(our_states)-1)
    state = "/home/hamza/Desktop/venv/hamzakinter/States/" + our_states[rando] + ".png"

    # Create our state images
    global state_image
    state_image = ImageTk.PhotoImage(Image.open(state))
    show_state = Label(state_frame, image=state_image)
    show_state.pack(pady=1)


    # Create answer input box
    global answer_input
    answer_input = Entry(state_frame,font=("Helvetica", 18))
    answer_input.pack(pady=15)


    # Create a button to randomize state images
    rando_button = Button(state_frame, text="Pass",command=states)
    rando_button.pack(pady=15)

    # Create button to answer the question
    answer_button = Button(state_frame, text="Answer", command=state_answer)
    answer_button.pack(pady=5)

    # Create a label to tell us if we got the answer right or wrong
    global answer_label
    answer_label = Label(state_frame, text="", font=("Helvetica", 18))
    answer_label.pack(pady=15)


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
