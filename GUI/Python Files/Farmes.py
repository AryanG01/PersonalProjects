from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Frames")
root.iconbitmap("Pictures\PYTHON.ico")

frame = LabelFrame(root, text='This is a Frame', padx=10, pady=10)
frame.pack(padx=20, pady=20)

b = Button(frame, text="Exit Program", command=root.quit)
b.pack()

root.mainloop()