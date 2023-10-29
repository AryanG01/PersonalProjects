from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Pictures")
root.iconbitmap("Pictures\Image0.ico")

img1 = ImageTk.PhotoImage(Image.open("Image_Viewer_Contents\Image1.png"))
img2 = ImageTk.PhotoImage(Image.open("Image_Viewer_Contents\Image2.png"))
img3 = ImageTk.PhotoImage(Image.open("Image_Viewer_Contents\Image3.png"))
img4 = ImageTk.PhotoImage(Image.open("Image_Viewer_Contents\Image4.png"))
img5 = ImageTk.PhotoImage(Image.open("Image_Viewer_Contents\Image5.png"))

img_list = [img1, img2, img3, img4, img5]

picture = Label(root, image=img1)
picture.grid(row=0, column=0, columnspan=3)

Status_Bar = Label(root, text = "Image 1 of " + str(len(img_list)), relief=SUNKEN, bd=2, anchor=E)

def forward(img_num):
    global picture
    global forward_button
    global backward_button
    
    picture.grid_forget()
    
    picture = Label(root, image=img_list[img_num-1])
    backward_button = Button(root, text='<<', command=lambda: backward(img_num-1))
    forward_button = Button(root, text='>>', command=lambda: forward(img_num+1))
    
    if img_num == len(img_list):
        forward_button = Button(root, text='>>', command=forward, state=DISABLED)
        
    picture.grid(row=0, column=0, columnspan=3)
    backward_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)
    
    # Update for Status Bar
    Status_Bar = Label(root, text = "Image "+str(img_num)+" of " + str(len(img_list)), relief=SUNKEN, bd=2, anchor=E)
    Status_Bar.grid(row=2, column=0, columnspan=3, sticky=E+W)
    
def backward(img_num):
    global picture
    global forward_button
    global backward_button
    
    picture.grid_forget()
    
    picture = Label(root, image=img_list[img_num-1])
    backward_button = Button(root, text='<<', command=lambda: backward(img_num-1))
    forward_button = Button(root, text='>>', command=lambda: forward(img_num+1))
    
    if img_num == 1:
        backward_button = Button(root, text='<<', command=backward, state=DISABLED)
        
    picture.grid(row=0, column=0, columnspan=3)
    backward_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)
    
    # Update for Status Bar
    Status_Bar = Label(root, text = "Image "+str(img_num)+" of " + str(len(img_list)), relief=SUNKEN, bd=2, anchor=E)
    Status_Bar.grid(row=2, column=0, columnspan=3, sticky=E+W)

backward_button = Button(root, text='<<', command=backward, state=DISABLED)
exit_button = Button(root, text='Exit Program', command=root.quit)
forward_button = Button(root, text='>>', command=lambda: forward(2))

backward_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2, pady=10)
Status_Bar.grid(row=2, column=0, columnspan=3, sticky=E+W)

root.mainloop()