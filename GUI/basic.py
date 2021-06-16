from tkinter import *
from PIL import ImageTk, Image

root = Tk()

########################################################  Basic  ########################################################
# myLabel = Label(root, text="Hello World!")

# myLabel.pack()

########################################################  Grid  ########################################################
# myLabel1 = Label(root, text="Hello World!")
# myLabel2 = Label(root, text="My Name is Nipun")

# myLabel1.grid(row=0,column=0)
# myLabel2.grid(row=1,column=0)


########################################################  Button  ########################################################

# def myClick():

#     myLabel = Label(root,text='Clicked a button')
#     myLabel.pack()

# myButton = Button(root, text="Click Me",command=myClick, padx=50,pady=50, fg = "white", bg="black") #state=disabled
# myButton.pack()

########################################################  text input  ########################################################
# e = Entry(root, width=50, bg="black", fg="white")
# # e.insert(0,"Enter Your Name: ")
# e.pack()

# def myClick():

#     myLabel = Label(root,text="Hello "+ e.get())
#     myLabel.pack()

# myButton = Button(root, text="Enter your name",command=myClick, padx=10,pady=10, fg = "white", bg="black") #state=disabled
# myButton.pack()

########################################################  Exit Button  ########################################################

# button_quit = Button(root, text="Exit Program",command=root.quit)
# button_quit.pack()

# Image Load

my_img = ImageTk.PhotoImage(Image.open("f.jpg"))
my_img_label = Label(image=my_img)
my_img_label.pack()

root.mainloop()