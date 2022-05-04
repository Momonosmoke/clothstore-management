from _tkinter import*
from tkinter import Tk, Button
import subprocess

def open_part_manager(t: Tk):
    t.destroy()
    subprocess.call(["python", "part_manager.py"])



cloth = Tk()

col_count, row_count = cloth.grid_size()
 
for col in range(col_count):
    cloth.grid_columnconfigure(col, minsize=20)
 
for row in range(row_count):
    cloth.grid_rowconfigure(row, minsize=20)
    
cloth.geometry("200x150")
cloth.title("Staff Page")

bt1 = Button(cloth, text="Remaining", font=('Times New Roman',20, 'italic', 'bold'), bg='#808080')
bt1.pack()


bt2 = Button(cloth, text="Order", font=('Times New Roman',20, 'italic', 'bold'), bg='#808080', command=lambda: open_part_manager(cloth))
bt2.pack()


cloth.mainloop()