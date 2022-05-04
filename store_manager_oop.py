import tkinter as tk
from tkinter import messagebox
from db import Database

# Instantiate database object
db = Database('store.db')

# Main Application/GUI class
class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Seventh Boutique')
        # Width height
        master.geometry("1920x1080")
        # Create widgets/grid
        self.create_widgets()
        # Init selected item var
        self.selected_item = 0  
        # Populate initial list
        self.populate_list()

    def create_widgets(self):
        # clothes
        self.clothes_text = tk.StringVar()
        self.clothes_label = tk.Label(
            self.master, text='Clothes', font=('bold', 14), pady=20)
        self.clothes_label.grid(row=0, column=0, sticky=tk.W)
        self.clothes_entry = tk.Entry(self.master, textvariable=self.clothes_text)
        self.clothes_entry.grid(row=0, column=1)
        # Customer
        self.customer_text = tk.StringVar()
        self.customer_label = tk.Label(
            self.master, text='Customer', font=('bold', 14))
        self.customer_label.grid(row=0, column=2, sticky=tk.W)
        self.customer_entry = tk.Entry(self.master, textvariable=self.customer_text)
        self.customer_entry.grid(row=0, column=3)
        # Retailer
        self.retailer_text = tk.StringVar()
        self.retailer_label = tk.Label(
            self.master, text='Retailer', font=('bold', 14))
        self.retailer_label.grid(row=1, column=0, sticky=tk.W)
        self.retailer_entry = tk.Entry(self.master, textvariable=self.retailer_text)
        self.retailer_entry.grid(row=1, column=1)
        # Price
        self.price_text = tk.StringVar()
        self.price_label = tk.Label(
            self.master, text='Price', font=('bold', 14))
        self.price_label.grid(row=1, column=2, sticky=tk.W)
        self.price_entry = tk.Entry(self.master, textvariable=self.price_text)
        self.price_entry.grid(row=1, column=3)
        # Order_time
        self.order_time_text = tk.StringVar()
        self.order_time_label = tk.Label(
            self.master, text='Order time', font=('bold', 14))
        self.order_time_label.grid(row=2, column=0, sticky=tk.W)
        self.order_time_entry = tk.Entry(self.master, textvariable=self.order_time_text)
        self.order_time_entry.grid(row=2, column=1)
        # clothes list (listbox)
        self.clothes_list = tk.Listbox(self.master, height=9, width=60, border=0)
        self.clothes_list.grid(row=4, column=0, columnspan=3,
                             rowspan=6, pady=20, padx=20)
        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=4, column=3)
        # Set scrollbar to clothess
        self.clothes_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.clothes_list.yview)

        # Bind select
        self.clothes_list.bind('<<ListboxSelect>>', self.select_item)

        # Buttons
        self.add_btn = tk.Button(
            self.master, text="Add clothes", width=12, command=self.add_item)
        self.add_btn.grid(row=3, column=0, pady=20)

        self.remove_btn = tk.Button(
            self.master, text="Remove clothes", width=12, command=self.remove_item)
        self.remove_btn.grid(row=3, column=1)

        self.update_btn = tk.Button(
            self.master, text="Update clothes", width=12, command=self.update_item)
        self.update_btn.grid(row=3, column=2)

        self.exit_btn = tk.Button(
            self.master, text="Clear Input", width=12, command=self.clear_text)
        self.exit_btn.grid(row=3, column=3)

    def populate_list(self):
        # Delete items before update. So when you keep pressing it doesn't keep getting (show example by calling this twice)
        self.clothes_list.delete(0, tk.END)
        # Loop through records
        for row in db.fetch():
            # Insert into list
            self.clothes_list.insert(tk.END, row)

    # Add new item
    def add_item(self):
        if self.clothes_text.get() == '' or self.customer_text.get() == '' or self.retailer_text.get() == '' or self.price_text.get() == '' or self.order_time_text.get() == '':
            messagebox.showerror(
                "Required Fields", "Please include all fields")
            return
        print(self.clothes_text.get())
        # Insert into DB
        db.insert(self.clothes_text.get(), self.customer_text.get(),
                  self.retailer_text.get(), self.price_text.get(), self.order_time_text.get())
        # Clear list
        self.clothes_list.delete(0, tk.END)
        # Insert into list
        self.clothes_list.insert(tk.END, (self.clothes_text.get(), self.customer_text.get(), self.retailer_text.get(), self.price_text.get(), self.order_time_text.get()))
        self.clear_text()
        self.populate_list()
    # Runs when item is selected
    def select_item(self, event):
        # # Create global selected item to use in other functions
        # global self.selected_item
        try:
            # Get index
            index = self.clothes_list.curselection()[0]
            # Get selected item
            self.selected_item = self.clothes_list.get(index)
            # print(selected_item) # Print tuple

            # Add text to entries
            self.clothes_entry.delete(0, tk.END)
            self.clothes_entry.insert(tk.END, self.selected_item[1])
            self.customer_entry.delete(0, tk.END)
            self.customer_entry.insert(tk.END, self.selected_item[2])
            self.retailer_entry.delete(0, tk.END)
            self.retailer_entry.insert(tk.END, self.selected_item[3])
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(tk.END, self.selected_item[4])
            self.order_time_entry.delete(0, tk.END)
            self.order_time_entry.insert(tk.END, self.selected_item[5])
        except IndexError:
            pass

    # Remove item
    def remove_item(self):
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()

    # Update item
    def update_item(self):
        db.update(self.selected_item[0], self.clothes_text.get(), self.customer_text.get(), self.price_text.get(), self.order_time_text.get(), self.retailer_text.get())
        self.populate_list()

    # Clear all text fields
    def clear_text(self):
        self.clothes_entry.delete(0, tk.END)
        self.customer_entry.delete(0, tk.END)
        self.retailer_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.order_time_entry.delete(0, tk.END)


root = tk.Tk()
app = Application(master=root)
app.mainloop()