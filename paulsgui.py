from tkinter import *
# root is the location saved for the Tk functions
root = Tk()
root.title('Pauls First GUI')
root.geometry('500x500')
root['bg']= '#ff0062'
# crate the entry box with root and give it a width
e = Entry(root, width=50)
#.pack() places the item inside the box
e.pack()
# create a message inside the entry box
e.insert(0,'Put number in here')
# e.delete(0,END)
def myClick():
    hello = "TY user Paul will text you @" + e.get() + '. Have a great day'
    myLabel = Label(root,text=hello,bg='#ff0062')
    myLabel.pack()

myButton = Button(root, text="Please enter your number", command=myClick, fg='blue', bg='black').pack()


root.mainloop()