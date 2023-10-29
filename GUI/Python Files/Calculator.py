from tkinter import *

root = Tk()
root.title("Ayush is an idiot")

e = Entry(root, width = 40, borderwidth = 10)
e.grid(row = 0, column = 0, columnspan = 4, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END) #delete whatever was in textbox
    e.insert(0, current + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num 
    global math
    math = 'addition'
    f_num = float(first_number)
    e.delete(0, END)

def button_minus():
    first_number = e.get()
    global f_num 
    global math
    math = 'minus'
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num 
    global math
    math = 'multiply'
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num 
    global math
    math = 'divide'
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    s_num = float(e.get())
    e.delete(0, END)
    if math == "addition":
        e.insert(0, str(f_num + s_num))
    if math == "minus":
        e.insert(0, str(f_num - s_num))
    if math == "multiply":
        e.insert(0, str(f_num * s_num))
    if math == "divide":
        e.insert(0, str(f_num / s_num))

Button_1 = Button(root, text ="1", padx=40, pady=20, command=lambda: button_click(1))
Button_2 = Button(root, text ="2", padx=40, pady=20, command=lambda: button_click(2))
Button_3 = Button(root, text ="3", padx=40, pady=20, command=lambda: button_click(3))
Button_4 = Button(root, text ="4", padx=40, pady=20, command=lambda: button_click(4))
Button_5 = Button(root, text ="5", padx=40, pady=20, command=lambda: button_click(5))
Button_6 = Button(root, text ="6", padx=40, pady=20, command=lambda: button_click(6))
Button_7 = Button(root, text ="7", padx=40, pady=20, command=lambda: button_click(7))
Button_8 = Button(root, text ="8", padx=40, pady=20, command=lambda: button_click(8))
Button_9 = Button(root, text ="9", padx=40, pady=20, command=lambda: button_click(9))
Button_0 = Button(root, text ="0", padx=40, pady=20, command=lambda: button_click(0))
Button_add = Button(root, text ="+", padx=39, pady=20, command=button_add)
Button_minus = Button(root, text ="-", padx=40, pady=20, command=button_minus)
Button_mutiply = Button(root, text ="*", padx=41, pady=20, command=button_multiply)
Button_divide = Button(root, text ="/", padx=40, pady=20, command=button_divide)
Button_equal = Button(root, text ="=", padx=89, pady=20, command=button_equal)
Button_clear = Button(root, text ="Clear", padx=79, pady= 20, command=button_clear)


Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)

Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)

Button_0.grid(row=4, column=0)
Button_add.grid(row=5, column=0)
Button_equal.grid(row=5, column=1, columnspan=2)
Button_clear.grid(row=4, column=1, columnspan=2)

Button_minus.grid(row=6, column=0)
Button_mutiply.grid(row=6, column=1)
Button_divide.grid(row=6, column=2)

root.mainloop()