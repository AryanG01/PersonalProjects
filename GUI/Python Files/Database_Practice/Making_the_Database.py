from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Address Directory Database")
root.iconbitmap("Pictures\Address_Book.ico")
root.geometry("400x400")

conn = sqlite3.connect("address_directory.db")

c = conn.cursor()

c.execute("""CREATE TABLE directory (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode text
        )""")

conn.commit()

conn.close()

root.mainloop()