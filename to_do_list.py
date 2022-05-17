# Simple To-Do List App
# By Jesse White
# Python 3.10.4 using VS Code
# Windows 10 (Mac and Linux compatible)
# Topics: tkinter, grid geometry manager
# Topics: Listbox Widget, Scrollbar widget, tkinter.messagebox, try/except block, pickle

import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("To-Do List by Jesse White")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

# Create GUI
listbox_tasks = tkinter.Listbox(root, height=3, width=50)
listbox_tasks.pack()

scrollbar_tasks = tkinter.Scrollbar(root)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()



root.mainloop()