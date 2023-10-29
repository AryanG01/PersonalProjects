from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root=Tk()
root.title("Message Box")
root.iconbitmap("Pictures\PYTHON.ico")

#showinfo (ok), showerror (ok), showwarning (ok), askquestion (yes/no), askokcancel (1/0), askyesno (1/0)
#takes in 2 parameters, title of message box and text inside

def popup():
    response = messagebox.showinfo("This is my POPUP!!!", "Hello World!")
    Label(root, text=response).pack() 
    #if response == 1:
       #Label(root, text="Yes").pack()
    #else:
        #Label(root, text="No").pack()

Button(root, text="Click Me", command=popup).pack()




root.mainloop()