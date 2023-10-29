from tkinter import *
from turtle import update
from PIL import ImageTk,Image
import sqlite3 #Structured Query Language

root =Tk()
root.title("Address Directory")
root.iconbitmap("Pictures\Address_Book.ico")
root.geometry("400x500")

#Database

#Create a databse or connect to it
conn = sqlite3.connect("address_book.db")

#Create Cursor
c = conn.cursor()

######################################################################################################

def update():
    #Create a databse or connect to it
    conn = sqlite3.connect("address_book.db")

    #Create Cursor
    c = conn.cursor()    

    record_id = Delete_Box.get()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address, 
        city = :city,
        state = :state,
        zipcode = :zipcode
                                  
        WHERE oid = :oid""",
        {
        'first': f_name_edit.get(),
        'last' : l_name_edit.get(),
        'address' : address_edit.get(),
        'city' : city_edit.get(),
        'state' : state_edit.get(),
        'zipcode' : zipcode.get(),
        'oid' : record_id
        })

    #Commit Changes
    conn.commit()

    #Close connection
    conn.close()
    
    edit.destroy()    
    
######################################################################################################

#Create Update Function
def edit():
    global edit
    edit =Tk()
    edit.title("Update a Record")
    edit.iconbitmap("Pictures\PYTHON.ico")
    edit.geometry("280x180")
    
    #Create a databse or connect to it
    conn = sqlite3.connect("address_book.db")

    #Create Cursor
    c = conn.cursor()

    record_id = Delete_Box.get()
    #Query the database - fetchone, fetchmany, fetchall
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    #Create Global variable for text box names
    global f_name_edit
    global l_name_edit
    global address_edit
    global city_edit
    global state_edit
    global zipcode_edit

    #Create Text Box
    f_name_edit = Entry(edit, width=30)
    f_name_edit.grid(row=0, column=1, padx=20, pady=(10,0))
    l_name_edit = Entry(edit, width=30)
    l_name_edit.grid(row=1, column=1, padx=20)
    address_edit = Entry(edit, width=30)
    address_edit.grid(row=2, column=1, padx=20)
    city_edit = Entry(edit, width=30)
    city_edit.grid(row=3, column=1, padx=20)
    state_edit = Entry(edit, width=30)
    state_edit.grid(row=4, column=1, padx=20)
    zipcode_edit = Entry(edit, width=30)
    zipcode_edit.grid(row=5, column=1, padx=20)

    #Create Text Box Label
    f_name_label_edit = Label(edit, text="First Name")
    f_name_label_edit.grid(row=0, column=0, pady=(10,0))
    l_name_label_edit = Label(edit, text="Last Name")
    l_name_label_edit.grid(row=1, column=0)
    address_label_edit = Label(edit, text="Address")
    address_label_edit.grid(row=2, column=0)
    city_label_edit = Label(edit, text="City")
    city_label_edit.grid(row=3, column=0)
    state_label_edit = Label(edit, text="State")
    state_label_edit.grid(row=4, column=0)
    zipcode_label_edit = Label(edit, text="Zipcode")
    zipcode_label_edit.grid(row=5, column=0)
    
    #Lopp through results
    for record in records:
        f_name_edit.insert(0, record[0])
        l_name_edit.insert(0, record[1])
        address_edit.insert(0, record[2])
        city_edit.insert(0, record[3])
        state_edit.insert(0, record[4])
        zipcode_edit.insert(0, record[5])


    #Create Update Button
    Save_button = Button(edit, text="Save Record", command=update)
    Save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=87)

######################################################################################################
    
#Create a function to delete a record
def delete():
    #Create a databse or connect to it
    conn = sqlite3.connect("address_book.db")

    #Create Cursor
    c = conn.cursor()
    
    #Delete a record
    c.execute("DELETE from addresses WHERE oid = " + Delete_Box.get())
    
    #Commit Changes
    conn.commit()

    #Close connection
    conn.close()

######################################################################################################

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

######################################################################################################

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
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) +" \n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)
    
    #Commit Changes
    conn.commit()

    #Close connection
    conn.close()

######################################################################################################

#Create Text Box
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))

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

Delete_Box = Entry(root, width=30)
Delete_Box.grid(row=8, column=1, padx=20, pady=5)

######################################################################################################

#Create Text Box Label
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10,0))

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

Delete_Box_label = Label(root, text="Select ID")
Delete_Box_label.grid(row=8, column=0, padx=20, pady=5)

######################################################################################################

#Create Submit Button 
submit_button = Button(root, text="Add Record To Database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

#Create Query Button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

#Create Delete Button
delete_button = Button(root, text="Delete Record", command=delete)
delete_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=136)

#Create Edit Button to update record
Edit_button = Button(root, text="Update Record", command=edit)
Edit_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=136)

######################################################################################################

#Commit Changes
conn.commit()

#Close connection
conn.close()

root.mainloop()