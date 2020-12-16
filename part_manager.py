from tkinter import *
from tkinter import Entry
from tkinter import Label
from tkinter import ttk
from tkinter import StringVar
from db import Database

# create window object
app = Tk()

db = Database("store.db")

def populate_list():
    print("Populate")
    for row in db.fetch():
        parts_list.insert(END, row)

def add_item():
    print("Add")

def remove_item():
    print("Remove")

def update_item():
    print("Update")

def clear_text():
    print("Clear")


# Part
part_text = StringVar()
part_label = Label(app, text="Part Name", font=("bold",14), pady=20)
part_label.grid(row=0, column=0, sticky=W) # posizione dell'etichetta
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1) # posizione della casella di testo

# Customer
customer_text = StringVar()
customer_label = Label(app, text="Customer", font=("bold",14))
customer_label.grid(row=0, column=2, sticky=W) # posizione dell'etichetta
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3) # posizione della casella di testo

# Retailer
retailer_text = StringVar()
retailer_label = Label(app, text="Retailer", font=("bold",14))
retailer_label.grid(row=1, column=0, sticky=W) # posizione dell'etichetta
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1) # posizione della casella di testo

# Price
price_text = StringVar()
price_label = Label(app, text="Price", font=("bold",14))
price_label.grid(row=1, column=2, sticky=W) # posizione dell'etichetta
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3) # posizione della casella di testo

# Parts List (list box)
parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# collegamento alla barra di scorrimento
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
# Buttons
add_btn = Button(app, text="Add Part", width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text="Remove Part", width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text="Update Part", width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text="Clear Input", width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

# titolo della finestra
app.title("Part Manager")
# dimensioni della finestra
app.geometry("700x350")
# start application


populate_list()


app.mainloop()

