import sys
import math
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout, QPushButton, QLabel
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.current_display = "0"

        self.setStyleSheet("""
            QPushButton {
                min-width: 60px;
                min-height: 40px;
                font-size: 18px;
            }
        """)

        layout = QGridLayout()

        # Mode label
        mode = QLabel("≡ Standard")
        mode.setFont(QFont("Arial", 14, QFont.Bold))

        # Display
        self.display = QLabel(self.current_display)
        self.display.setFont(QFont("Arial", 38, QFont.Bold))
        self.display.setAlignment(Qt.AlignRight)

        layout.addWidget(mode, 0, 0, 1, 2)
        layout.addWidget(self.display, 1, 0, 1, 4)

        # Row 1
        layout.addWidget(self.make_op_button("%"), 2, 0)
        layout.addWidget(self.make_button("CE", self.reset_zero), 2, 1)
        layout.addWidget(self.make_button("C", self.reset_zero), 2, 2)
        layout.addWidget(self.make_button("⌫", self.del_last), 2, 3)

        # Row 2
        layout.addWidget(self.make_button("1/x", self.reciprocal), 3, 0)
        layout.addWidget(self.make_button("x²", self.square), 3, 1)
        layout.addWidget(self.make_button("√x", self.sqrt), 3, 2)
        layout.addWidget(self.make_op_button("/"), 3, 3)

        # Numbers
        nums = [
            ("7", 4, 0), ("8", 4, 1), ("9", 4, 2),
            ("4", 5, 0), ("5", 5, 1), ("6", 5, 2),
            ("1", 6, 0), ("2", 6, 1), ("3", 6, 2),
        ]

        for n, r, c in nums:
            layout.addWidget(self.make_num_button(n), r, c)

        layout.addWidget(self.make_op_button("*"), 4, 3)
        layout.addWidget(self.make_op_button("-"), 5, 3)
        layout.addWidget(self.make_op_button("+"), 6, 3)

        # Last row
        layout.addWidget(self.make_button("+/-", self.negate), 7, 0)
        layout.addWidget(self.make_num_button("0"), 7, 1)
        layout.addWidget(self.make_op_button("."), 7, 2)
        layout.addWidget(self.make_button("=", self.calculate), 7, 3)

        layout.setSpacing(2)
        layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(layout)

    # ---------- Button helpers ----------
    def make_num_button(self, text):
        btn = QPushButton(text)
        btn.clicked.connect(lambda _, v=text: self.append_value(v))
        return btn

    def make_op_button(self, op):
        btn = QPushButton(op)
        btn.clicked.connect(lambda _, v=op: self.append_operator(v))
        return btn

    def make_button(self, text, func):
        btn = QPushButton(text)
        btn.clicked.connect(func)
        return btn

    # ---------- Logic ----------
    def append_value(self, val):
        if self.current_display == "0":
            self.current_display = val
        else:
            self.current_display += val
        self.display.setText(self.current_display)

    def append_operator(self, op):
        self.current_display += op
        self.display.setText(self.current_display)

    def reset_zero(self):
        self.current_display = "0"
        self.display.setText(self.current_display)

    def del_last(self):
        if len(self.current_display) == 1:
            self.current_display = "0"
        else:
            self.current_display = self.current_display[:-1]
        self.display.setText(self.current_display)

    def calculate(self):
        try:
            result = eval(self.current_display)
            self.current_display = str(result)
        except Exception:
            self.current_display = "Error"
        self.display.setText(self.current_display)

    def reciprocal(self):
        try:
            x = float(self.current_display)
            self.current_display = str(1 / x)
        except Exception:
            self.current_display = "Error"
        self.display.setText(self.current_display)

    def square(self):
        try:
            x = float(self.current_display)
            self.current_display = str(x ** 2)
        except Exception:
            self.current_display = "Error"
        self.display.setText(self.current_display)

    def sqrt(self):
        try:
            x = float(self.current_display)
            self.current_display = str(math.sqrt(x))
        except Exception:
            self.current_display = "Error"
        self.display.setText(self.current_display)

    def negate(self):
        try:
            x = float(self.current_display)
            self.current_display = str(-x)
        except Exception:
            self.current_display = "Error"
        self.display.setText(self.current_display)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setCentralWidget(CalculatorLayout())
        self.resize(320, 470)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
