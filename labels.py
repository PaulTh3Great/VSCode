from tkinter import *
root = Tk()

e = Entry(root, width=50, borderwidth=5).pack()


def myClick():
    myLabel = Label(root,text=e.__getattribute__())
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", command=myClick, fg='blue', bg='black').pack()


root.mainloop()