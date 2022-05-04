from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')


def populate_list():
    clothes_list.delete(0, END)
    for row in db.fetch():
        clothes_list.insert(END, row)


def add_item():
    if clothes_text.get() == '' or customer_text.get() == '' or retailer_text.get() == '' or price_text.get() == '' or order_time_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(clothes_text.get(), customer_text.get(),
              retailer_text.get(), price_text.get(), order_time_text.get())
    clothes_list.delete(0, END)
    clothes_list.insert(END, (clothes_text.get(), customer_text.get(), retailer_text.get(), price_text.get(), order_time_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = clothes_list.curselection()[0]
        selected_item = clothes_list.get(index)
        clothes_entry.delete(0, END)
        clothes_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
        order_time_entry.delete(0, END)
        order_time_entry.insert(END, selected_item[5])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], clothes_text.get(), customer_text.get(), price_text.get(), order_time_text.get(), retailer_text.get())
    populate_list()


def clear_text():
    clothes_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)
    order_time_entry.delete(0, END)


# Create window object
app = Tk()

# clothes
clothes_text = StringVar()
clothes_label = Label(app, text='Clothes', font=('bold', 14), pady=20)
clothes_label.grid(row=0, column=0, sticky=W)
clothes_entry = Entry(app, textvariable=clothes_text)
clothes_entry.grid(row=0, column=1)
# Customer
customer_text = StringVar()
customer_label = Label(app, text='Customer', font=('bold', 14))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)
# Retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer', font=('bold', 14))
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)
# Price
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 14))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)
# Order time
order_time_text = StringVar()
order_time_label = Label(app, text='Order Time', font=('bold', 14))
order_time_label.grid(row=2, column=0, sticky=W)
order_time_entry = Entry(app, textvariable=order_time_text)
order_time_entry.grid(row=2, column=1)
# clothes List (Listbox)
clothes_list = Listbox(app, height=8, width=50, border=0)
clothes_list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=4, column=3)
# Set scroll to listbox
clothes_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=clothes_list.yview)
# Bind select
clothes_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add clothes', width=12, command=add_item)
add_btn.grid(row=3, column=0, pady=20)

remove_btn = Button(app, text='Remove clothes', width=12, command=remove_item)
remove_btn.grid(row=3, column=1)

update_btn = Button(app, text='Update clothes', width=12, command=update_item)
update_btn.grid(row=3, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=3, column=3)

app.title('Seven Boutique')
app.geometry('700x350')

# Populate data
populate_list()

# Start program
app.mainloop()