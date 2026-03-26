import sys, os
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit,
    QVBoxLayout, QHBoxLayout, 
    QPushButton, QCheckBox, QMainWindow
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QFont

class login(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
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

        #img
        img_layout = QHBoxLayout()
        img_layout.setSpacing(25)
        img_layout.setAlignment(Qt.AlignCenter)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        for img_name in ["gg.png", "face.png", "in.png"]:
            label = QLabel()
            path = os.path.join(current_dir, "img", img_name)
            pixmap = QPixmap(path)

            if not pixmap.isNull():
                label.setPixmap(pixmap.scaled(
                    28, 28,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                ))

            img_layout.addWidget(label)

        main_layout.addLayout(img_layout)
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
