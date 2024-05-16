from tkinter import *
from tkinter.scrolledtext import ScrolledText
from math import sqrt
from tkinter import ttk
import subprocess
from sympy.solvers import solve
from sympy import Symbol


def reshenie(root, answer):
    root5 = Toplevel(root)
    root5.title("Решение")

    editor = ScrolledText(root5, width=50,  height=10)
    editor.insert(1.0, answer)
    editor.pack()

    root5.mainloop()


# Кнопка "Выход"
def click_button_nazad():
    subprocess.Popen(["python", "menu.py"])
    exit(root4)


def solver(d, e):
    return 'x = %s' % (e / d / -1)


def solver2(a, b, c):
    D = b * b - 4 * a * c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        text = 'D = %s \n x1 = %s \n x2 = %s \n' % (D, x1, x2)
    else:
        text = 'D = %s \n Это уранвение не имеет корней' % D
    return text


def solver3(a, b, c, d):
    x = Symbol('x')
    return solve(a*x ** 3 + b*x**2 + c*x + d, x)


def solver4(a, b, c):
    x = Symbol('x')
    return solve(a*x ** 3 + b*x + c, x)


def solver5(a, b, c, d, e):
    x = Symbol('x')
    return solve(a*x ** 4 + b*x**3 + c*x**2 + d*x + e, x)


def solver6(a, b, c, d):
    x = Symbol('x')
    return solve(a*x ** 4 + b*x**2 + c*x + d, x)


def inserter(value):
    reshenie(root4, value)


def handler(degree):
    if degree == 1:
        try:
            d_val = float(d.get())
            e_val = float(e.get())
            inserter(solver(d_val, e_val))
        except ValueError:
            inserter('Убедитесь, что ввели 2 числа')
    elif degree == 2:
        try:
            a_val = float(a.get())
            b_val = float(b.get())
            c_val = float(c.get())
            inserter(solver2(a_val, b_val, c_val))
        except ValueError:
            inserter('Убедитесь, что ввели 3 числа')
    elif degree == 3:
        try:
            a_val = float(a1.get())
            b_val = float(b1.get())
            c_val = float(c1.get())
            d_val = float(d1.get())
            inserter(solver3(a_val, b_val, c_val, d_val))
        except ValueError:
            inserter('Убедитесь, что ввели 4 числа')
    elif degree == 4:
        try:
            a_val = float(a2.get())
            b_val = float(b2.get())
            c_val = float(c2.get())
            inserter(solver4(a_val, b_val, c_val))
        except ValueError:
            inserter('Убедитесь, что ввели 3 числа')
    elif degree == 5:
        try:
            a_val = float(a3.get())
            b_val = float(b3.get())
            c_val = float(c3.get())
            d_val = float(d3.get())
            e_val = float(e3.get())
            inserter(solver5(a_val, b_val, c_val, d_val, e_val))
        except ValueError:
            inserter('Убедитесь, что ввели 5 чисел')
    elif degree == 6:
        try:
            a_val = float(a4.get())
            b_val = float(b4.get())
            c_val = float(c4.get())
            d_val = float(d4.get())
            inserter(solver6(a_val, b_val, c_val, d_val))
        except ValueError:
            inserter('Убедитесь, что ввели 4 числа')


root4 = Tk()
root4.title('Калькулятор')
root4.geometry('700x500+200+200')
root4.config(bg='#7FFF00')
root4.resizable(width=False, height=False)

btn = ttk.Button(text="<---", command=click_button_nazad)
btn.place(x=70, y=20, anchor="e", width=65, height=25)

f_top = Frame(root4)
f_top2 = Frame(root4)
f_top3 = Frame(root4)
f_top4 = Frame(root4)
f_top5 = Frame(root4)
f_top6 = Frame(root4)
f_top.pack()
f_top2.pack()
f_top3.pack()
f_top4.pack()
f_top5.pack()
f_top6.pack()

#1 степень
d = Entry(f_top, width=5, font='Arial 15')
d.pack(side=LEFT, pady=10, padx=10)

d_lab = Label(f_top, text='x +', font='Arial 15').pack(side=LEFT, pady=10)

e = Entry(f_top, width=5, font='Arial 15')
e.pack(side=LEFT, pady=10)

e_lab = Label(f_top, text='= 0', font='Arial 15').pack(side=LEFT, pady=10)

btn = Button(f_top, text='Решить', font='Arial 12', command=lambda: handler(1)).pack(side=LEFT, pady=10)

#2 степень
a = Entry(f_top2, width=5, font='Arial 15')
a.pack(side=LEFT, pady=10, padx=10)

a_lab = Label(f_top2, text='x^2 +', font='Arial 15').pack(side=LEFT, pady=10)

b = Entry(f_top2, width=5, font='Arial 15')
b.pack(side=LEFT, pady=10)

