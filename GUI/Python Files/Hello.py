from tkinter import *
name = input("Whats your name? \n")

root = Tk() #First Thing we must type out, it creates the window pop up

#Creating a Label Widget
myLabel = Label(root, text="Hello " + name + "!")
#Shoving it onto the screen
myLabel.pack()

root.mainloop()