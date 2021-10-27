from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

paww = Tk()
paww.title("Windows")
paww.geometry("400x400")

def show():
    mylabel = Label(paww,text=var.get())
    mylabel.pack()

var = StringVar()

c = Checkbutton(paww,text="my check box",variable=var, onvalue="On",offvalue="Off")
c.deselect()
c.pack()


mybut = Button(paww,text="click me",command=show).pack()


paww.mainloop()