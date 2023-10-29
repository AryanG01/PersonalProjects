from tkinter import *
from PIL import ImageTk,Image

root =Tk()
root.title("Dropdown Menu")
root.iconbitmap("Pictures\PYTHON.ico")
root.geometry("400x400")

def Show():
    my_Label = Label(root, text=clicked.get())
    my_Label.pack()

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options).pack() # the * helps to break open the list instead of treating all as 1 object

Button(root, text="Show Selection", command=Show).pack()

root.mainloop()