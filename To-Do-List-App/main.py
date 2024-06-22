import tkinter
import tkinter.messagebox
import pickle
root = tkinter.Tk()
root.title("To-Do-List Application")

def addTask():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Error", message="Make sure you entered the task.")

def deleteTask():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Error", message="Make sure you selected the task.")

def loadTask():
    try:    
        tasks = pickle.load(open("tasks.txt", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for tasks in tasks:
            listbox_tasks.insert(tkinter.END, tasks)
    except:
        tkinter.messagebox.showwarning(title="Error", message="Cannot find old tasks.")

def saveTask():
    tasks = listbox_tasks.get(0 , listbox_tasks.size())
    pickle.dump(tasks, open("tasks.txt", "wb"))
    
#Gui
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=73)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT , fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=75)
entry_task.pack()

button_addTask = tkinter.Button(root, text="Add Task", width=72, command=addTask)
button_addTask.pack()

button_deleteTask = tkinter.Button(root, text="Delete Task", width=72, command=deleteTask)
button_deleteTask.pack()

button_loadTask = tkinter.Button(root, text="Load Task", width=72, command=loadTask)
button_loadTask.pack()

button_saveTask = tkinter.Button(root, text="Save Task", width=72, command=saveTask)
button_saveTask.pack()

root.mainloop()