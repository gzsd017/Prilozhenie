from sympy import symbols, Eq, solve, sympify
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 580)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        MainWindow.setStyleSheet("color: rgb(0, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 210, 250, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setStyleSheet("color: rgb(93, 171, 255);\n"
                                      "font: 11pt \"Segoe Print\";\n"
                                      "background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 270, 250, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_2.setStyleSheet("color: rgb(93, 171, 255);\n"
                                        "font: 11pt \"Segoe Print\";\n"
                                        "background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_3.setStyleSheet("color: rgb(93, 171, 255);\n"
                                        "font: 11pt \"Segoe Print\";\n"
                                        "background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 110, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(93, 171, 255);\n"
                                 "font: 11pt \"Segoe Print\";\n"
                                 "background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu"))
        self.pushButton.setText(_translate("MainWindow", "Калькулятор"))
        self.pushButton_2.setText(_translate("MainWindow", "Правила"))
        self.pushButton_3.setText(_translate("MainWindow", "Выход"))
        self.label.setText(_translate("MainWindow", " Калькулятор уравнений 1,2,3,4 степени"))


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(450, 580)
        Calculator.setStyleSheet("font: 10pt \"Segoe Script\";\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(12, 40, 428, 80))
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(255, 148, 129);")
        self.pushButton.setObjectName("pushButton")
        self.btnResh = QtWidgets.QPushButton(self.centralwidget)
        self.btnResh.setGeometry(QtCore.QRect(230, 150, 211, 51))
        self.btnResh.setStyleSheet("background-color: rgb(135, 255, 99);")
        self.btnResh.setObjectName("btnResh")
        self.btnNazad = QtWidgets.QPushButton(self.centralwidget)
        self.btnNazad.setGeometry(QtCore.QRect(10, 150, 101, 51))
        self.btnNazad.setObjectName("btnNazad")
        self.btnDel = QtWidgets.QPushButton(self.centralwidget)
        self.btnDel.setGeometry(QtCore.QRect(120, 150, 101, 51))
        self.btnDel.setObjectName("btnDel")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 101, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 210, 101, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 210, 101, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 210, 101, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 270, 101, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(120, 270, 101, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(230, 270, 101, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(340, 270, 101, 51))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 330, 101, 51))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(120, 330, 101, 51))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(230, 330, 101, 51))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(340, 330, 101, 111))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(10, 390, 101, 51))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(120, 390, 101, 51))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(230, 390, 101, 51))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 450, 101, 51))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(120, 450, 101, 51))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(230, 450, 101, 51))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(340, 450, 101, 51))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(10, 510, 211, 51))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(230, 510, 101, 51))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(340, 510, 101, 51))
        self.pushButton_24.setObjectName("pushButton_24")
        Calculator.setCentralWidget(self.centralwidget)

        self.add_functions()

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.pushButton.setText(_translate("Calculator", "Назад"))
        self.btnResh.setText(_translate("Calculator", "Решить"))
        self.btnNazad.setText(_translate("Calculator", "C"))
        self.btnDel.setText(_translate("Calculator", "<---"))
        self.pushButton_2.setText(_translate("Calculator", "("))
        self.pushButton_3.setText(_translate("Calculator", ")"))
        self.pushButton_4.setText(_translate("Calculator", "x"))
        self.pushButton_5.setText(_translate("Calculator", "^"))
        self.pushButton_6.setText(_translate("Calculator", "+"))
        self.pushButton_7.setText(_translate("Calculator", "-"))
        self.pushButton_8.setText(_translate("Calculator", "*"))
        self.pushButton_9.setText(_translate("Calculator", ":"))
        self.pushButton_10.setText(_translate("Calculator", "7"))
        self.pushButton_11.setText(_translate("Calculator", "8"))
        self.pushButton_12.setText(_translate("Calculator", "9"))
        self.pushButton_13.setText(_translate("Calculator", "="))
        self.pushButton_14.setText(_translate("Calculator", "4"))
        self.pushButton_15.setText(_translate("Calculator", "5"))
        self.pushButton_16.setText(_translate("Calculator", "6"))
        self.pushButton_17.setText(_translate("Calculator", "1"))
        self.pushButton_18.setText(_translate("Calculator", "2"))
        self.pushButton_19.setText(_translate("Calculator", "3"))
        self.pushButton_20.setText(_translate("Calculator", "/"))
        self.pushButton_21.setText(_translate("Calculator", "0"))
        self.pushButton_23.setText(_translate("Calculator", "."))
        self.pushButton_24.setText(_translate("Calculator", ","))

    def add_functions(self):
        buttons = [
            self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5,
            self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9,
            self.pushButton_10, self.pushButton_11, self.pushButton_12, self.pushButton_13,
            self.pushButton_14, self.pushButton_15, self.pushButton_16, self.pushButton_17,
            self.pushButton_18, self.pushButton_19, self.pushButton_20, self.pushButton_21,
            self.pushButton_23, self.pushButton_24
        ]

        for btn in buttons:
            btn.clicked.connect(lambda ch, btn=btn: self.write_number(btn.text()))

        self.btnNazad.clicked.connect(self.lineEdit.clear)
        self.btnDel.clicked.connect(self.lineEdit.backspace)

    def write_number(self, number):
        current_line = self.lineEdit.text()
        new_line = current_line + str(number)
        self.lineEdit.setText(new_line)


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 580)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font: 10pt \"Segoe Script\";")
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 430, 500))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.textEdit.setPlainText(
            "Правила использования:\n"
            "1. Введите уравнение для решения в текстовое поле.\n"
            "2. Используйте кнопки на калькуляторе для ввода коэффициентов и операций.\n"
            "3. Нажмите кнопку 'Решить', чтобы получить решение.\n"
            "4. Кнопка 'C' очищает текущее уравнение.\n"
            "5. Кнопка '<---' удаляет последний введенный символ.\n"
            "6. Используйте '+' для сложения, '-' для вычитания, '*' для умножения и ':' для деления.\n"
            "7. Кнопка '^' используется для возведения в степень.\n"
        )
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 550, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(99, 193, 255);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rules"))
        self.pushButton.setText(_translate("MainWindow", "Назад"))

