from tkinter import *
from PIL import Image, ImageTk
from random import randint
import os
import random

root = Tk()
root.title("Hamxah Flashcard!")
root.geometry("500x600")

# Create randomizing state function
def random_state():
    # Create a list of state names
    global our_states
    our_states = [
        "Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe", "Kano", "Kaduna", "Katsina", "Jigawa", "Kebbi", "Sokoto", "Zamfara" 
    ]

    # Generate random number
    global rando
    rando = randint(0, len(our_states)-1)
    state = "/home/hamza/Desktop/venv/hamzakinter/States/" + our_states[rando] + ".png"

    # Create our state images
    global state_image
    state_image = ImageTk.PhotoImage(Image.open(state))
    show_state.config(image=state_image, bg="white")
    

# Create state capital answers
def state_capital_answer():
    if capital_radio.get() == our_state_capitals[answer]:
        response = "Correct! " + our_state_capitals[answer].title() + " is the capital of " + answer.title()
    else:
        response = "Incorrect! " + our_state_capitals[answer].title() + " is the capital of " + answer.title()

    answer_label_capitals.config(text=response)






def state_answer():
    answer = answer_input.get()
    answer = answer.replace(" ", "")

    if answer.lower() == our_states[rando].lower():
        response = "Correct! " + our_states[rando]
    else:
        response = "Incorrect! " + our_states[rando].title()

    answer_label.config(text=response)

    # Clear the entry box
    answer_input.delete(0, "end")

    random_state()


def states():
    hide_all_frames()
    state_frame.pack(fill=BOTH, expand=1)
    # my_label = Label(state_frame, text="States").pack()


    '''
    # Create a list of state names
    global our_states
    our_states = [
        "Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe", "Kano", "Kaduna", "Katsina", "Jigawa", "Kebbi", "Sokoto", "Zamfara" 
    ]

    # Generate random number
    global rando
    rando = randint(0, len(our_states)-1)
    state = "/home/hamza/Desktop/venv/hamzakinter/States/" + our_states[rando] + ".png"

    # Create our state images
    global state_image
    state_image = ImageTk.PhotoImage(Image.open(state))
    '''
    global show_state
    show_state = Label(state_frame)
    show_state.pack(pady=15)
    random_state()

    

    # Create answer input box
    global answer_input
    answer_input = Entry(state_frame,font=("Helvetica", 18), bd=2)
    answer_input.pack(pady=15)


    # Create a button to randomize state images
    rando_button = Button(state_frame, text="Pass",command=states)
    rando_button.pack(pady=15)

    # Create button to answer the question
    answer_button = Button(state_frame, text="Answer", command=state_answer)
    answer_button.pack(pady=5)

    # Create a label to tell us if we got the answer right or wrong
    global answer_label
    answer_label = Label(state_frame, text="", font=("Helvetica", 18), bg="white")
    answer_label.pack(pady=15)


def state_capitals():
    hide_all_frames()
    state_capitals_frame.pack(fill=BOTH, expand=1)
    # my_label = Label(state_capitals_frame, text="Capitals").pack()

    global show_state
    show_state = Label(state_capitals_frame)
    show_state.pack(pady=15)

    

    global our_states
    our_states = [
            "Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe", "Kano", "Kaduna", "Katsina", "Jigawa", "Kebbi", "Sokoto", "Zamfara" 
        ]

    global our_state_capitals
    our_state_capitals = {
        "Adamawa":"Yola",
        "Bauchi":"Bauchi",
        "Borno":"Maiduguri",
        "Gombe":"Gombe",
        "Taraba":"Jalingo",
        "Yobe":"Damaturu",
        "Kano":"Kano",
        "Kaduna":"Kaduna",
        "Katsina":"Katsina",
        "Jigawa":"Dutse",
        "Kebbi": "Birnin Kebbi",
        "Sokoto":"Sokoto",
        "Zamfara":"Gusau"
    }

    # Create empty answer list and counter 
    answer_list = []
    count = 1
    global answer


    # Generate our 3 random numbers
    while count < 4:
        rando = randint(0, len(our_states)-1)

        # If 1st selection, make it our answer
        if count == 1:
            answer = our_states[rando]
            global state_image
            state = "/home/hamza/Desktop/venv/hamzakinter/States/" + our_states[rando] + ".png"
            state_image = ImageTk.PhotoImage(Image.open(state))
            show_state.config(image=state_image)

        # Add our 1st selection to a new list
        answer_list.append(our_states[rando])

        # Remove from old list
        our_states.remove(our_states[rando])

        # Shuffle original list
        random.shuffle(our_states)
        count += 1


    random.shuffle(answer_list)

    global capital_radio
    capital_radio = StringVar()
    capital_radio.set(our_state_capitals[answer_list[0]])

    capital_radio_button1 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[0]].title(), variable=capital_radio, value=our_state_capitals[answer_list[0]]).pack()

    capital_radio_button2 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[1]].title(), variable=capital_radio, value=our_state_capitals[answer_list[1]]).pack()

    capital_radio_button3 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[2]].title(), variable=capital_radio, value=our_state_capitals[answer_list[2]]).pack()
    
    # Add a Pass Button
    pass_button = Button(state_capitals_frame, text="Pass", command=state_capitals)
    pass_button.pack(pady=15)

    # Create a button to answer
    capital_answer_button = Button(state_capitals_frame, text="Answer", command=state_capital_answer)
    capital_answer_button.pack(pady=15)

    # Craete an answer label 
    global answer_label_capitals
    answer_label_capitals = Label(state_capitals_frame, text="", font=("Helvetica", 18))
    answer_label_capitals.pack(pady=15)



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
state_frame = Frame(root, width=500, height=500, bg="white")
state_capitals_frame = Frame(root, width=500, height=500)


# print("Current Working Directory:", os.getcwd())


root.mainloop()