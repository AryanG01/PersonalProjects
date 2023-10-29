from tkinter import *
from PIL import ImageTk,Image
import sqlite3 #Structured Query Language

root =Tk()
root.title("Databases")
root.iconbitmap("Pictures\PYTHON.ico")
root.geometry("400x400")

#Database

#Create a databse or connect to it
conn = sqlite3.connect("address_book.db")

#Create Cursor
c = conn.cursor()

#Create Submit function
def submit():
    #Create a databse or connect to it
    conn = sqlite3.connect("address_book.db")

    #Create Cursor
    c = conn.cursor()
    
    #Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                "f_name": f_name.get(),         
                "l_name": l_name.get(),
                "address": address.get(),
                "city": city.get(),
                "state": state.get(),
                "zipcode": zipcode.get()
            })
    
    #Commit Changes
    conn.commit()

    #Close connection
    conn.close()
    
    #Clear the boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#Create query function
def query():
    #Create a databse or connect to it
    conn = sqlite3.connect("address_book.db")

    #Create Cursor
    c = conn.cursor()
    
    #Query the database - fetchone, fetchmany, fetchall
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)
    
    #Loop through results
    print_records=""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[6]) +" \n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    
    #Commit Changes
    conn.commit()

    #Close connection
    conn.close()

#Create Text Box
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

#Create Text Box Label
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

#Create Submit Button
submit_button = Button(root, text="Add Record To Databse", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

#Create Query Button
query_button = Button(root, text="Show Database", command=query)
query_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

#Commit Changes
conn.commit()

#Close connection
conn.close()

root.mainloop()