class Ui_ResultWindow(object):
    def setupUi(self, ResultWindow):
        ResultWindow.setObjectName("ResultWindow")
        ResultWindow.resize(450, 580)
        self.centralwidget = QtWidgets.QWidget(ResultWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("font: 10pt \"Segoe Script\";")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 430, 500))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 520, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(99, 193, 255);")
        self.pushButton.setObjectName("pushButton")
        ResultWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ResultWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultWindow)

    def retranslateUi(self, ResultWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultWindow.setWindowTitle(_translate("ResultWindow", "Reshenie"))
        self.pushButton.setText(_translate("ResultWindow", "Назад"))

class ResultWindow(QtWidgets.QMainWindow):
    def __init__(self, result_text):
        super().__init__()
        self.ui = Ui_ResultWindow()
        self.ui.setupUi(self)
        self.ui.textEdit.setPlainText(result_text)
        self.ui.pushButton.clicked.connect(self.close)


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = Ui_MainWindow()
        self.calculator = Ui_Calculator()
        self.rules_window = Ui_MainWindow2()
        self.main_window.setupUi(self)

        self.main_window.pushButton.clicked.connect(self.show_calculator)
        self.main_window.pushButton_2.clicked.connect(self.show_rules)
        self.main_window.pushButton_3.clicked.connect(self.close)

        self.calculator_window = None
        self.rules_window_window = None
        self.result_window = None

    def show_calculator(self):
        if self.calculator_window:
            self.calculator_window.close()
        self.calculator_window = QtWidgets.QMainWindow()
        self.calculator.setupUi(self.calculator_window)
        self.calculator.btnResh.clicked.connect(self.calculate)
        self.calculator.pushButton.clicked.connect(self.return_to_main)
        self.calculator_window.show()
        self.close()

    def show_rules(self):
        if self.rules_window_window:
            self.rules_window_window.close()
        self.rules_window_window = QtWidgets.QMainWindow()
        self.rules_window.setupUi(self.rules_window_window)
        self.rules_window.pushButton.clicked.connect(self.return_to_main)
        self.rules_window_window.show()
        self.close()

    def return_to_main(self):
        if self.calculator_window:
            self.calculator_window.close()
        if self.rules_window_window:
            self.rules_window_window.close()

        self.show()

    def calculate(self):
        equation = self.calculator.lineEdit.text().strip()
        x = symbols('x')

        try:
            if '=' not in equation:
                raise ValueError("Уравнение должно содержать знак '='.")

            left, right = equation.split('=')

            left_expr = sympify(left.replace('^', '**'))
            right_expr = sympify(right)

            steps = "Решение уравнения:\n"
            steps += f"1. Исходное уравнение: {equation}\n"

            steps += "2. Переносим все члены в одну часть уравнения:\n"
            combined_expr = left_expr - right_expr
            steps += f"   {combined_expr} = 0\n"

            steps += "3. Упрощаем уравнение:\n"
            simplified_expr = combined_expr.simplify()
            steps += f"   {simplified_expr} = 0\n"

            steps += "4. Решаем уравнение, находя значения x, которые обращают уравнение в ноль:\n"
            roots = solve(simplified_expr, x)
            if roots:
                for i, root in enumerate(roots, start=1):
                    steps += f"   Корень {i}: x = {root}\n"
            else:
                steps += "   Нет решений.\n"

            result = steps

        except Exception as e:
            result = f"Ошибка: {str(e)}"

        self.result_window = ResultWindow(result)
        self.result_window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())




