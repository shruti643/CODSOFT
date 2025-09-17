# TASK 3 PASSWORD GENERATOR

import tkinter as tk
from tkinter import messagebox
import random
import string

# function to create password
def make_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Too Short", "Password length should be at least 4")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")
        return

    # characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))

    # display result
    output_var.set(password)

# function to copy password
def copy_password():
    generated = output_var.get()
    if generated:
        root.clipboard_clear()
        root.clipboard_append(generated)
        messagebox.showinfo("Copied", "Password copied to clipboard")
    else:
        messagebox.showwarning("Empty", "No password to copy")

# main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("420x250")
root.config(bg="lightblue")

# heading
heading = tk.Label(root, text="🔐 Password Generator", font=("Arial", 16, "bold"), bg="lightblue")
heading.pack(pady=10)

# input label + entry
tk.Label(root, text="Enter password length:", font=("Arial", 12), bg="lightblue").pack()
length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack(pady=5)

# buttons
btn_frame = tk.Frame(root, bg="lightblue")
btn_frame.pack(pady=10)

generate_btn = tk.Button(btn_frame, text="Generate", font=("Arial", 12), command=make_password, bg="green", fg="white", width=10)
generate_btn.grid(row=0, column=0, padx=5)

copy_btn = tk.Button(btn_frame, text="Copy", font=("Arial", 12), command=copy_password, bg="orange", fg="white", width=10)
copy_btn.grid(row=0, column=1, padx=5)

# output field
output_var = tk.StringVar()
output_label = tk.Entry(root, textvariable=output_var, font=("Arial", 12), width=35, justify="center")
output_label.pack(pady=10)

# run app
root.mainloop()
