import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit,
    QVBoxLayout, QHBoxLayout, 
    QPushButton, QCheckBox, QMainWindow
)
from PySide6.QtCore import Qt

class login(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        login_layout = QHBoxLayout()
        main_layout.setContentsMargins(40, 40, 40, 40)
        title = QLabel("LOGIN")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        title.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(title)

        main_layout.addWidget(QLabel("Email"))
        self.email_input = QLineEdit()
        self.email_input.setFixedHeight(40)
        main_layout.addWidget(self.email_input)

        main_layout.addWidget(QLabel("Password"))
        self.pass_input = QLineEdit()
        self.pass_input.setFixedHeight(40)
        main_layout.addWidget(self.pass_input)

        self.mem_checkbox = QCheckBox("Remember me?")
        main_layout.addWidget(self.mem_checkbox)

        self.submit_button = QPushButton("LOGIN")
        self.submit_button.setFixedHeight(40)
        main_layout.addWidget(self.submit_button)
        main_layout.addWidget(QLabel("Forgot Password?", alignment= Qt.AlignRight))

        main_layout.addWidget(QLabel("——————————————[OR]——————————————", alignment= Qt.AlignCenter))

        main_layout.addWidget(QLabel("Need an account? SIGN UP", alignment= Qt.AlignCenter))

        main_layout.addSpacing(20)
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setCentralWidget(login())
    window.setWindowTitle("login page")
    window.setFixedSize(350,450)
    window.show()
    sys.exit(app.exec())
