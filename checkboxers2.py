from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

paww = Tk()
paww.title("Windows")
paww.geometry("400x400")

def show():
    mylabel = Label(paww, text=var.get())
    mylabel.pack()


var = StringVar()
var.set(varlist[0])

varlist = [
    "january",
    "febuary",
    "march",
    "april"
]

op = OptionMenu(paww, var, *varlist)
op.pack()

mylab = Button(paww, text="Show Month",command=show)
mylab.pack()


paww.mainloop()