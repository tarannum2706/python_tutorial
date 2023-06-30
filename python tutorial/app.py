import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title('Tkinter Window Demo')
root.geometry('600x400+50+50')
name=input("Enter you name: ")
message = tk.Label(root, text="Hello " +name,font=("Helvetica", 14))
message.pack(ipadx=150, ipady=150)

def button_clicked():
 print('Button clicked')
#    button1 = ttk.Button(root, text='Button Clicked')
#    button1.pack()
   
 button = ttk.Button(root, text='Click Me', command=button_clicked)
 button.pack()

# photo = tk.PhotoImage(file='')
# image_label = ttk.Label(
# root,
# image=photo,
# padding=5
# )
# image_label.pack()

root.mainloop()
