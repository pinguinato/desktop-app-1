from tkinter import *
from tkinter import Entry
from tkinter import Label
from tkinter import ttk
from tkinter import StringVar

# create window object
app = Tk()

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









# titolo della finestra
app.title("Part Manager")
# dimensioni della finestra
app.geometry("700x350")
# start application
app.mainloop()

