from tkinter import *
from random import choice
from random import shuffle

root = Tk()
root.title("Hamxah")
root.geometry("400x400")

my_label = Label(root, text="",font=("Helvetica", 30))
my_label.pack(pady=20)


def shuffler():
    # Clear Hint Label
    hint_label.config(text="")

    # Clear Hint Count
    global hint_count
    hint_count = 0 

    # Clear Answer Box
    entry_answer.delete(0, END)

    # Clear Answer Label
    answer_label.config(text="")

    # List of code words
    codes = [
        'alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliet', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform', 'violet', 'whiskey', 'xray', 'yankee', 'zulu']
    
    # Pick random state from list
    global word
    word = choice(codes)
    

    # Break apart our chosen word
    break_apart_word = list(word)
    shuffle(break_apart_word)


    # turn shuffled list into a word
    global shuffled_word
    shuffled_word = ""
    for letter in break_apart_word:
        shuffled_word += letter


    # Print shuffled word to the screen
    my_label.config(text=shuffled_word)

def answer():
    if word == entry_answer.get():
        answer_label.config(text="Correct!!!")
    else:
        answer_label.config(text="Incorrect!!!")     

# Create Hint Counter
global hint_count
hint_count = 0

# Create Hint Function 
def hint(count):
    global hint_count
    hint_count = count

    # Get the length of the chosen word
    word_length = len(word)

    # Show a hint
    if count < word_length:
        hint_label.config(text=f'{hint_label["text"]} {word[count]}')
        hint_count += 1


entry_answer = Entry(root, font=("Helvetica", 25))
entry_answer.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=10)

my_button = Button(button_frame, text="Pick Another Word", command=shuffler)
my_button.grid(row=0, column=1, padx=10)


hint_button = Button(button_frame, text="Hint", command=lambda: hint(hint_count))
hint_button.grid(row=0, column=2, padx=10)

answer_label = Label(root, text="", font=("helvetica", 18))
answer_label.pack(pady=20)


hint_label = Label(root, font=("Helvetica", 18))
hint_label.pack(pady=10)


shuffler()
root.mainloop()