import subprocess
from tkinter import *
from tkinter import ttk

#Кнопка "Выход"
def click_button_nazad():
    subprocess.Popen(["python", "menu.py"])
    exit(root2)

root2 = Tk()
root2.title("Правила использования")
root2.geometry("1920x1080")
root2.config(bg='#33ffe6')

btn = ttk.Button(text="<---", command=click_button_nazad)
btn.place(x=250, y=750, anchor="e", width=200, height=25)

label = ttk.Label(root2, text="Правила использования", background='#33ffe6', font=("Arial", 40))
label.place(relx=0.5, rely=0.3, anchor="c")
label.pack()

label1 = ttk.Label(root2, text="Правила использования", background='#33ffe6', font=("Arial", 20))
label1.place(relx=0.5, rely=0.6, anchor="c")
label1.pack()



root2.mainloop()