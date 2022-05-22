# Super To Do List by Jesse White
# Python 3.10.4
# Part 1: Create the GUI elements
import tkinter
from tkinter import messagebox
import random

# Create root window
root = tkinter.Tk()

# Change root window background color
root.configure(bg="white")

# Change the title
root.title("My Super To Do List")

# Change the window size
root.geometry("350x300")

# Create an empty list
tasks = []

# For testing purposes use a default list
# tasks = ["Call mom", "practice piano", "more coding"]

# Create functions

def update_listbox():
    # Clear the current list
    clear_listbox()
    # Populate the listbox
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    # Get the task to add
    task = txt_input.get()
    # Make sure the task is not empty
    if task!="":
        # Append to the list
        tasks.append(task)
        # Update the listbox
        update_listbox()
    else:
        messagebox.showwarning("Warning", "You need to enter a task.")
    txt_input.delete(0, "end")

def delete_all():
    confirmed = messagebox.askyesno("Please Confirm", "Do you really want to delete all?")
    if confirmed == True:
        # Since we are changing the list, it needs to be global
        global tasks
        # Clear the task list
        tasks = []
        # Update the listbox
        update_listbox()

def del_one():
    # Get the text of the currently selected item
    task = lb_tasks.get("active")
    # Confirm it is in the list
    if task in tasks:
        tasks.remove(task)
    # Update the listbox
    update_listbox()

def sort_asc():
    # Sort the list
    tasks.sort()
    # Update the listbox
    update_listbox()

def sort_desc():
    # Sort the list
    tasks.sort()
    # Reverse the list
    tasks.reverse()
    # Update the listbox
    update_listbox()

def choose_random():
    # Choose a random task
    task = random.choice(tasks)
    # Update the display label
    lbl_display["text"]=task

def show_number_of_tasks():
    # Get the number of tasks
    number_of_tasks = len(tasks)
    # Create and format the message
    msg = "Number of tasks: %s" %number_of_tasks
    # Display the message
    lbl_display["text"]=msg

lbl_title = tkinter.Label(root, text="To-Do-List", bg="white")
lbl_title.grid(row=0,column=0)

lbl_display = tkinter.Label(root, text="", bg="white")
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(root, width=15)
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root, text="Add task", fg="black", bg="white", command=add_task)
btn_add_task.grid(row=1,column=0)

btn_delete_all = tkinter.Button(root, text="Delete All", fg="black", bg="white", command=delete_all)
btn_delete_all.grid(row=2,column=0)

btn_del_one = tkinter.Button(root, text="Delete", fg="black", bg="white", command=del_one)
btn_del_one.grid(row=3,column=0)

btn_sort_asc = tkinter.Button(root, text="Sort (ASC)", fg="black", bg="white", command=sort_asc)
btn_sort_asc.grid(row=4,column=0)

btn_sort_desc = tkinter.Button(root, text="Sort (DESC)", fg="black", bg="white", command=sort_desc)
btn_sort_desc.grid(row=5,column=0)

btn_choose_random = tkinter.Button(root, text="Choose Random", fg="black", bg="white", command=choose_random)
btn_choose_random.grid(row=6,column=0)

btn_number_of_tasks = tkinter.Button(root, text="Number of Tasks", fg="black", bg="white", command=show_number_of_tasks)
btn_number_of_tasks.grid(row=7,column=0)

btn_exit = tkinter.Button(root, text="Exit", fg="green", bg="white", command=exit)
btn_exit.grid(row=8,column=0)

lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2, column=1, rowspan=7)

# Start the main events loop
root.mainloop()