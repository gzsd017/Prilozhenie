from tkinter import *
from tkinter import ttk
import subprocess


#Кнопка "Калькулятор"
def click_button_calc():
    subprocess.Popen(["python", "calculator.py"])
    root.withdraw()
    exit(root)


#Кнопка "Правила использования"
def click_button_rool():
    subprocess.Popen(["python", "pravila.py"])
    root.withdraw()
    exit(root)

#Кнопка "Выход"
def click_button_nazad():
    exit(root)

root = Tk()
root.title("Решение уравнений 1,2,3,4 степени")
root.geometry("1920x1080")
root.config(bg='#7FFF00')

label = ttk.Label(root, text="Решение уравнений 1,2,3,4 степени", background='#7FFF00', font=("Arial", 40))
label.place(relx=0.5, rely=0.3, anchor="c")
label.pack()

btn = ttk.Button(text="Калькулятор", command=click_button_calc)
btn.place(relx=0.5, rely=0.3, anchor="c", relwidth=0.45, relheight=0.10)

btn = ttk.Button(text="Правила использования", command=click_button_rool)
btn.place(relx=0.5, rely=0.45, anchor="c", relwidth=0.45, relheight=0.10)

btn = ttk.Button(text="Выход", command=click_button_nazad)
btn.place(x=250, y=750, anchor="e", width=200, height=25)

root.mainloop()


