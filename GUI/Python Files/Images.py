from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Python Programming")
root.iconbitmap("Pictures\PYTHON.ico")

my_img = ImageTk.PhotoImage(Image.open("Pictures\Python.png"))
my_label = Label(image=my_img)
my_label.pack()

button_exit = Button(root, text="Exit", command=root.quit)
button_exit.pack()


root.mainloop()