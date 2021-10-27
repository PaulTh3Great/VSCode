from tkinter import *

paw = Tk()
paw.title("Paul's First Try")
paw.geometry('1000x500')
paw['bg'] = '#ff6a00'

def say_hi():
    

button1 = Button(paw,text='Click Me',command=lambda:say_hi())
button1.pack()

insert1 = Entry(paw)
insert1.insert(END,'Place numbers in here')
insert1.pack()



paw.mainloop()