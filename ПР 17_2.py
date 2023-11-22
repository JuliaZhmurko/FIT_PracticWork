import tkinter as tk
from tkinter import *
def handle_click():
    x=entry1.get()
    if len(x) == 0:
        x=0
    x=float(x)
    y=var.get()
    if y==1:
        miles = x * 0.621371 # частка милі у кілометрі
        res1=tk.Label(text= miles)
        res1.grid(row=1,column=1)
    elif y==2:
        lieue = x * 0.17998560115191 # частка льє у кілометрі
        res2=tk.Label(text= lieue)
        res2.grid(row=2,column=1)
win=tk.Tk()
win.geometry("650x450")
entry1=tk.Entry()
var=IntVar()
var.set(1)
radio1=tk.Radiobutton(text="Перевести у милі", value=1, variable=var)
radio2=tk.Radiobutton(text="Перевести у льє", value=2, variable=var)
lab1=tk.Label(width=50,text="Кілометри")
button1=tk.Button(master=win,text="Обчислити", command=handle_click)
lab1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
radio1.grid(row=1,column=0)
radio2.grid(row=2,column=0)
button1.grid(row=3,column=0)
win.mainloop()