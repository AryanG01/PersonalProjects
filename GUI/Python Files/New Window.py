from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Original window")
root.iconbitmap("Pictures\PYTHON.ico")

def open():
    global my_img
    top = Toplevel()
    top.title("New window")
    top.iconbitmap("Pictures\Image0.ico")
    my_img=ImageTk.PhotoImage(Image.open("Pictures\Python.png"))
    Label(top, image=my_img).pack()
    Button(top, text="Close New Window", command=top.destroy).pack()
    
Button(root, text="Open New Window", command=open).grid(row=0, column=0)
Button(root, text="Close Original Window", command=root.quit).grid(row=2, column=0)

#lbl = Label(top, text="Hello World")
#lbl.pack()

root.mainloop()