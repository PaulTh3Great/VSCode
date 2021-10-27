from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

# creates the window, color, size, and name
pab = Tk()
pab.title('Frames')
pab.geometry('400x400')
# comment out until we decide if we want a back ground color
# pab["bg"] = "#002aff"

# creating forgot password new window
def forgotpassword():
    password_page = Tk()
    password_page.title('Adjust Password')
    password_page.geometry('400x400')

def login():
    global login_page
    login_page = Tk()
    login_page.title('Welcome Page')
    login_page.geometry('400x400')

def quit_gui():
    login_page.destroy()

title_label = Label(pab,text='Welcome to the Project')
title_label.grid(row=0,column=1)

# username and passwaord boxes
username_label = Label(pab,text='Username')
username_label.grid(row=1,column=0)

password_label = Label(pab,text='Password')
password_label.grid(row=2,column=0)

# Create entry for user input for username and password
username_entry = Entry(pab)
username_entry.grid(row=1,column=1)

password_entry = Entry(pab)
password_entry.grid(row=2,column=1)

# create buttons for forgot password and login
forgot_password_button = Button(pab,text='Forgot Password',command=forgotpassword)
forgot_password_button.grid(row=3,column=0)

login_button = Button(pab,text='Login',command=login)
login_button.grid(row=3,column=1)

pab.mainloop()