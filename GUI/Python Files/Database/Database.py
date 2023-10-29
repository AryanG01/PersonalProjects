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

#Create Table - text, integer, real(decimal), null, blob(e.g. Image, Video files)
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")

#Commit Changes
conn.commit()

#Close connection
conn.close()

root.mainloop()