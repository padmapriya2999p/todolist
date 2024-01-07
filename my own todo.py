# TO-DO List using Tkinter and SQLite3
#create the GUI Elements
import tkinter
from tkinter import messagebox 

import sqlite3

#create root window 
root=tkinter.Tk()
#change root window background colour
root.configure(bg="white")

#change the title
root.title("Our own To-Do genidappa :)")

#change the window size 
root.geometry("200x500")

#create an empty list
tasks=[]

#create function 
def update_listbox():
    #clear the current list
    clear_listbox()
    #populate the listbox
    for task in tasks:
        lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0,"end")

def add_task():
    #get the task to add
    task = txt_input.get()
    #Make sure the task is not empty
    if task!="":
        #append to the list
        tasks.append(task)
        #update the list box
        update_listbox()
        conn=sqlite3.connect("details.db")
        cur = conn.cursor()
        #cur.execute("DROP TABLE task;")
        cur.execute("CREATE TABLE IF NOT EXISTS task(task TEXT);")
        #cur.execute("INSERT INTO task VALUES('hi');")
        cur.execute("INSERT INTO task VALUES('"+task+"');")
        conn.commit()
        conn.close()
        messagebox.showinfo("Status","Task Added")
    else:
        lbl_display["text"]="Please enter a task"
    txt_input.delete(0,"end")

def del_task():
    pass

#creating a title
lbl_title=tkinter.Label(root,text="To-Do List",bg="white")
lbl_title.pack()

lbl_display=tkinter.Label(root,text="",bg="white")
lbl_display.pack()

#list of functions that the app can do
txt_input=tkinter.Entry(root,width=15)
txt_input.pack()

btn_add_task = tkinter.Button(root,text="Add task",fg="green",bg="white",command=add_task)
btn_add_task.pack()

btn_del = tkinter.Button(root,text="Delete",fg="green",bg="white",command=del_task)
btn_del.pack()

lb_tasks=tkinter.Listbox(root)
lb_tasks.pack()


#Start the main events loop
root.mainloop()

