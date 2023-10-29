from tkinter import *

root = Tk()

e = Entry(root, width=50, border=5)
e.pack()
e.insert(1, "Enter Your Name:") #the text will be printed inside the text box

def myName():
    hello = "Hello " +e.get()
    Label(root, text = hello).pack()

# e.get() can allow us to use entered values but will be str data type

myButton = Button(root, text="Enter Your Name", command=myName) 
myButton.pack()

root.mainloop()