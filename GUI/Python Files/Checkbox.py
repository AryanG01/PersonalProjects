from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Checkbox")
root.iconbitmap("Pictures\PYTHON.ico")
root.geometry("400x400")

#var=IntVar()
var=StringVar()
var.set("Aryan") 

c = Checkbutton(root, text="Click Here", variable=var, onvalue="Ayush", offvalue="Aryan").pack()

def show():
    if var.get() == "Aryan": #0 if var=IntVar()
        Label(root, text="You didn't Click").pack()
    else:
        Label(root, text="You Clicked").pack()

myButton = Button(root, text="Show Me", command=show).pack()

root.mainloop()