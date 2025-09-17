
# TASK 5 CONTACT BOOK


import tkinter as tk
from tkinter import messagebox

contacts = []

def save_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        contact = {"name": name, "phone": phone, "email": email, "address": address}
        contacts.append(contact)

        listbox.insert(tk.END, f"{name} - {phone}")

        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Name and Phone are required!")

def show_details(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        contact = contacts[index]
        details = (f"Name: {contact['name']}\n"
                   f"Phone: {contact['phone']}\n"
                   f"Email: {contact['email']}\n"
                   f"Address: {contact['address']}")
        messagebox.showinfo("Contact Details", details)

root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")

label = tk.Label(root, text="📖 Contact Book", font=("Arial", 20, "bold"))
label.pack(pady=10)

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack()

tk.Label(root, text="Phone:").pack()
entry_phone = tk.Entry(root, width=40)
entry_phone.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root, width=40)
entry_email.pack()

tk.Label(root, text="Address:").pack()
entry_address = tk.Entry(root, width=40)
entry_address.pack()

btn_save = tk.Button(root, text="Save Contact", command=save_contact, bg="lightblue")
btn_save.pack(pady=10)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Bind double-click event to listbox
listbox.bind("<Double-1>", show_details)

root.mainloop()


