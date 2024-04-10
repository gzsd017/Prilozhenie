import tkinter as tk
from tkinter import ttk
from math import *

def click_button_nazad():
    exit(root)

convert_constant = 1
inverse_convert_constant = 1

btn_params = {
    'padx': 40,
    'pady': 1,
    'bd': 4,
    'fg': 'black',
    'bg': '#666666',
    'font': ('TimesNewRoman', 18),
    'width': 3,
    'height': 3,
    'relief': 'raised',
    'activebackground': "#6D6D6D"
}


class Calculator:
    def __init__(self, master):
        self.expression = ""
        self.recall = ""
        self.sum_up = ""
        self.text_input = tk.StringVar()
        self.master = master
        top_frame = tk.Frame(master, width=650, height=20, bd=4, relief='flat', bg='#6D6D6D')
        top_frame.pack(side=tk.TOP)
        bottom_frame = tk.Frame(master, width=100, height=100, bd=4, relief='flat', bg='#6D6D6D')
        bottom_frame.pack(side=tk.BOTTOM)
        my_item = tk.Label(top_frame, text="Калькулятор",
                           font=('arial', 20), fg='black', width=26, bg='#6D6D6D')
        my_item.pack()
        txt_display = tk.Entry(top_frame, font=('arial', 36), relief='raised',
                               bg='#6D6D6D', fg='black', textvariable=self.text_input, width=23, bd=28, justify='right')
        txt_display.pack()

        self.btn_left_brack = tk.Button(bottom_frame, **btn_params, text="(", command=lambda: self.btn_click('('))
        self.btn_left_brack.grid(row=0, column=4)
        self.btn_right_brack = tk.Button(bottom_frame, **btn_params, text=")", command=lambda: self.btn_click(')'))
        self.btn_right_brack.grid(row=0, column=5)
        self.btn_clear = tk.Button(bottom_frame, **btn_params, text="C", command=self.btn_clear_all)
        self.btn_clear.grid(row=0, column=6)
        self.btn_del = tk.Button(bottom_frame, **btn_params, text="⌫", command=self.btn_clear1)
        self.btn_del.grid(row=0, column=7)
        self.btn_div = tk.Button(bottom_frame, **btn_params, text="/", command=lambda: self.btn_click('/'))
        self.btn_div.grid(row=0, column=3)
        self.cube = tk.Button(bottom_frame, **btn_params, text=u"x\u00B3", command=lambda: self.btn_click('**3'))
        self.cube.grid(row=2, column=3)
        self.cube = tk.Button(bottom_frame, **btn_params, text=u"x\u00B4", command=lambda: self.btn_click('**4'))
        self.cube.grid(row=1, column=3)
        self.btn_7 = tk.Button(bottom_frame, **btn_params, text="7", command=lambda: self.btn_click(7))
        self.btn_7.configure(activebackground="#666666", bg='#666666')
        self.btn_7.grid(row=1, column=4)
        self.btn_8 = tk.Button(bottom_frame, **btn_params, text="8", command=lambda: self.btn_click(8))
        self.btn_8.configure(activebackground="#666666", bg='#666666')
        self.btn_8.grid(row=1, column=5)
        self.btn_9 = tk.Button(bottom_frame, **btn_params, text="9", command=lambda: self.btn_click(9))
        self.btn_9.configure(activebackground="#666666", bg='#666666')
        self.btn_9.grid(row=1, column=6)
        self.btn_mult = tk.Button(bottom_frame, **btn_params, text="x", command=lambda: self.btn_click('*'))
        self.btn_mult.grid(row=4, column=3)
        self.btn_4 = tk.Button(bottom_frame, **btn_params, text="4", command=lambda: self.btn_click(4))
        self.btn_4.configure(activebackground="#666666", bg='#666666')
        self.btn_4.grid(row=2, column=4)
        self.btn_5 = tk.Button(bottom_frame, **btn_params, text="5", command=lambda: self.btn_click(5))
        self.btn_5.configure(activebackground="#666666", bg='#666666')
        self.btn_5.grid(row=2, column=5)
        self.btn_6 = tk.Button(bottom_frame, **btn_params, text="6", command=lambda: self.btn_click(6))
        self.btn_6.configure(activebackground="#666666", bg='#666666')
        self.btn_6.grid(row=2, column=6)
        self.btnSub = tk.Button(bottom_frame, **btn_params, text="-", command=lambda: self.btn_click('-'))
        self.btnSub.grid(row=1, column=7)
        self.btn_1 = tk.Button(bottom_frame, **btn_params, text="1", command=lambda: self.btn_click(1))
        self.btn_1.configure(activebackground="#666666", bg='#666666')
        self.btn_1.grid(row=3, column=4)
        self.btn_2 = tk.Button(bottom_frame, **btn_params, text="2", command=lambda: self.btn_click(2))
        self.btn_2.configure(activebackground="#666666", bg='#666666')
        self.btn_2.grid(row=3, column=5)
        self.btn_3 = tk.Button(bottom_frame, **btn_params, text="3", command=lambda: self.btn_click(3))
        self.btn_3.configure(activebackground="#666666", bg='#666666')
        self.btn_3.grid(row=3, column=6)
        self.btn_add = tk.Button(bottom_frame, **btn_params, text="+", command=lambda: self.btn_click('+'))
        self.btn_add.grid(row=2, column=7)
        self.btn_sqr = tk.Button(bottom_frame, **btn_params, text=u"x\u00B2", command=lambda: self.btn_click('**2'))
        self.btn_sqr.grid(row=3, column=3)
        self.btn_0 = tk.Button(bottom_frame, **btn_params, text="0", command=lambda: self.btn_click(0))
        self.btn_0.configure(activebackground="#666666", bg='#666666', width=7, bd=5)
        self.btn_0.grid(row=4, column=4, columnspan=2)
        self.btn_eq = tk.Button(bottom_frame, **btn_params, text="=", command=self.btn_equal)
        self.btn_eq.configure(bg='#FF5C00', activebackground='#FF5C00')
        self.btn_eq.grid(row=4, column=6)
        self.btn_dec = tk.Button(bottom_frame, **btn_params, text=".", command=lambda: self.btn_click('.'))
        self.btn_dec.grid(row=4, column=7)
        self.btn_comma = tk.Button(bottom_frame, **btn_params, text=",", command=lambda: self.btn_click(','))
        self.btn_comma.grid(row=3, column=7)


    def btn_click(self, expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.text_input.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)

    def btn_clear1(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)

    def change_signs(self):
        self.expression = self.expression + '-'
        self.text_input.set(self.expression)

    def memory_clear(self):
        self.recall = ""

    def memory_add(self):
        self.recall = self.recall + '+' + self.expression

    def answer(self):
        self.answer = self.sum_up
        self.expression = self.expression + self.answer
        self.text_input.set(self.expression)

    def memory_recall(self):
        if self.expression == "":
            self.text_input.set('0' + self.expression + self.recall)
        else:
            self.text_input.set(self.expression + self.recall)


    def btn_clear_all(self):
        self.expression = ""
        self.text_input.set("")

    def btn_equal(self):
        self.sum_up = str(eval(self.expression))
        self.text_input.set(self.sum_up)
        self.expression = self.sum_up


root = tk.Tk()
b = Calculator(root)
root.title("Калькулятор")
root.geometry("1000x690")
root.resizable(False, False)

btn = ttk.Button(text="Выход", command=click_button_nazad)
btn.place(x=250, y=750, anchor="e", width=200, height=25)

root.mainloop()