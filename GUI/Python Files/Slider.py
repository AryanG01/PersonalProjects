from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Slider")
root.iconbitmap("Pictures\PYTHON.ico")
root.geometry("400x400") # - x | (Breadth x Height)

vertical = Scale(root, from_=0,to=400)
vertical.pack()
my_label = Label(root, text = vertical.get()).pack()

horizontal = Scale(root, from_=0,to=400, orient=HORIZONTAL)
horizontal.pack()
my_label = Label(root, text = horizontal.get()).pack()

def slide():
    Label(root, text = str(horizontal.get()) + "x" + str(vertical.get())).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

my_Btn = Button(root, text = "Click Me", command=slide).pack()

root.mainloop()