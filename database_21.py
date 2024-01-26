from tkinter import *
from PIL import Image, ImageTk
import sqlite3

root = Tk()
root.title("Hamxah")
root.geometry("400x400")

# Create a database or connect to one
conn = sqlite3.connect("adress_book.db")

# Create a cursor
c = conn.cursor()

# Create a table
# c.execute("""CREATE TABLE addresses (
#           first_name text,
#           last_name text,
#           address text,
#           city text,
#           state text,
#           zipcode integer)
#           """)

# Create function to delete a record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Craete a cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

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

delete_box_label = Label(root, text=" Delete ID")
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

# connect changes
conn.commit()

# Close connection
conn.close()


root.mainloop()
