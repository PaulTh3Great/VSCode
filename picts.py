from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Nice Pictures')
# will place a icon on the window using the file location
root.iconbitmap('/Users/paulavalos/Desktop/python/vscode/FAT_CAT.ico')

# needs to have the whole file 
# this assings the picture and location to an object name
# my_img = ImageTk.PhotoImage(Image.open('/Users/paulavalos/Desktop/python/vscode/funnycat.jpeg'))
my_img = ImageTk.PhotoImage(Image.open('/Users/paulavalos/Desktop/python/vscode/cat.png'))
my_img1 = ImageTk.PhotoImage(Image.open('/Users/paulavalos/Desktop/python/vscode/funnypic2.jpeg'))
my_img2 = ImageTk.PhotoImage(Image.open('/Users/paulavalos/Desktop/python/vscode/funnypic1.jpeg'))
my_img3 = ImageTk.PhotoImage(Image.open('/Users/paulavalos/Desktop/python/vscode/funnypic5.jpeg'))
my_img4 = ImageTk.PhotoImage(Image.open('/Users/paulavalos/Desktop/python/vscode/funnypic3.jpeg'))

# place all pic objects into a list to be read
image_list = [my_img, my_img1, my_img2, my_img3, my_img4]

current_img_index = 0
my_label = Label(image=image_list[current_img_index])
my_label.grid(row=0, column=0, columnspan=3)

# this will crate a label but it won't change with the new pics becuase it isnt updating
status_bar = Label(root,text='Image' + str((current_img_index)+1) + ' of ' + str(len(image_list)))
status_bar.grid(row=2, column=2)



def forward():
    global my_label
    global button_forward
    global button_back
    global current_img_index
    global status_bar
    my_label.grid_forget()
    if len(image_list)-1 == current_img_index:
        current_img_index = 0
    else:
        current_img_index += 1

    my_label = Label(image=image_list[current_img_index])
    # not showing another image
    # button_forward = Label(Button(root, text='Next Picture', command=lambda: forward(image_number+1)))
    # button_back = Label(Button(root, text='Previous Picture', command=lambda: back(image_number-1)))

    my_label.grid(row=0, column=0, columnspan=3)
    # button_back.grid(row=1, column=0)
    # button_forward.grid(row=1, column=2)
    status_bar.grid_forget()
    status_bar = Label(root,text='Image ' + str((current_img_index)+1) + ' of ' + str(len(image_list)))
    status_bar.grid(row=2, column=2)


def back():
    global my_label
    global button_forward
    global button_back
    global current_img_index
    global status_bar
    my_label.grid_forget()
    if current_img_index == 0:
        current_img_index = len(image_list)-1
    else:
        current_img_index -=1

    my_label = Label(image=image_list[current_img_index])
    my_label.grid(row=0, column=0, columnspan=3)

    status_bar.grid_forget()
    status_bar = Label(root,text='Image ' + str((current_img_index)+1) + ' of ' + str(len(image_list)))
    status_bar.grid(row=2, column=2)


# button with the command to exit out of the window and forward and back
button_back = Button(root, text='Previous Picture',command=back)
button_forward = Button(root, text='Next Picture', command=lambda: forward())
button_quit = Button(root, text='Press this to quit', command=root.quit)

# test button for disable state
test_button = Button(root, text='Test Button',state=DISABLED)
test_button.grid(row=2, column=1)


# placing the buttons on position.
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)



root.mainloop()