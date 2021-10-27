from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox


paww = Tk()
paww.title("Windows")


def open():
    global myimg
    top = Toplevel()
    top.title("new window sucka")

    myimg = ImageTk.PhotoImage(Image.open("/Users/paulavalos/Desktop/python/vscode/funnypic5.jpeg"))

    mylabel = Label(top,image=myimg).pack()

    mybutton2 = Button(top, text="close window", command=top.destroy).pack()


mybutton = Button(paww,text="Open Window",command=open).pack()




paww.mainloop()