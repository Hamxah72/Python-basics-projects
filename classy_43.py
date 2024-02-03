from tkinter import *


root = Tk()
root.title("Hamxah")
root.geometry("400x400")


class Hamxah:

    def __init__(self, master):
        myframe = Frame(master)
        myframe.pack()

        self.myButton = Button(master, text="Click Me!", command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("Look at you... You clicked a button!")

h = Hamxah(root)



root.mainloop()