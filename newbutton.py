from tkinter import *
# sets up window and names the title of window along with background color and pop up size
# use googler serach #ff0000 to search color codes
popup = Tk()
popup.title('PaulTh3Great')
popup.geometry('600x600')
popup['bg'] = '#00ffd0'

# making to action of the button click to be linked to key word command
def printValue():
    pname = player_name.get()
    Label(popup, text=f'Thank you {pname}, you will receive a text when your survey is in your email!', pady=20, bg='#00ffd0').pack()

player_name = Entry(popup)
player_name.pack(pady=30)

Button(
    popup,
    text='Register Player',
    padx=10,
    pady=5,
    command=printValue
).pack()

popup.mainloop()