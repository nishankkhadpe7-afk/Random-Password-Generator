import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 8:
            messagebox.showwarning("Weak Password", "Minimum length is 8.")
            return

        char_pool = ""
        password_chars = []

        if upper_var.get():
            char_pool += string.ascii_uppercase
            password_chars.append(random.choice(string.ascii_uppercase))

        if lower_var.get():
            char_pool += string.ascii_lowercase
            password_chars.append(random.choice(string.ascii_lowercase))

        if digit_var.get():
            char_pool += string.digits
            password_chars.append(random.choice(string.digits))

        if symbol_var.get():
            char_pool += string.punctuation
            password_chars.append(random.choice(string.punctuation))

        if not char_pool:
            messagebox.showerror("Error", "Select at least one character type.")
            return

        while len(password_chars) < length:
            password_chars.append(random.choice(char_pool))

        random.shuffle(password_chars)
        password = ''.join(password_chars)

        output_entry.delete(0, tk.END)
        output_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digit_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()

tk.Checkbutton(root, text="Uppercase", variable=upper_var).grid(row=1, column=0)
tk.Checkbutton(root, text="Lowercase", variable=lower_var).grid(row=1, column=1)
tk.Checkbutton(root, text="Numbers", variable=digit_var).grid(row=2, column=0)
tk.Checkbutton(root, text="Symbols", variable=symbol_var).grid(row=2, column=1)

tk.Button(root, text="Generate", command=generate_password).grid(row=3, column=0)
tk.Button(root, text="Copy", command=copy_to_clipboard).grid(row=3, column=1)

output_entry = tk.Entry(root, width=30)
output_entry.grid(row=4, column=0, columnspan=2)

root.mainloop()


