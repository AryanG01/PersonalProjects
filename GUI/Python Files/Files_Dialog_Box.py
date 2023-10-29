from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root=Tk()
root.title("File Dialog Box")

def open():
    global imagex
    root.filename = filedialog.askopenfilename(initialdir="Pictures", title="Select a File", filetypes=(("Image Files", "*.png"),("All Files","*.*")))
    Label(root, text=root.filename).pack()
    imagex=ImageTk.PhotoImage(Image.open(root.filename))
    Label(image=imagex).pack()

Button(root, text="Open New File", command=open).pack()

root.mainloop()