from tkinter import *
from PIL import Image, ImageTk
import sqlite3

root = Tk()
root.title("Hamxah")
root.geometry("400x400")

# Create a database or connect to one

conn = sqlite3.connect("adress_book.db")

# create a cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE addresses (
          first_name text,
          last_name text,
          address text,
          city text,
          state text,
          zipcode integer)""")


# connect changes
conn.commit()

# Close connection
conn.close()


root.mainloop()