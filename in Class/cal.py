import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                             QVBoxLayout, QWidget, QHBoxLayout,
                             QGridLayout, QFormLayout, QLineEdit,
                             QSpinBox, QPushButton, QLabel)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox
from PySide6.QtGui import QFont

class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setStyleSheet("""
            QPushButton {
                min-width: 60px;
                min-height: 40px;
                font-size: 16px;
            }
        """)
        
        # Basic grid positioning
        mode = QComboBox()
        mode.addItems(["≡ Standard", "≡ Scientific", "≡ Graphing", "≡ Programmer"])
        mode.setMinimumHeight(32)
        font = QFont("Arial", 14)
        font.setBold(True)
        mode.setFont(font)
        #dis = QLabel("1 + 1 =")
        #dis.setFont(QFont("Arial", 11))
        #dis.setAlignment(Qt.AlignRight)

        self.current_display = "0"
        self.display = QLabel(self.current_display)
        self.display.setFont(QFont("Arial", 25))
        self.display.setAlignment(Qt.AlignRight)

        # Span across all 4 columns
        layout.addWidget(mode, 0, 0, 1, 2)
        #layout.addWidget(dis, 1, 0, 1, 4)
        layout.addWidget(self.display, 2, 0, 1, 4)
        layout.addWidget(QPushButton("MC"), 3, 0)  # row 0, col 1
        layout.addWidget(QPushButton("MR"), 3, 1)  # row 0, col 2
        layout.addWidget(QPushButton("M+"), 3, 2)
        layout.addWidget(QPushButton("M-"), 3, 3)
        layout.addWidget(QPushButton("%"), 4, 0)
        layout.addWidget(QPushButton("CE"), 4, 1)
        bC = QPushButton("C")
        bC.clicked.connect(self.reset_zero)
        bd = QPushButton("⌫")
        bd.clicked.connect(self.del_last)

        layout.addWidget(bC, 4, 2)
        layout.addWidget(bd, 4, 3)
        layout.addWidget(QPushButton("⅟x"), 5, 0)
        layout.addWidget(QPushButton("x²"), 5, 1)
        layout.addWidget(QPushButton("2√x"), 5, 2)
        layout.addWidget(QPushButton("÷"), 5, 3)

        b0 = QPushButton("0")
        b0.clicked.connect(lambda: self.append_value("0"))
        b1 = QPushButton("1")
        b1.clicked.connect(lambda: self.append_value("1"))
        b2 = QPushButton("2")
        b2.clicked.connect(lambda: self.append_value("2"))
        b3 = QPushButton("3")
        b3.clicked.connect(lambda: self.append_value("3"))
        b4 = QPushButton("4")
        b4.clicked.connect(lambda: self.append_value("4"))
        b5 = QPushButton("5")
        b5.clicked.connect(lambda: self.append_value("5"))
        b6 = QPushButton("6")
        b6.clicked.connect(lambda: self.append_value("6"))
        b7 = QPushButton("7")
        b7.clicked.connect(lambda: self.append_value("7"))
        b8 = QPushButton("8")
        b8.clicked.connect(lambda: self.append_value("8"))
        b9 = QPushButton("9")
        b9.clicked.connect(lambda: self.append_value("9"))

        layout.addWidget(b7, 6, 0)
        layout.addWidget(b8, 6, 1)
        layout.addWidget(b9, 6, 2)
        layout.addWidget(QPushButton("x"), 6, 3)
        layout.addWidget(b4, 7, 0)
        layout.addWidget(b5, 7, 1)
        layout.addWidget(b6, 7, 2)
        layout.addWidget(QPushButton("-"), 7, 3)
        layout.addWidget(b1, 8, 0)
        layout.addWidget(b2, 8, 1)
        layout.addWidget(b3, 8, 2)
        layout.addWidget(QPushButton("+"), 8, 3)
        layout.addWidget(QPushButton("+/-"), 9, 0)
        layout.addWidget(b0, 9, 1)
        layout.addWidget(QPushButton("."), 9, 2)
        layout.addWidget(QPushButton("="), 9, 3)

        # Widget spanning multiple cells 

        # Spacing and margins
        layout.setSpacing(2)
        layout.setContentsMargins(5, 5, 5, 5)

        # Column/Row stretch
        layout.setColumnStretch(0, 0)  # First column stretches more
        layout.setRowStretch(0, 0)     # Second row stretches more

        self.setLayout(layout)
    
    def append_value(self, new_num):
        if self.current_display == "0":
            self.current_display = str(new_num)
        else:
            self.current_display += str(new_num)
        self.display.setText(self.current_display)
    
    def reset_zero(self):
        self.current_display = "0"
        self.display.setText(self.current_display)
    
    def del_last(self):
        if self.current_display != "0":
            self.current_display = self.current_display[:-1]
            self.display.setText(self.current_display)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NOT A CALCULATOR")
        self.setCentralWidget(CalculatorLayout())
        self.resize(300, 520)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())