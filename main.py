from tkinter import *
from tkinter import messagebox

# Function to add task
def add_task():
    task = task_entry.get()

    if task != "":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning(
            "Warning",
            "Please enter a task"
        )

# Function to delete selected task
def delete_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected)
    except:
        messagebox.showwarning(
            "Warning",
            "Select a task first"
        )

# Function to clear all tasks
def clear_tasks():
    task_listbox.delete(0, END)

# Main Window
root = Tk()

root.title("To-Do List")
root.geometry("400x500")

# Heading
Label(
    root,
    text="To-Do List Application",
    font=("Arial", 16, "bold")
).pack(pady=10)

# Entry Box
task_entry = Entry(
    root,
    width=30
)
task_entry.pack(pady=10)

# Add Button
Button(
    root,
    text="Add Task",
    command=add_task
).pack(pady=5)

# Listbox
task_listbox = Listbox(
    root,
    width=40,
    height=12
)
task_listbox.pack(pady=10)

# Delete Button
Button(
    root,
    text="Delete Selected Task",
    command=delete_task
).pack(pady=5)

# Clear Button
Button(
    root,
    text="Clear All Tasks",
    command=clear_tasks
).pack(pady=5)

# Run Program
root.mainloop()