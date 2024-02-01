from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import csv
from tkinter import ttk

root = Tk()
root.title("Hamxah")
root.geometry("500x600")

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
# Create a table
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers \
                  (first_name VARCHAR(255), \
                   last_name VARCHAR(255), \
                   address_1 VARCHAR(255), \
                   address_2 VARCHAR(255), \
                   city VARCHAR(50), \
                   state VARCHAR(50), \
                   zipcode INT(10), \
                   country VARCHAR(255), \
                   phone VARCHAR(255), \
                   email VARCHAR(255), \
                   payment_method VARCHAR(50), \
                   discount_code VARCHAR(255), \
                   price_paid DECIMAL(10, 2), \
                   user_id INT AUTO_INCREMENT PRIMARY KEY)")



# Show table
# my_cursor.execute("SELECT * FROM customers")
# # print(my_cursor.description)

# for thing in my_cursor.description:
#     print(thing)

# Clear text fields
def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address_1_box.delete(0, END)
    address_2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)

# Write to CSV Excel function
def write_to_csv(result):
    with open('customers.csv', 'a') as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(result)

# Seearch Customers
def search_customer():
    search_customers = Tk()
    search_customers.title("Search Customers")
    search_customers.geometry("1400x800")

    def update():
        return

    def edit_now(id, index):
        sql2 = "SELECT * FROM customers WHERE user_id = %s"
        name2 = (id, )
        result2 = my_cursor.execute(sql2, name2)
        result2 = my_cursor.fetchall()
        print(result2)

        index +=1
        # Create main form to enter customer data
        first_name_label = Label(search_customers, text="First Name").grid(row=index+1, column=0, sticky=W, padx=10, pady=10)
        last_name_label = Label(search_customers, text="Last Name").grid(row=index+2, column=0, sticky=W, padx=10)
        address_1_label = Label(search_customers, text="Address 1").grid(row=index+3, column=0, sticky=W, padx=10)
        address_2_label = Label(search_customers, text="Address 2").grid(row=index+4, column=0, sticky=W, padx=10)
        city_label = Label(search_customers, text="City").grid(row=index+5, column=0, sticky=W, padx=10)
        state_label = Label(search_customers, text="State").grid(row=index+6, column=0, sticky=W, padx=10)
        zipcode_label = Label(search_customers, text="Zipcode").grid(row=index+7, column=0, sticky=W, padx=10)
        country_label = Label(search_customers, text="Country").grid(row=index+8, column=0, sticky=W, padx=10)
        phone_label = Label(search_customers, text="Phone").grid(row=index+9, column=0, sticky=W, padx=10)
        email_label = Label(search_customers, text="Email").grid(row=index+10, column=0, sticky=W, padx=10)
        payment_method_label = Label(search_customers, text="Payment Method").grid(row=index+11, column=0, sticky=W, padx=10)
        discount_code_label = Label(search_customers, text="Discount Code").grid(row=index+12, column=0, sticky=W, padx=10)
        price_paid_label = Label(search_customers, text="Price Paid").grid(row=index+13, column=0, sticky=W, padx=10)
        id_label = Label(search_customers, text="User ID").grid(row=index+14, column=0, sticky=W, padx=10)

        # Create entry boxes
        global first_name_box2
        first_name_box2 = Entry(search_customers)
        first_name_box2.grid(row=index+1, column=1, pady=10)
        
        global last_name_box2
        last_name_box2 = Entry(search_customers)
        last_name_box2.grid(row=index+2, column=1, pady=5)

        global address_1_box2
        address_1_box2 = Entry(search_customers)
        address_1_box2.grid(row=index+3, column=1, pady=5)

        global address_2_box2
        address_2_box2 = Entry(search_customers)
        address_2_box2.grid(row=index+4, column=1, pady=5)

        global city_box2
        city_box2 = Entry(search_customers)
        city_box2.grid(row=index+5, column=1, pady=5)

        global state_box2
        state_box2 = Entry(search_customers)
        state_box2.grid(row=index+6, column=1, pady=5)

        global zipcode_box2
        zipcode_box2 = Entry(search_customers)
        zipcode_box2.grid(row=index+7, column=1, pady=5)

        global country_box2
        country_box2 = Entry(search_customers)
        country_box2.grid(row=index+8, column=1, pady=5)

        global phone_box2
        phone_box2 = Entry(search_customers)
        phone_box2.grid(row=index+9, column=1, pady=5)

        global email_box2
        email_box2 = Entry(search_customers)
        email_box2.grid(row=index+10, column=1, pady=5)

        global payment_method_box2
        payment_method_box2 = Entry(search_customers)
        payment_method_box2.grid(row=index+11, column=1, pady=5)

        global discount_code_box2
        discount_code_box2 = Entry(search_customers)
        discount_code_box2.grid(row=index+12, column=1, pady=5)

        global price_paid_box2
        price_paid_box2 = Entry(search_customers)
        price_paid_box2.grid(row=index+13, column=1, pady=5)
        
        global id_box2
        id_box2 = Entry(search_customers)
        id_box2.grid(row=index+14, column=1, pady=5)

        save_record = Button(search_customers, text="Update Record", command=update)
        save_record.grid(row=15, column=0, padx=10)

    def search_now():
        selected = drop.get()
        sql = ""
        if selected == "Search by...":
            test = Label(search_customers, text="Hey! You forgot to pick a drop down selection")
            test.grid(row=2, column=0)

        if selected == "Last Name":
            sql = "SELECT * FROM customers WHERE last_name = %s"
                      
        if selected == "Email Address":
            sql = "SELECT * FROM customers WHERE email = %s"

        if selected == "Customer ID":
            sql = "SELECT * FROM customers WHERE user_id = %s"
          

       
        searched = Search_box.get()
        # sql = "SELECT * FROM customers WHERE last_name = %s"
        name = (searched, )
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall()

        if not result:
            result = "Record Not Found..."
            search_label = Label(search_customers, text=result)
            search_label.grid(row=2, column=0)
            num +=1
        
        else:
            for index, x in enumerate(result):
                num = 0
                index += 2
                id_reference = str(x[4])
                edit_button = Button(search_customers, text="Edit", command=lambda: edit_now(id_reference, index))
                edit_button.grid(row=index, column=num)
                for y in x:
                    search_label = Label(search_customers, text=y)
                    search_label.grid(row=index, column=num+1)
                    num +=1

            csv_button = Button(search_customers, text="Save To Excel", command=lambda: write_to_csv(result))
            csv_button.grid(row=index+1, column=0)


        # search_label = Label(search_customers, text=result)
        # search_label.grid(row=3, column=0, padx=10, columnspan=2)
       
    
    # Entry box to search for customer
    Search_box = Entry(search_customers)
    Search_box.grid(row=0, column=1, padx=10, pady=10)
    # Entry box label to search for customer
    search_box_label = Label(search_customers, text="Search: ")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)
    # Entry box button to search for customer
    search_button = Button(search_customers, text="Search Customers", command=search_now)
    search_button.grid(row=1, column=0, padx=10)
    # Drop Down Box
    drop = ttk.Combobox(search_customers, values=["Search by...", "Last Name", "Email Address", "Customer ID"])
    drop.current(0)
    drop.grid(row=0, column=2)


