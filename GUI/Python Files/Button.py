from tkinter import *

root = Tk()

#myButton = Button(root, text="Click Me!") #generates a button you can click but doesn't do anything as you haven't placed any info into it yet
#myButton = Button(root, text="Click Me!", state=DISABLED) #Disables the button, cant click it

def myClick():
    myLabel = Label(root, text="Ayush is an Idiot!!", padx=50, pady=50) #padx, pady control the size
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg="black", bg="red") #fg = foreground colour, colour of words on button ; bg = background colour, colour of button 
#myButton = Button(root, text="Click Me!", command=myClick()) #If you put myClick() the function wont run accordingly

myButton.pack()

root.mainloop()