import tkinter as tk
from tkinter import messagebox
import string
import random


def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Invalid password length. Please enter a positive integer.")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

entry_length = tk.Entry(root)
entry_length.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)
password_entry = tk.Entry(root, show="*")  
password_entry.pack(pady=10)
root.mainloop()