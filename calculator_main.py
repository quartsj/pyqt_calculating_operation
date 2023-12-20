import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit, QLabel

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        layout_operation = QHBoxLayout()
        layout_clear_equal = QHBoxLayout()
        layout_number = QGridLayout()

        self.equation_line_edit = QLineEdit("")
        self.equation_line_edit.setReadOnly(True)
        self.equation_line_edit.setAlignment(Qt.AlignRight)  # You may need to import Qt from PyQt5.QtCore
        self.equation_line_edit.setMaxLength(15)

        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        button_plus.clicked.connect(lambda state, operation="+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation="-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation="*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation="/": self.button_operation_clicked(operation))

        layout_operation.addWidget(button_plus)
        layout_operation.addWidget(button_minus)
        layout_operation.addWidget(button_product)
        layout_operation.addWidget(button_division)

        button_equal = QPushButton("=")
        button_clear = QPushButton("Clear")
        button_backspace = QPushButton("Backspace")

        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        layout_clear_equal.addWidget(button_clear)
        layout_clear_equal.addWidget(button_backspace)
        layout_clear_equal.addWidget(button_equal)

        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num=number: self.number_button_clicked(num))
            if number > 0:
                x, y = divmod(number - 1, 3)
                layout_number.addWidget(number_button_dict[number], x, y)
            elif number == 0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num=".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num="00": self.number_button_clicked(num))
        layout_number.addWidget(button_double_zero, 3, 0)

        main_layout.addWidget(self.equation_line_edit)
        main_layout.addLayout(layout_operation)
        main_layout.addLayout(layout_clear_equal)
        main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        self.show()

    def number_button_clicked(self, num):
        equation = self.equation_line_edit.text()
        equation += str(num)
        self.equation_line_edit.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation_line_edit.text()
        equation += operation
        self.equation_line_edit.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation_line_edit.text()
        try:
            solution = eval(equation)
            self.equation_line_edit.setText(str(solution))
        except Exception as e:
            self.equation_line_edit.setText('Error')

    def button_clear_clicked(self):
        self.equation_line_edit.clear()

    def button_backspace_clicked(self):
        equation = self.equation_line_edit.text()
        equation = equation[:-1]
        self.equation_line_edit.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
