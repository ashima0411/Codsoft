import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def save_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task)
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")


frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)


listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10, selectbackground="yellow")
listbox_tasks.pack(side=tk.LEFT)


scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)


listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)


entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=10, padx=10)

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_save_tasks = tk.Button(root, text="Save Tasks", width=48, command=save_tasks)
button_save_tasks.pack()

load_tasks()
root.mainloop()