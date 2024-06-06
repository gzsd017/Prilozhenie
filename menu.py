from tkinter import *
from tkinter import ttk
import subprocess

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def create_main_window():
    root = Tk()
    center_window(root, 700, 500)
    root.title("Решение уравнений 1,2,3,4 степени")
    root.geometry("700x500")
    root.config(bg='#7FFF00')
    root.resizable(False, False)

    label = ttk.Label(root, text="Решение уравнений 1,2,3,4 степени", background='#7FFF00', font=("Arial", 20))
    label.place(relx=0.5, rely=0.1, anchor="c")

    btn_calc = ttk.Button(text="Калькулятор", command=click_button_calc)
    btn_calc.place(relx=0.5, rely=0.3, anchor="c", relwidth=0.45, relheight=0.10)

    btn_rules = ttk.Button(text="Правила использования", command=click_button_rules)
    btn_rules.place(relx=0.5, rely=0.45, anchor="c", relwidth=0.45, relheight=0.10)

    btn_exit = ttk.Button(text="Выход", command=click_button_exit)
    btn_exit.place(x=230, y=440, anchor="e", width=200, height=25)

    return root

def click_button_calc():
    subprocess.Popen(["python", "calculator.py"])
    root.withdraw()
    exit(root)


def click_button_rules():
    root2 = create_rules_window()
    root2.grab_set()
    root2.mainloop()
    root.withdraw()
    exit(root)


def click_button_exit():
    exit()

def click_button_menu():
    subprocess.Popen(["python", "menu.py"])
    root.withdraw()
    exit(root)

def create_rules_window():
    root2 = Toplevel()
    center_window(root2, 700, 500)
    root2.title("Правила использования")
    root2.geometry("700x500")
    root2.config(bg='#7FFF00')
    root2.resizable(False, False)


    label = ttk.Label(root2, text="Правила использования", background='#7FFF00', font=("Arial", 20))
    label.place(relx=0.5, rely=0.1, anchor="c")

    labels_text = [
        "Введите коэффициенты уравнения, которое требуется решить,",
        "используя предоставленное поле для ввода текста.",
        "После ввода уравнения нажмите на кнопку 'Решить',",
        "чтобы приложение вычислило корни уравнения",
        "и предоставило результат.",
        "Внимательно изучите полученный ответ,",
        "убедитесь в правильности решения и в том,",
        "что все корни уравнения были найдены."
    ]

    y_offset = 0.2
    for text in labels_text:
        label = ttk.Label(root2, text=text, background='#7FFF00', font=("Arial", 15))
        label.place(relx=0.5, rely=y_offset, anchor="c")
        y_offset += 0.05

    btn_back = ttk.Button(root2, text="<---", command=root2.destroy)
    btn_back.place(x=10, y=10)

    return root2

root = create_main_window()
root.mainloop()
