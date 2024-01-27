from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import os

# Print the current working directory
print("Current Working Directory:", os.getcwd())

# Check if the database file exists
db_file_path = "adress_book.db"
print("Database file exists:", os.path.isfile(db_file_path))


root = Tk()
root.title("Hamxah")
root.geometry("400x600")

# Create a database or connect to one
conn = sqlite3.connect("adress_book.db")

# Create a cursor
c = conn.cursor()

# Create a database or connect to one
conn = sqlite3.connect(os.path.join(os.getcwd(), "adress_book.db"))


# Create a table
try:
    c.execute("""CREATE TABLE addresses (
                first_name text,
                last_name text,
                address text,
                city text,
                state text,
                zipcode integer)
                """)
except sqlite3.Error as e:
    print("SQLite error:", e)

c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='addresses';")
table_exists = c.fetchone()
print("Table exists:", bool(table_exists))

# Create Edit fnction to a record
def update():
     # Create a database or connect to one
    conn = sqlite3.connect("adress_book.db")
    # create a cursor
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
              first_name = :first,
              last_name = :last,
              address = :address,
              city = :city,
              state = :state,
              zipcode = :zipcode

              WHERE oid = :oid""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),

                  'oid': record_id

              } )


    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    editor.destroy()

def edit():
    global editor
    editor = Tk()
    editor.title("Update A Record")
    editor.geometry("400x300")
     # Create a database or connect to one
    conn = sqlite3.connect("adress_book.db")
    # create a cursor
    c = conn.cursor()

    record_id = delete_box.get()
    #Query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    # Create a global for text boxe names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor


    #Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    delete_box_editor = Entry(editor, width=30)
    delete_box_editor.grid(row=9, column=1, pady=5)

     # Loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    #Create Text Box labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    # Create a save button to save edited Record
    edit_btn = Button(editor, text="Save Record", command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)



# Create function to delete a record
    # Create function to delete a record
# def delete():
#     # Use the global connection and cursor
#     global conn, c

#     # Delete a record
#     c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

#     # Commit changes
#     conn.commit()

#     # Close connection
#     conn.close()
    
def delete():
    # Print delete_box value
    print("Delete Box Value:", delete_box.get())

    # Create a database or connect to one
    conn = sqlite3.connect("adress_book.db")
    # Create a cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    delete_box.delete(0, END)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()



#Create a submit function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect("adress_book.db")
    # create a cursor
    c = conn.cursor()

    # Insert into label
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # connect changes
    conn.commit()

    # Close connection
    conn.close()

    #Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#Create Querry Func
def query():
    # Create a database or connect to one
    conn = sqlite3.connect("adress_book.db")
    # create a cursor
    c = conn.cursor()

    #Query the database
    c.execute("SELECT *, oid FROM  addresses")
    records = c.fetchall()
    # print(records)

    #  loop thru results
    print_records = '' 
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[6]) + "\t" +"\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

#Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

global delete_box
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

#Create Text Box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Addrees").grid(row=2, column=0)

city_label = Label(root, text="City").grid(row=3, column=0)

state_label = Label(root, text="State").grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text=" Select ID")
delete_box_label.grid(row=9, column=0, pady=5)


# Create a submit button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a query button 
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Create a delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Create an update button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

# connect changes
conn.commit()

# Close connection
conn.close()


root.mainloop()

# And here's the error(
# And here is the error (c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
# sqlite3.OperationalError: no such table: addresses)
# )