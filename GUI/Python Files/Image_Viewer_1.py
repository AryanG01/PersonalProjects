from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Image_Viewer_1")
root.iconbitmap("Pictures\Image0.ico")

my_img_1=ImageTk.PhotoImage(Image.open("Image_Viewer_Contents\Image1.png"))
my_img_2=ImageTk.PhotoImage(Image.open("Image_Viewer_Contents\Image2.png"))
my_img_3=ImageTk.PhotoImage(Image.open("Image_Viewer_Contents\Image3.png"))
my_img_4=ImageTk.PhotoImage(Image.open("Image_Viewer_Contents\Image4.png"))
my_img_5=ImageTk.PhotoImage(Image.open("Image_Viewer_Contents\Image5.png"))

my_Label=Label(root, image=my_img_1)
my_Label.grid(row=0, column=0, columnspan=3)

my_img_list=[my_img_1, my_img_2, my_img_3, my_img_4, my_img_5]

def Forward(img_num):
    global my_Label
    global Button_Backward
    global Button_Forward
    
    my_Label.grid_forget()
    my_Label=Label(root, image=my_img_list[img_num-1])
    Button_Forward=Button(root, text=">>", command=lambda: Forward(img_num+1))
    Button_Backward=Button(root, text="<<", command=lambda: Backward(img_num-1))
    
    if img_num == len(my_img_list):
        Button_Forward=Button(root, text=">>", state=DISABLED)
    
    my_Label.grid(row=0, column=0, columnspan=3)
    Button_Backward.grid(row=1, column=0)
    Button_Forward.grid(row=1, column=2)

def Backward(img_num):
    global my_Label
    global Button_Backward
    global Button_Forward
    
    my_Label.grid_forget()
    my_Label=Label(root, image=my_img_list[img_num-1])
    Button_Forward=Button(root, text=">>", command=lambda: Forward(img_num+1))
    Button_Backward=Button(root, text="<<", command=lambda: Backward(img_num-1))
    
    if img_num == 1:
        Button_Backward=Button(root, text="<<", state=DISABLED)
    
    my_Label.grid(row=0, column=0, columnspan=3)
    Button_Backward.grid(row=1, column=0)
    Button_Forward.grid(row=1, column=2)

Button_Backward=Button(root, text="<<", command=Backward, state=DISABLED)
Button_Exit=Button(root, text="Exit Program", command=root.quit)
Button_Forward=Button(root, text=">>", command=lambda: Forward(2))

Button_Backward.grid(row=1, column=0)
Button_Exit.grid(row=1, column=1)
Button_Forward.grid(row=1, column=2)

root.mainloop()