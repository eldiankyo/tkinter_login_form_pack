import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('350x180')
root.title('Login')
root.resizable(True, False)
root.config(bg='#d9d9d9')

fields = {}

fields['username_label'] = ttk.Label(text='Username:')
fields['username'] = ttk.Entry()

fields['password_label'] = ttk.Label(text='Password:')
fields['password'] = ttk.Entry(show='•')

for field in fields.values():
    field.pack(anchor='w', padx=10, pady=5, fill='x')

ttk.Button(text='Login').pack(padx='10', pady='10', fill='x')


root.mainloop()