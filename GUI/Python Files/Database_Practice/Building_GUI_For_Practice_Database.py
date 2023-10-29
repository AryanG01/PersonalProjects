from tkinter import *
from turtle import update
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Address Directory")
root.iconbitmap("Pictures\Address_Book.ico")
root.geometry("280x400")

conn = sqlite3.connect("address_directory.db")

c = conn.cursor()

##########################################################################################################

def update():
    #Create a databse or connect to it
    conn = sqlite3.connect("address_directory.db")

    #Create Cursor
    c = conn.cursor()    

    record_id = select_ID.get()
    c.execute("""UPDATE directory SET
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
        'zipcode' : zipcode_edit.get(),
        'oid' : record_id
        })

    #Commit Changes
    conn.commit()

    #Close connection
    conn.close()
    
    new.destroy() 
       
##########################################################################################################

def edit():
    conn = sqlite3.connect("address_directory.db")

    #Create Cursor
    conn.cursor() 
    
    f_name_edit.configure(state='normal')
    l_name_edit.configure(state='normal')
    address_edit.configure(state='normal')
    city_edit.configure(state='normal')
    state_edit.configure(state='normal')
    zipcode_edit.configure(state='normal')
    
    #Commit Changes
    conn.commit()

    #Close connection
    conn.close()
        
##########################################################################################################

def delete():
    conn = sqlite3.connect("address_directory.db")

    #Create Cursor
    c = conn.cursor() 
    #Create a databse or connect to it
    conn = sqlite3.connect("address_directory.db")

    #Create Cursor
    c = conn.cursor()
    
    #Delete a record
    c.execute("DELETE from directory WHERE oid = " + select_ID.get())
    
    #Commit Changes
    conn.commit()

    #Close connection
    conn.close()
    
    new.destroy()

##########################################################################################################

def view():
    global new
    new =Tk()
    new.title("View a Record")
    new.iconbitmap("Pictures\PYTHON.ico")
    
    #Create a databse or connect to it
    conn = sqlite3.connect("address_directory.db")

    #Create Cursor
    c = conn.cursor()

    record_id = select_ID.get()
    #Query the database - fetchone, fetchmany, fetchall
    c.execute("SELECT * FROM directory WHERE oid = " + record_id)
    records = c.fetchall()

    #Create Global variable for text box names
    global f_name_edit
    global l_name_edit
    global address_edit
    global city_edit
    global state_edit
    global zipcode_edit

    #Create Text Box
    f_name_edit = Entry(new, width=30)
    f_name_edit.grid(row=0, column=1, padx=20, pady=(10,0))
    l_name_edit = Entry(new, width=30)
    l_name_edit.grid(row=1, column=1, padx=20)
    address_edit = Entry(new, width=30)
    address_edit.grid(row=2, column=1, padx=20)
    city_edit = Entry(new, width=30)
    city_edit.grid(row=3, column=1, padx=20)
    state_edit = Entry(new, width=30)
    state_edit.grid(row=4, column=1, padx=20)
    zipcode_edit = Entry(new, width=30)
    zipcode_edit.grid(row=5, column=1, padx=20)

    #Create Text Box Label
    f_name_label_edit = Label(new, text="First Name")
    f_name_label_edit.grid(row=0, column=0, pady=(10,0))
    l_name_label_edit = Label(new, text="Last Name")
    l_name_label_edit.grid(row=1, column=0)
    address_label_edit = Label(new, text="Address")
    address_label_edit.grid(row=2, column=0)
    city_label_edit = Label(new, text="City")
    city_label_edit.grid(row=3, column=0)
    state_label_edit = Label(new, text="State")
    state_label_edit.grid(row=4, column=0)
    zipcode_label_edit = Label(new, text="Zipcode")
    zipcode_label_edit.grid(row=5, column=0)
    
    #Lopp through results
    for record in records:
        f_name_edit.insert(0, record[0])
        f_name_edit.configure(state='readonly')
        l_name_edit.insert(0, record[1])
        l_name_edit.configure(state='readonly')
        address_edit.insert(0, record[2])
        address_edit.configure(state='readonly')
        city_edit.insert(0, record[3])
        city_edit.configure(state='readonly')
        state_edit.insert(0, record[4])
        state_edit.configure(state='readonly')
        zipcode_edit.insert(0, record[5])
        zipcode_edit.configure(state='readonly')
    
    #Create View Button
    delete_btn = Button(new, text="Delete Record", command=delete)
    delete_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=84)
    
    #Create edit Button
    edit_btn = Button(new, text="Edit Record", command=edit)
    edit_btn.grid(row=7, column=0, pady=10, padx=10, ipadx=84)

    #Create Update Button
    update_btn = Button(new, text="Update Record", command=update)
    update_btn.grid(row=7, column=1, pady=10, padx=10, ipadx=84)
    
    new.mainloop()

##########################################################################################################

def submit():
    conn = sqlite3.connect("address_directory.db")

    c = conn.cursor()
    
    c.execute("INSERT INTO directory VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
            "f_name": f_name.get(),
            "l_name": l_name.get(),
            "address": address.get(),
            "city": city.get(),
            "state": state.get(),
            "zipcode": zipcode.get()
            })
    
    conn.commit()

    conn.close()
    
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    
##########################################################################################################

def show():
    conn = sqlite3.connect("address_directory.db")

    c = conn.cursor()
    
    c.execute("SELECT *, oid FROM directory")
    records=c.fetchall()
    print(records)
    
    print_records=""
    for record in records:
        print_records += record[0] + " " + record[1] + "\t" + str(record[6]) + "\n"
        
    show_label = Label(root, text=print_records)
    show_label.grid(row=10, column=0, columnspan=2, padx=20, pady=20)
    
    conn.commit()

    conn.close()

##########################################################################################################    

#Creating text box labels
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
select_ID_label = Label(root, text="Select ID")
select_ID_label.grid(row=8, column=0)

#Creating text box 
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
select_ID = Entry(root, width=30)
select_ID.grid(row=8, column=1, padx=20)

##########################################################################################################


#Creating Submit Button
submit_btn = Button(root, text="Add Record to Directory", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=57)

#Create Show Button
show_btn = Button(root, text="Show Records", command=show)
show_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=84)

#Create View Button
view_btn = Button(root, text="View Records", command=view)
view_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=84)

conn.commit()

conn.close()

root.mainloop()