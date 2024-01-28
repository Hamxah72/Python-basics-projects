from tkinter import *
from PIL import Image, ImageTk
import mysql.connector

root = Tk()
root.title("Hamxah")
root.geometry("400x400")

mydb  = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
)

print(mydb)

root.mainloop()