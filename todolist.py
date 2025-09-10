import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# List to store tasks
todo_list = []

# Function to update the Listbox display
def update_listbox():
    listbox.delete(0, tk.END)
    for task in todo_list:
        listbox.insert(tk.END, task)

# Add Task
def add_task():
    task = simpledialog.askstring("Add Task", "Enter the task:")
    if task:
        todo_list.append(task)
        update_listbox()

# Update Task
def update_task():
    try:
        selected_index = listbox.curselection()[0]
        new_task = simpledialog.askstring("Update Task", "Enter the new task:")
        if new_task:
            todo_list[selected_index] = new_task
            update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Delete Task
def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        removed_task = todo_list.pop(selected_index)
        update_listbox()
        messagebox.showinfo("Deleted", f"Task '{removed_task}' deleted successfully!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Listbox to show tasks
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=20)

# Buttons
frame = tk.Frame(root)
frame.pack(pady=10)

add_btn = tk.Button(frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(frame, text="Update Task", width=12, command=update_task)
update_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

# Run the application
root.mainloop()
