from tkinter import *

calculator = Tk()
calculator.title('Pawws Calculator')

e = Entry(calculator,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    # this line will delete what is currently in the box
    # insert will place the number in which is clikced inside the text box at index 0
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)

# create buttons
button_1 = Button(calculator,text='1',padx=40,pady=20,command=lambda : button_click('1'))
button_2 = Button(calculator,text='2',padx=40,pady=20,command=lambda : button_click('2'))
button_3 = Button(calculator,text='3',padx=40,pady=20,command=lambda : button_click('3'))
button_4 = Button(calculator,text='4',padx=40,pady=20,command=lambda : button_click('4'))
button_5 = Button(calculator,text='5',padx=40,pady=20,command=lambda : button_click('5'))
button_6 = Button(calculator,text='6',padx=40,pady=20,command=lambda : button_click('6'))
button_7 = Button(calculator,text='7',padx=40,pady=20,command=lambda : button_click('7'))
button_8 = Button(calculator,text='8',padx=40,pady=20,command=lambda : button_click('8'))
button_9 = Button(calculator,text='9',padx=40,pady=20,command=lambda : button_click('9'))
button_0 = Button(calculator,text='0',padx=40,pady=20,command=lambda : button_click('0'))
button_add = Button(calculator,text='+',padx=40,pady=20,command=lambda : button_click(1))
button_equal = Button(calculator,text='=',padx=91,pady=20,command=lambda : button_click(1))
button_clear1 = Button(calculator,text='Clear',padx=91,pady=20,command=lambda : button_clear())


# place buttons on the screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=5,column=0)
button_clear1.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)







calculator.mainloop()