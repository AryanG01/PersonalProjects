from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name is Aryan")


#myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
#myLabel2 = Label(root, text="My Name is Aryan").grid(row=1, column=0)
#Can follow whats mentioned here but not as clean as a two step process

myLabel1.grid(row=0, column=0) # row column column
myLabel2.grid(row=1, column=1) # row

root.mainloop()