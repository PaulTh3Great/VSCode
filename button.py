from tkinter import *
root = Tk()
# Creating a Label Widget
myLabel1 = Label(root, text="Paul's World").grid(row=0, column=0)
myLabel2 = Label(root, text="A button will be placed here")
myLabel3 = Label(root, text="A button will be placed here")

# Shoving it onto the screen
# both lines can be combined on the same line like functions added .()
# myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)
#def myClick():
    #myLabel = Label(root,text='Clicked a button!')
    #myLabel.pack()
# button trying
# myButton = Button(root, text="Click Me", padx=100, pady=100) (this creates a button and the size)
# fg = color of the words on button | bg = color of clickable button
#myButton = Button(root, text="Click Me", command=myClick, fg='blue', bg='black').pack()


root.mainloop()