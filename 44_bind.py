from tkinter import *

root = Tk()
root.title("Hamxah")
root.geometry("400x400")

def clicker(event):
    myLabel = Label(root, text="You clicked this button: " + event.char)
    myLabel.pack()

myButton = Button(root, text="Click Me!")
myButton.bind("<KeyPress>", clicker)

myButton.pack(pady=20)

root.mainloop()
