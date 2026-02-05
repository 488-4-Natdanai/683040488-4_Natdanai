import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit,
    QVBoxLayout, QHBoxLayout, QComboBox, QRadioButton,
    QButtonGroup, QPushButton, QCheckBox, QDateEdit, QMainWindow
)
from PySide6.QtCore import QDate, Qt

class StudentRegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Registration")
        self.setFixedSize(400, 600)

        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        title = QLabel("Student Registration Form")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        main_layout.addWidget(QLabel("Full Name:"))
        self.name_input = QLineEdit()
        main_layout.addWidget(self.name_input)

        main_layout.addWidget(QLabel("Email:"))
        self.email_input = QLineEdit()
        main_layout.addWidget(self.email_input)

        main_layout.addWidget(QLabel("Phone:"))
        self.phone_input = QLineEdit()
        main_layout.addWidget(self.phone_input)

        main_layout.addWidget(QLabel("Date of Birth:"))
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("M/dd/yy")
        self.date_edit.setDate(QDate(2000, 1, 1))
        main_layout.addWidget(self.date_edit)

        main_layout.addWidget(QLabel("Gender:"))
        gender_layout = QHBoxLayout()

        self.gender_group = QButtonGroup()

        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        self.non_binary_radio = QRadioButton("Non-binary")
        self.prefer_not_radio = QRadioButton("Prefer not to say")

        self.gender_group.addButton(self.male_radio)
        self.gender_group.addButton(self.female_radio)
        self.gender_group.addButton(self.non_binary_radio)
        self.gender_group.addButton(self.prefer_not_radio)

        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        gender_layout.addWidget(self.non_binary_radio)
        gender_layout.addWidget(self.prefer_not_radio)

        main_layout.addLayout(gender_layout)

        main_layout.addWidget(QLabel("Program:"))
        self.program_combo = QComboBox()
        self.program_combo.setPlaceholderText("Select your program")
        self.program_combo.addItems([
            "Computer Engineering",
            "Digital Media Engineering",
            "Environmental Engineering",
            "Electical Engineering",
            "Semiconductor Engineering",
            "Mechanical Engineering",
            "Industrial Engineering",
            "Logistic Engineering",
            "Power Engineering",
            "Electronic Engineering",
            "Telecommunication Engineering",
            "Agricultural Engineering",
            "Civil Engineering",
            "ARIS"
        ])
        main_layout.addWidget(self.program_combo)

        main_layout.addWidget(QLabel("Tell us a little bit about yourself:"))
        self.about_text = QTextEdit()
        self.about_text.setMaximumHeight(100)
        main_layout.addWidget(self.about_text)

        self.terms_checkbox = QCheckBox("I accept the terms and conditions.")
        main_layout.addWidget(self.terms_checkbox)

        self.submit_button = QPushButton("Submit Registration")
        self.submit_button.setFixedWidth(150)

        button_layout.addWidget(self.submit_button)
        button_layout.setAlignment(Qt.AlignCenter)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setCentralWidget(StudentRegistrationForm())
    window.show()
    sys.exit(app.exec())