# List Customers
def list_customer():
    list_customer_querry = Tk()
    list_customer_querry.title("List Of All Customers")
    list_customer_querry.geometry("800x600")
    # Querry The Database
    my_cursor.execute("SELECT * FROM customers")
    result = my_cursor.fetchall()
    for index, x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(list_customer_querry, text=y)
            lookup_label.grid(row=index, column=num)
            num +=1
    csv_button = Button(list_customer_querry, text="Save To Excel", command=lambda: write_to_csv(result))
    csv_button.grid(row=index+1, column=0)


# Submit customer to database
def add_customer():
    sql_command = "INSERT INTO customers (first_name, last_name, address_1, address_2, city, state, zipcode, country, email, payment_method, discount_code, price_paid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # Convert 'zipcode' to integer (assuming it's supposed to be an integer)
    zipcode_value = int(zipcode_box.get()) if zipcode_box.get().isdigit() else 0

    price_paid_value = float(price_paid_box.get()) if price_paid_box.get().replace('.', '', 1).isdigit() else 0.0


# Create the 'values' tuple
    values = (
    first_name_box.get(),
    last_name_box.get(),
    address_1_box.get(),
    address_2_box.get(),
    city_box.get(),
    state_box.get(),
    zipcode_value,  # Use the converted 'zipcode' value
    country_box.get(),
    email_box.get(),
    payment_method_box.get(),
    discount_code_box.get(),
    price_paid_box.get()
)

    my_cursor.execute(sql_command, values)

    # Commit the changes to the database
    mydb.commit()
    # Clear the fields
    clear_fields()




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
payment_method_label = Label(root, text="Payment Method").grid(row=11, column=0, sticky=W, padx=10)
discount_code_label = Label(root, text="Discount Code").grid(row=12, column=0, sticky=W, padx=10)
price_paid_label = Label(root, text="Price Paid").grid(row=13, column=0, sticky=W, padx=10)

# Create entry boxes 
first_name_box = Entry(root)
first_name_box.grid(row=1, column=1, pady=5)

last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=5)

address_1_box = Entry(root)
address_1_box.grid(row=3, column=1, pady=5)

address_2_box = Entry(root)
address_2_box.grid(row=4, column=1, pady=5)

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

payment_method_box = Entry(root)
payment_method_box.grid(row=11, column=1, pady=5)

discount_code_box = Entry(root)
discount_code_box.grid(row=12, column=1, pady=5)

price_paid_box = Entry(root)
price_paid_box.grid(row=13, column=1, pady=5)

# Create Buttons
add_customer_button = Button(root, text="Add Customer To Database", command=add_customer)
add_customer_button.grid(row=14, column=0, padx=10, pady=10)
clear_fields_buttons = Button(root, text="Clear Fields", command=clear_fields)
clear_fields_buttons.grid(row=14, column=1)

# List customers buttons
list_customer_button = Button(root, text="List Customer", command=list_customer)
list_customer_button.grid(row=15, column=0, sticky=W, padx=10)
# Search customers
search_customers_button = Button(root, text="Search/Edit Customers", command=search_customer)
search_customers_button.grid(row=15, column=1, sticky=W, padx=10)


root.mainloop()