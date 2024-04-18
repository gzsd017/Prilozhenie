from tkinter import *
import tkinter as tk
from tkinter import ttk

#Кнопка "Выход"
def click_button_nazad():
    subprocess.Popen(["python", "menu.py"])
    exit(root3)

def add_digit(digit):
    value = calc.get() + str(digit)
    calc.delete(0,tk.END)
    calc.insert(0,value)

def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))

def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), command=lambda: add_digit(operation))

root3 = Tk()
root3.title('Калькулятор')
root3.geometry('600x600+300+300')

btn = ttk.Button(text="<---", command=click_button_nazad)
btn.place(x=250, y=750, anchor="e", width=200, height=25)

calc = tk.Entry(root3, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.grid(row=0, column=0, columnspan=3, stick='we')

make_operation_button('/').grid(row=1, column=0, stick='wens', padx=2, pady=2)
make_operation_button('(').grid(row=1, column=1, stick='wens', padx=2, pady=2)
make_operation_button(')').grid(row=1, column=2, stick='wens', padx=2, pady=2)
make_operation_button('C').grid(row=1, column=3, stick='wens', padx=2, pady=2)
make_digit_button('1').grid(row=2, column=1, stick='wens', padx=2, pady=2)
make_digit_button('2').grid(row=2, column=2, stick='wens', padx=2, pady=2)
make_digit_button('3').grid(row=2, column=3, stick='wens', padx=2, pady=2)
make_digit_button('4').grid(row=3, column=1, stick='wens', padx=2, pady=2)
make_digit_button('5').grid(row=3, column=2, stick='wens', padx=2, pady=2)
make_digit_button('6').grid(row=3, column=3, stick='wens', padx=2, pady=2)
make_digit_button('7').grid(row=4, column=1, stick='wens', padx=2, pady=2)
make_digit_button('8').grid(row=4, column=2, stick='wens', padx=2, pady=2)
make_digit_button('9').grid(row=4, column=3, stick='wens', padx=2, pady=2)
make_digit_button('0').grid(row=5, column=1, columnspan=2, stick='wens', padx=2, pady=2)
make_operation_button('=').grid(row=5, column=3, stick='wens', padx=2, pady=2)
make_digit_button('x').grid(row=2, column=0, stick='wens', padx=2, pady=2)
make_digit_button('x^2').grid(row=3, column=0, stick='wens', padx=2, pady=2)
make_digit_button('x^3').grid(row=4, column=0, stick='wens', padx=2, pady=2)
make_digit_button('x^4').grid(row=5, column=0, stick='wens', padx=2, pady=2)
make_operation_button('<--').grid(row=1, column=4, stick='wens', padx=2, pady=2)
make_operation_button('+').grid(row=2, column=4, stick='wens', padx=2, pady=2)
make_operation_button('=').grid(row=3, column=4, stick='wens', padx=2, pady=2)
make_operation_button('*').grid(row=4, column=4, stick='wens', padx=2, pady=2)
make_digit_button(',').grid(row=5, column=4, stick='wens', padx=2, pady=2)

root3.grid_columnconfigure(0,minsize=80)
root3.grid_columnconfigure(1,minsize=80)
root3.grid_columnconfigure(2,minsize=80)
root3.grid_columnconfigure(3,minsize=80)
root3.grid_columnconfigure(4,minsize=80)

root3.grid_rowconfigure(1,minsize=80)
root3.grid_rowconfigure(2,minsize=80)
root3.grid_rowconfigure(3,minsize=80)
root3.grid_rowconfigure(4,minsize=80)
root3.grid_rowconfigure(5,minsize=80)


root3.mainloop()

