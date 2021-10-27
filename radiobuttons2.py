from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

# creates the window, color, size, and name
pab = Tk()
pab.title('Frames')
# pab.geometry('400x400')
# pab["bg"] = "#002aff"


# a = IntVar()
# set the a var before a button is pressed
# a.set('2')
# if value was a str then the bwloe line would be used
# r = StrVar()

def clicked(value):
    mylabel = Label(pab,text=value).pack()



# creating a radio button

MODES = [
    ("Animal","Cat"),
    ("Car","Camaro"),
    ("Fastfood","Mc Donalds"),
    ("Candy","Laffy Taffy")
]

things = StringVar()
things.set('Nothing')

for text, mode in MODES:
    Radiobutton(pab,text=text,variable=things,value=mode).pack(anchor=W)

#Radiobutton(pab, text='Option 1', variable=a, value=1,command=lambda: clicked(a.get())).pack()
#Radiobutton(pab, text='Option 2', variable=a, value=2,command=lambda: clicked(a.get())).pack()
#Radiobutton(pab, text='Option 3', variable=a, value=3).pack()
#Radiobutton(pab, text='Option 4', variable=a, value=4).pack()

mylabel = Label(pab,text=things.get())
mylabel.pack()


mybutton = Button(pab,text='click me',command=lambda: clicked(things.get()))
mybutton.pack()

pab.mainloop()