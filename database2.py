from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

paww = Tk()
paww.title("Windows")
paww.geometry("400x400")

# create button function
# include clearing of the text boxes


def hello():
    return

def bye():
    return


def submit():
    #inside of function you need to connect to data base and create a new cursor
    
    # database create or connect to a crated one
    conn = sqlite3.connect("/Users/paulavalos/Desktop/python/vscode/addressbook.db")
    # create a cursor so dump and bring information
    c = conn.cursor()

    
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :addi, :state, :city, :zip)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'addi': addi.get(),
                'state': state.get(),
                'city': city.get(),
                'zip': zip.get() 
            })
    # commit changes to database
    conn.commit()
    # close connection
    conn.close()
    # delete the info that was placed in the entry boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    addi.delete(0,END)
    state.delete(0,END)
    city.delete(0,END)
    zip.delete(0,END)

def query():
    # database create or connect to a crated one
    conn = sqlite3.connect("/Users/paulavalos/Desktop/python/vscode/addressbook.db")
    # create a cursor so dump and bring information
    c = conn.cursor() 


    # to query the database
    c.execute("SELECT *, oid FROM addresses")
    # grabs all the data inside
    records = c.fetchall()
    # go threw all data and display it
    print_records = ""
    for record in records:
        print_records += "\t" + str(record[0]) + "\t" + str(record[1]) + "\t" + str(record[6]) + "\n"

    query_label = Label(paww,text=print_records)
    query_label.grid(row=11,column=1)

    # commit changes to database
    conn.commit()
    # close connection
    conn.close()

def delete_record():
    # database create or connect to a crated one
    conn = sqlite3.connect("/Users/paulavalos/Desktop/python/vscode/addressbook.db")
    # create a cursor so dump and bring information
    c = conn.cursor()

    # delete a record
    c.execute("DELETE from addresses WHERE oid= " + delete_record_entry.get())
    delete_record_entry.delete(0,END)

    # commit changes to database
    conn.commit()
    # close connection
    conn.close()

def update():
    # database create or connect to a crated one
    conn = sqlite3.connect("/Users/paulavalos/Desktop/python/vscode/addressbook.db")
    # create a cursor so dump and bring information
    c = conn.cursor()
    
    record_id = delete_record_entry.get()

    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        state = :state,
        city = :city,
        zipcode = zipcode

        WHERE oid = :oid""",
        {
        'first': f_name2.get(),
        'last': l_name2.get(),
        'address': addi2.get(),
        'state': state2.get(),
        'city': city2.get(),
        'zipcode': zip2.get(),
        'oid': record_id
        })


    # commit changes to database
    conn.commit()
    # close connection
    conn.close()

    paww2.destroy()

def edit():
    global paww2
    paww2 = Tk()
    paww2.title("Windows")
    paww2.geometry("400x400")

    # connect to the location of the DB
    conn = sqlite3.connect("/Users/paulavalos/Desktop/python/vscode/addressbook.db")
    # create a cursor so dump and bring information
    c = conn.cursor()

    # grans the id to place all info inside information boxes 
    record_id = delete_record_entry.get()

    # to query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    # grabs all the data inside
    records = c.fetchall()

    # need to make these global so you can use in other functions
    global f_name2
    global l_name2
    global addi2
    global state2
    global city2
    global state2
    global zip2

    f_name2 = Entry(paww2)
    f_name2.grid(row=0,column=1)
    f_label2 = Label(paww2,text="First Name")
    f_label2.grid(row=0,column=0)

    l_name2 = Entry(paww2)
    l_name2.grid(row=1,column=1)
    l_label2 = Label(paww2,text="Last Name")
    l_label2.grid(row=1,column=0)

    addi2 = Entry(paww2)
    addi2.grid(row=2,column=1)
    addi2_label = Label(paww2,text="Address")
    addi2_label.grid(row=2,column=0)

    state2 = Entry(paww2)
    state2.grid(row=3,column=1)
    state_label2 = Label(paww2,text="State")
    state_label2.grid(row=3,column=0)

    city2 = Entry(paww2)
    city2.grid(row=4,column=1)
    city_label2 = Label(paww2,text="City")
    city_label2.grid(row=4,column=0)

    zip2 = Entry(paww2)
    zip2.grid(row=5,column=1)
    zip_label2 = Label(paww2,text="Zip Code")
    zip_label2.grid(row=5,column=0)

    #loop threw information and place correct info in each box
    for record in records:
        f_name2.insert(0,record[0])
        l_name2.insert(0,record[1])
        addi2.insert(0,record[2])
        state2.insert(0,record[3])
        city2.insert(0,record[4])
        zip2.insert(0,record[5])

    # create save button
    edit_button = Button(paww2,text="Update Record",command=update)
    edit_button.grid(row=6,column=1)

    # commit changes to database
    conn.commit()
    # close connection
    conn.close()    



# database create or connect to a crated one
conn = sqlite3.connect("/Users/paulavalos/Desktop/python/vscode/addressbook.db")

# create a cursor so dump and bring information
c = conn.cursor()

# create table
# after you run once comment out so you dont recreate the table over again
'''
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    state text,
    city text,
    zipcode integer
    )""")
'''

# create labels and entrys for all the info you asked for

f_name = Entry(paww)
f_name.grid(row=0,column=1)
f_label = Label(paww,text="First Name")
f_label.grid(row=0,column=0)

l_name = Entry(paww)
l_name.grid(row=1,column=1)
l_label = Label(paww,text="Last Name")
l_label.grid(row=1,column=0)

addi = Entry(paww)
addi.grid(row=2,column=1)
addi_label = Label(paww,text="Address")
addi_label.grid(row=2,column=0)

state = Entry(paww)
state.grid(row=3,column=1)
state_label = Label(paww,text="State")
state_label.grid(row=3,column=0)

city = Entry(paww)
city.grid(row=4,column=1)
city_label = Label(paww,text="City")
city_label.grid(row=4,column=0)

zip = Entry(paww)
zip.grid(row=5,column=1)
zip_label = Label(paww,text="Zip Code")
zip_label.grid(row=5,column=0)

# button to submit info
info_button = Button(paww,text="Submit Info",command=submit)
info_button.grid(row=6,column=1)

# query button
querybutton = Button(paww,text="show records",command=query)
querybutton.grid(row=7,column=1)

# delete button
deletebutton = Button(paww,text="Delete Record",command=delete_record)
deletebutton.grid(row=8,column=1)
# entry for the id 
delete_record_entry = Entry(paww)
delete_record_entry.grid(row=9,column=1)

# create edit button
edit_button = Button(paww,text="Update an entry",command=edit)
edit_button.grid(row=10,column=1)




# commit changes to database
conn.commit()

# close connection
conn.close()


paww.mainloop()