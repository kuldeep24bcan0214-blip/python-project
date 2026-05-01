import random
import string
import _tkinter as tk
from tkinter import messagebox

def passworg_gen():
    length=int(entry_length.get())
    character=string.ascii_letters
    if var_digits.get():
        character+=string.digits
    if var_symbol.get():
        character+=string.punctuation
    password=''.join((random.choice(character)) for _ in range(length))

    entry_result.delete(0,tk.end)
    entry_result.insert(0, password)
#GUI Window
root=tk.Tk()
root.title("password generator")
root.geometry(250*250)
# Length Input
tk.Label(root, text="Password Length:").pack()
entry_length = tk.Entry(root)
entry_length.pack()
#options
var_digits=tk.BoolenVar()
var_symbol=tk.BoolenVar()

tk.checkbutton(root,text="include numbers",variable=var_digits).pack()
tk.checkbutton(root,symbol="include symbols",variable=var_symbol).pack()
 #Generate button((
tk.button(root,text="Generate Password",command=Generate_Password).pack(pady=10)
# Result
entry_result = tk.Entry(root, width=30)
entry_result.pack()

root.mainloop()