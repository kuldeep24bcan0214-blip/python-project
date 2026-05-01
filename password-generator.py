import  random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Enter valid length")
            return
    except:
        messagebox.showerror("Error", "Enter a number")
        return

    characters = string.ascii_letters

    if var_digits.get():
        characters += string.digits
    if var_symbol.get():
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    entry_result.delete(0, tk.END)
    entry_result.insert(0, password)

# GUI Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x250")

# Length Input
tk.Label(root, text="Password Length:").pack()
entry_length = tk.Entry(root)
entry_length.pack()

# Options
var_digits = tk.BooleanVar()
var_symbol = tk.BooleanVar()

tk.Checkbutton(root, text="Include Numbers", variable=var_digits).pack()
tk.Checkbutton(root, text="Include Symbols", variable=var_symbol).pack()

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Result
entry_result = tk.Entry(root, width=30)
entry_result.pack()

root.mainloop()