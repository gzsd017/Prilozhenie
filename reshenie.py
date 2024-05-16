import subprocess
from tkinter import *
from tkinter import ttk

#Кнопка "Выход"
def click_button_nazad():
    subprocess.Popen(["python", "calc.py"])
    exit(root)

root5 = Tk()
root5.title("Решение")
root5.geometry("1920x1080")
root5.config(bg='#7FFF00')

editor = Text(height=40, width=185, wrap="word")
editor.grid(column=0, row=0, sticky=NSEW)

ys = ttk.Scrollbar(orient="vertical", command=editor.yview)
ys.grid(column=1, row=0, sticky=NS)

editor["yscrollcommand"] = ys.set

btn = ttk.Button(text="<---", command=click_button_nazad)
btn.place(x=250, y=750, anchor="e", width=200, height=25)

root5.mainloop()