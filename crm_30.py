from tkinter import *
from PIL import Image, ImageTk
import mysql.connector

root = Tk()
root.title("Hamxah")
root.geometry("400x600")

# connect to MySQL
mydb  = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Hamza"
)


# Check to see if MySQL was created.
# print(mydb)



# Create a cursor and initialise it
my_cursor = mydb.cursor()

# Create a database
# my_cusor.execute("CREATE DATABASE Hamza")

# Test to see if database was created
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)

# Create a table
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers \
                  (first_name VARCHAR(255), \
                  last_name VARCHAR(255), \
                  zipcode INT(10), \
                  price_paid DECIMAL(10, 2), \
                  user_id INT AUTO_INCREMENT PRIMARY KEY)")

# Alter table
# Alter table
# my_cursor.execute("ALTER TABLE customers ADD (\
#                   email VARCHAR(255), \
#                   address_1 VARCHAR(255), \
#                   address_2 VARCHAR(255), \
#                   city VARCHAR(50), \
#                   state VARCHAR(50), \
#                   country VARCHAR(255), \
#                   phone VARCHAR(255), \
#                   payment_method VARCHAR(50), \
#                   discount_code VARCHAR(255))")



# Show table
# my_cursor.execute("SELECT * FROM customers")
# # print(my_cursor.description)

# for thing in my_cursor.description:
#     print(thing)


# Create a label
title_label = Label(root, text="Hamxah Customer Database", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Create main form to enter customer data
first_name_label = Label(root, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
last_name_label = Label(root, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
address_1_label = Label(root, text="Address 1").grid(row=3, column=0, sticky=W, padx=10)
address_2_label = Label(root, text="Address 2").grid(row=4, column=0, sticky=W, padx=10)
city_label = Label(root, text="City").grid(row=5, column=0, sticky=W, padx=10)
state_label = Label(root, text="State").grid(row=6, column=0, sticky=W, padx=10)
zipcode_label = Label(root, text="Zipcode").grid(row=7, column=0, sticky=W, padx=10)
country_label = Label(root, text="Country").grid(row=8, column=0, sticky=W, padx=10)
phone_label = Label(root, text="Phone").grid(row=9, column=0, sticky=W, padx=10)
email_label = Label(root, text="Email").grid(row=10, column=0, sticky=W, padx=10)
username_label = Label(root, text="Username").grid(row=11, column=0, sticky=W, padx=10)
payment_method_label = Label(root, text="Payment Method").grid(row=12, column=0, sticky=W, padx=10)
discount_code_label = Label(root, text="Discount Code").grid(row=13, column=0, sticky=W, padx=10)
price_paid_label = Label(root, text="Price Paid").grid(row=14, column=0, sticky=W, padx=10)

# Create entry boxes
first_name_box = Entry(root)
first_name_box.grid(row=1, column=1, pady=5)

last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=5)

address1_box = Entry(root)
address1_box.grid(row=3, column=1, pady=5)

address2_box = Entry(root)
address2_box.grid(row=4, column=1, pady=5)

city_box = Entry(root)
city_box.grid(row=5, column=1, pady=5)

state_box = Entry(root)
state_box.grid(row=6, column=1, pady=5)

zipcode_box = Entry(root)
zipcode_box.grid(row=7, column=1, pady=5)

country_box = Entry(root)
country_box.grid(row=8, column=1, pady=5)

phone_box = Entry(root)
phone_box.grid(row=9, column=1, pady=5)

email_box = Entry(root)
email_box.grid(row=10, column=1, pady=5)

username_box = Entry(root)
username_box.grid(row=11, column=1, pady=5)

payment_method_box = Entry(root)
payment_method_box.grid(row=12, column=1, pady=5)

discount_code_box = Entry(root)
discount_code_box.grid(row=13, column=1, pady=5)

price_paid_box = Entry(root)
price_paid_box.grid(row=14, column=1, pady=5)





root.mainloop()