from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

# creates the window, color, size, and name
pab = Tk()
pab.title('Frames')
pab.geometry('400x400')
pab["bg"] = "#002aff"

# crates a frma ewith a size
frame = LabelFrame(pab, text="This is a Frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

#crates a button then gets placed inside the frame
b = Button(frame, text="Don't click here", command=pab.quit)
b.pack()
b1 = Button(frame,text=" Click Me", command=pab.quit)
b1.pack()
# crates an instance of the stringvar
my_str_var = StringVar()
my_str_var.set("MONDAY")

# crates the object combo box and links it with the instance and addes the values of the scroll down
my_combobox = ttk.Combobox(pab, textvariable= my_str_var, values=["MONDAY","TUESDAY","WENSDAY","THURSDAY","FRIDAY","SATURDAY",
"SUNDAY"])
my_combobox.pack()


clicked = IntVar()
clicked.set("one")

drop = OptionMenu(pab, clicked, "one","two","three")
drop.pack()
# radio buttons


pab.mainloop()