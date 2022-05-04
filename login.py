from _tkinter import*
from subprocess import call
from tkinter import Entry, Label, Tk, messagebox
from tkinter.ttk import Button

def login(t: Tk):
    entered_user = e1.get()
    entered_pass = e2.get()

    if (entered_user == "admin" and entered_pass == "123"):
        messagebox.showinfo("","logged in as admin")
        t.destroy()
        call(["python","admin.py"])


    elif (entered_user == "staff" and entered_pass == "123"):
        messagebox.showinfo("","logged in as staff")
        t.destroy()
        call(["python","store_manager_oop.py"])


    else:
       messagebox.showinfo("","invalid user or password")

cloth = Tk()
cloth.geometry("400x300")
cloth.title("Clothes management")

label = Label(cloth, text = "Login as", font=('Times New Roman',15))
label.grid(row=0, column=0)

l1 = Label(cloth, text="Username")
l2 = Label(cloth, text="Password")

e1 = Entry(cloth)
e2 = Entry(cloth)

bt = Button(cloth, text="Login",command=lambda: login(cloth))


l1.grid(row=1, column=0)
l2.grid(row=2, column=0)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

bt.grid(row=3, column=1)

cloth.mainloop()