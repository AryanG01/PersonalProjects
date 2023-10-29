from tkinter import *

r = Tk()

e = Entry(r,width=60)
e.insert(0,'Aryan')
e.configure(state='readonly')
e.grid(row=0,column=0)

r.mainloop()