b_lab = Label(f_top2, text='x +', font='Arial 15').pack(side=LEFT, pady=10)

c = Entry(f_top2, width=5, font='Arial 15')
c.pack(side=LEFT, pady=10)

c_lab = Label(f_top2, text='= 0', font='Arial 15').pack(side=LEFT, pady=10)

btn2 = Button(f_top2, text='Решить', font='Arial 12', command=lambda: handler(2)).pack(side=LEFT, pady=10)



#3 степень (1)
a1 = Entry(f_top3, width=5, font='Arial 15')
a1.pack(side=LEFT, pady=10, padx=10)

a1_lab = Label(f_top3, text='x^3 +', font='Arial 15').pack(side=LEFT, pady=10)

b1 = Entry(f_top3, width=5, font='Arial 15')
b1.pack(side=LEFT, pady=10, padx=10)

b1_lab = Label(f_top3, text='x^2 +', font='Arial 15').pack(side=LEFT, pady=10)

c1 = Entry(f_top3, width=5, font='Arial 15')
c1.pack(side=LEFT, pady=10)

c1_lab = Label(f_top3, text='x +', font='Arial 15').pack(side=LEFT, pady=10)

d1 = Entry(f_top3, width=5, font='Arial 15')
d1.pack(side=LEFT, pady=10)

d1_lab = Label(f_top3, text='= 0', font='Arial 15').pack(side=LEFT, pady=10)

btn3 = Button(f_top3, text='Решить', font='Arial 12', command=lambda: handler(3)).pack(side=LEFT, pady=10)

#3 степень (20
a2 = Entry(f_top4, width=5, font='Arial 15')
a2.pack(side=LEFT, pady=10, padx=10)

a2_lab = Label(f_top4, text='x^3+', font='Arial 15').pack(side=LEFT, pady=10)

b2 = Entry(f_top4, width=5, font='Arial 15')
b2.pack(side=LEFT, pady=10)

b2_lab = Label(f_top4, text='x +', font='Arial 15').pack(side=LEFT, pady=10)

c2 = Entry(f_top4, width=5, font='Arial 15')
c2.pack(side=LEFT, pady=10)

c2_lab = Label(f_top4, text='= 0', font='Arial 15').pack(side=LEFT, pady=10)

btn4 = Button(f_top4, text='Решить', font='Arial 12', command=lambda: handler(4)).pack(side=LEFT, pady=10)


#4 степень (1)
a3 = Entry(f_top5, width=5, font='Arial 15')
a3.pack(side=LEFT, pady=10, padx=10)

a3_lab = Label(f_top5, text='x^4 +', font='Arial 15').pack(side=LEFT, pady=10)

b3 = Entry(f_top5, width=5, font='Arial 15')
b3.pack(side=LEFT, pady=10, padx=10)

b3_lab = Label(f_top5, text='x^3 +', font='Arial 15').pack(side=LEFT, pady=10)

c3 = Entry(f_top5, width=5, font='Arial 15')
c3.pack(side=LEFT, pady=10, padx=10)

c3_lab = Label(f_top5, text='x^2 +', font='Arial 15').pack(side=LEFT, pady=10)

d3 = Entry(f_top5, width=5, font='Arial 15')
d3.pack(side=LEFT, pady=10)

d3_lab = Label(f_top5, text='x +', font='Arial 15').pack(side=LEFT, pady=10)

e3 = Entry(f_top5, width=5, font='Arial 15')
e3.pack(side=LEFT, pady=10)

e3_lab = Label(f_top5, text='= 0', font='Arial 15').pack(side=LEFT, pady=10)

btn5 = Button(f_top5, text='Решить', font='Arial 12', command=lambda: handler(5)).pack(side=LEFT, pady=10)


#4 степень (2)
a4 = Entry(f_top6, width=5, font='Arial 15')
a4.pack(side=LEFT, pady=10, padx=10)

a4_lab = Label(f_top6, text='x^4 +', font='Arial 15').pack(side=LEFT, pady=10)

b4 = Entry(f_top6, width=5, font='Arial 15')
b4.pack(side=LEFT, pady=10, padx=10)

b4_lab = Label(f_top6, text='x^2 +', font='Arial 15').pack(side=LEFT, pady=10)

c4 = Entry(f_top6, width=5, font='Arial 15')
c4.pack(side=LEFT, pady=10, padx=10)

c4_lab = Label(f_top6, text='x +', font='Arial 15').pack(side=LEFT, pady=10)

d4 = Entry(f_top6, width=5, font='Arial 15')
d4.pack(side=LEFT, pady=10)

d4_lab = Label(f_top6, text='= 0', font='Arial 15').pack(side=LEFT, pady=10)

btn6 = Button(f_top6, text='Решить', font='Arial 12', command=lambda: handler(6)).pack(side=LEFT, pady=10)




root4.mainloop()
