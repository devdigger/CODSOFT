import tkinter
import random
from tkinter import messagebox
import os

file_path = os.path.realpath(__file__)
directory_path = os.path.dirname(file_path)
data_file = os.path.join(directory_path,"data.txt")
print(directory_path)

def update_tasks():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)
    numtask = len(tasks)
    label_dsp_count['text'] = numtask


def clear_listbox():
    lb_tasks.delete(0, "end")


def add_task():
    label_dsply["text"] = ""
    Ntask = text_input.get()
    if Ntask != "":
        tasks.append(Ntask)
        update_tasks()
    else:
        label_dsply["text"] = "Please enter the text"
    text_input.delete(0, 'end')


def delete_all():
    conf = messagebox.askquestion(
        'Delete all??', 'Are you sure to delete all tasks?')
    print(conf)
    if conf.upper() == "YES":
        global tasks
        tasks = []
        update_tasks()
    else:
        pass


def delete_one():
    de = lb_tasks.get("active")
    if de in tasks:
        tasks.remove(de)
    update_tasks()


def sort_asc():
    tasks.sort()
    update_tasks()


def sort_dsc():
    tasks.sort(reverse=True)
    update_tasks()


def random_task():
    randtask = random.choice(tasks)
    label_dsply["text"] = randtask


def number_task():
    numtask = len(tasks)
    label_dsply["text"] = numtask


def save_act():
    savecon = messagebox.askquestion(
        'Save Confirmation', 'Save your progress?')
    if savecon.upper() == "YES":
        with open(data_file, "w") as filehandle:
            for listitem in tasks:
                filehandle.write('%s\n' % listitem)
    else:
        pass


def load_act():
    loadcon = messagebox.askquestion(
        'Save Confirmation', 'Save your progress?')
    if loadcon.upper() == "YES":
        tasks.clear()

        with open(data_file, 'r') as filereader:
            for line in filereader:
                currentask = line
                tasks.append(currentask)
            update_tasks()

    else:
        pass


def exit_app():
    confex = messagebox.askquestion(
        'Quit Confirmation', 'Are you sue you want to quit?')
    if confex.upper() == "YES":
        root.destroy()
    else:
        pass


root = tkinter.Tk()
root.configure(bg="white")
root.title("To-do list")
root.geometry("260x300")

tasks = []

label_title = tkinter.Label(root, text="Todo List", bg="white")
label_title.grid(row=0, column=0)

label_dsply = tkinter.Label(root, text="", bg="white")
label_dsply.grid(row=0, column=1)

label_dsp_count = tkinter.Label(root, text="", bg="white")
label_dsp_count.grid(row=0, column=3)

text_input = tkinter.Entry(root, width=15)
text_input.grid(row=1, column=1)

# button section
text_add_bttn = tkinter.Button(
    root, text="add todo", bg="white", fg="green", width=15, command=add_task)
text_add_bttn.grid(row=1, column=0)

delone_bttn = tkinter.Button(
    root, text="Done Task", bg="white", width=15, command=delete_one)
delone_bttn.grid(row=2, column=0)

delall_bttn = tkinter.Button(
    root, text="Delete all", bg="white", width=15, command=delete_all)
delall_bttn.grid(row=3, column=0)

sort_asc = tkinter.Button(root, text="sort (ASC)",
                          bg="White", width=15, command=sort_asc)
sort_asc.grid(row=4, column=0)

sort_dsc = tkinter.Button(root, text="sort (DSC)",
                          bg="White", width=15, command=sort_dsc)
sort_dsc.grid(row=5, column=0)

random_bttn = tkinter.Button(
    root, text="random task", bg="White", width=15, command=random_task)
random_bttn.grid(row=6, column=0)

number_task = tkinter.Button(
    root, text="Number of Task", bg="white", width=15, command=number_task)
number_task.grid(row=7, column=0)

exit_bttn = tkinter.Button(root, text="exit app",
                           bg="white", width=15, command=exit_app)
exit_bttn.grid(row=8, column=0)

save_button = tkinter.Button(
    root, text="save TodoList", bg="white", width=15, command=save_act)
save_button.grid(row=10, column=1)

load_button = tkinter.Button(
    root, text="Load LastTodolist", bg="white", width=15, command=load_act)
load_button.grid(row=10, column=0)


lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2, column=1, rowspan=7)


root.mainloop()
