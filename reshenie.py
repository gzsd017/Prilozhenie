import subprocess
from tkinter import *
from tkinter import ttk

#Кнопка "Выход"
def click_button_nazad():
    subprocess.Popen(["python", "calc.py"])
    exit(root)

root = Tk()
root.title("Решение")
root.geometry("1920x1080")
root.config(bg='#33ffe6')

entry = ttk.Entry()
entry.pack(anchor=NW, padx=8, pady= 8)
entry.place(x=250, y=750, anchor="e", width=200, height=25)

btn = ttk.Button(text="<---", command=click_button_nazad)
btn.place(x=250, y=750, anchor="e", width=200, height=25)

root.mainloop()