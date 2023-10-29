from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Frames")
root.iconbitmap("Pictures\PYTHON.ico")

r=IntVar()
r.set("1")

def clicked(value):
    myLabel=Label(root, text=value)
    myLabel.pack()
    

Radiobutton(root, text="Option 1", variable=r, value=1).pack()
Radiobutton(root, text="Option 2", variable=r, value=2).pack()


myLabel=Label(root, text=r.get())
myLabel.pack()

myButton = Button(root, text="Click Me", command=lambda: clicked(r.get()))
myButton.pack()

root.mainloop()