from tkinter import *
from ttkthemes import ThemedTk
from tkinter import ttk
import pandas as pd
from tkinter.filedialog import askopenfile

root = ThemedTk(theme="arc")
root.title("User entry")
root.geometry("500x600")

name_ = StringVar()
passs_ = StringVar()

ttk.Label(root, text="User name").pack(pady=5)
user_name = ttk.Entry(root, width=50,textvariable= name_)
user_name.pack()
ttk.Label(root, text="password").pack(pady=5)
pass_word = ttk.Entry(root, width=50,textvariable = passs_)
pass_word.pack()

file = open("data.csv", "a")
file.close()
file = open("data.csv", "r")
if file.read(9) == "User_Name":
    file.close()
else:
    file = open("data.csv", "a")
    file.write("User_Name,")
    file.write("Password\n")
    file.close()

global var , var2 ,var3,error, var , error2 , var2
var = 0
var2 = 0
var3 = 0


def submit():
    name = name_.get()
    passs = passs_.get()
    data_file  = open("data.csv", 'r')
    for line in data_file.readlines():
        if line == f'{str(name)},{str(passs)}\n':
            duplicate_record = True
            var2 += 1
        else:
            duplicate_record = False

    if ((name == "") or (passs == "")) and (var == 0):
        error = Label(root, text="Enter both User name and Password")
        error.pack()
        var = 1

    elif (not ((name == "") or (passs == ""))) and (not duplicate_record):
        data_file = open("data.csv", 'a')
        data_file.write(f'{str(name)},')
        data_file.write(f'{str(passs)}\n')
        data_file.close()
        error.destroy()
        var = 0
    elif duplicate_record and var2 == 1:
        error2 = Label(root, text="Duplicate_record found ")
        error2.pack()
    if (not duplicate_record) and (not var2 == 0):
        error2.destroy()


    user_name.delete(0, END)
    pass_word.delete(0, END)


def clear():
    user_name.delete(0, END)
    pass_word.delete(0, END)


def view_records():
    data = Text(root , height = 10 , width = 30)
    data.pack()
    dataset = pd.read_csv("data.csv")
    data.insert(END,dataset)
    
    var3=1

submit_b = ttk.Button(root, text="submit", command=submit).pack(padx=20, pady=11)
clear_b = ttk.Button(root, text="clear", command=clear).pack()
view_record = ttk.Button(root, text="Click here to view records", command=view_records).pack(pady=11)
root.mainloop()