from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Frames")
root.iconbitmap("Pictures\PYTHON.ico")

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza=StringVar()
pizza.set("Pepperoni")

for text,topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)
    
myButton = Button(root, text="Click Me", command=lambda: clicked(pizza.get()))
myButton.pack()

def clicked(value):
    myLabel=Label(root, text=value)
    myLabel.pack()

#myLabel=Label(root, text=pizza.get())
#myLabel.pack()

root.mainloop()