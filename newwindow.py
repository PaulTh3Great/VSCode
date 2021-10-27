from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox


paww = Tk()
paww.title("Windows")


def open():
    global myimg
    # will create another window and assign it to top
    top = Toplevel()
    top.title("new window sucka")
    # grabs tghe image and crates the object myimg from the directory
    myimg = ImageTk.PhotoImage(Image.open("/Users/paulavalos/Desktop/python/vscode/funnypic5.jpeg"))
    # places the image into a label and crates the mylabel object
    mylabel = Label(top,image=myimg).pack()

# quit exits entire windows / destroy quits the windows until mainloop i think
    mybutton2 = Button(top, text="close window", command=top.destroy).pack()

# creates the button that will have the open command 
mybutton = Button(paww,text="Open Window",command=open).pack()




paww.mainloop()