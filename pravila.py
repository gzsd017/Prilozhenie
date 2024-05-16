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
root2.config(bg='#7FFF00')

btn = ttk.Button(text="<---", command=click_button_nazad)
btn.place(x=250, y=750, anchor="e", width=200, height=25)

label = ttk.Label(root2, text="Правила использования", background='#7FFF00', font=("Arial", 40))
label.place(relx=0.5, rely=0.3, anchor="c")
label.pack()

label1 = ttk.Label(root2, text="Введите уравнение, которое требуется решить, используя предоставленное поле для ввода текста.", background='#7FFF00', font=("Arial", 20))
label1.place(relx=0.5, rely=0.8, anchor="c")
label1.pack()

label2 = ttk.Label(root2, text="После ввода уравнения нажмите на кнопку Решить,", background='#7FFF00', font=("Arial", 20))
label2.place(relx=0.5, rely=0.8, anchor="c")
label2.pack()

label3 = ttk.Label(root2, text="чтобы приложение вычислило корни уравнения и предоставило результат.", background='#7FFF00', font=("Arial", 20))
label3.place(relx=0.5, rely=0.8, anchor="c")
label3.pack()

label4 = ttk.Label(root2, text="Внимательно изучите полученный ответ,", background='#7FFF00', font=("Arial", 20))
label4.place(relx=0.5, rely=0.8, anchor="c")
label4.pack()

label5 = ttk.Label(root2, text="убедитесь в правильности решения и в том, что все корни уравнения были найдены.", background='#7FFF00', font=("Arial", 20))
label5.place(relx=0.5, rely=0.8, anchor="c")
label5.pack()

label6 = ttk.Label(root2, text="Ниже решения вы можете прочитать дополнительные пояснения или шаги решения.", background='#7FFF00', font=("Arial", 20))
label6.place(relx=0.5, rely=0.8, anchor="c")
label6.pack()



root2.mainloop()