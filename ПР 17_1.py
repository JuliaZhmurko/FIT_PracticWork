import tkinter as tk
import cyrtranslit

window=tk.Tk()
label=tk.Label(text="Прізвище/Surname",fg="blue")

entry=tk.Entry()
button=tk.Button(text="Translate")

def handle_click(event):
    print("Кнопу натиснуто!")
    name = entry.get()    
    label_rez=tk.Label(text=cyrtranslit.to_latin(name))
    label_rez.pack()
button.bind("<Button-1>", handle_click)
label.pack()
entry.pack()
button.pack()
window.mainloop()