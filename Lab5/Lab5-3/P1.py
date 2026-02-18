import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QComboBox, QMainWindow, QTableWidget,
    QTableWidgetItem, QFormLayout, QMessageBox, QSpinBox
)
from PySide6.QtCore import Qt

class Grade_Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grade Calculator")
        self.setGeometry(100, 100, 750, 550)

        #-----------Create Central Widget-----------
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        self.setLayout(main_layout)

        #-----------------Title-----------------
        title = QLabel("Student Grade Calculator")
        title.setAlignment(Qt.AlignCenter)
        title.setFixedHeight(35)
        title.setStyleSheet("""
            background-color: #6f969b;
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 6px;
            border-radius: 15px;
        """)
        main_layout.addWidget(title)

        #-----------------id input-----------------
        id_input__layout = QHBoxLayout()

        #ID
        id_input__layout.addWidget(QLabel("Student ID: "))
        self.studentID = QComboBox()
        #read file to combo box
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                name = line.strip()
                if name:
                    self.studentID.addItem(name)
        self.studentID.setPlaceholderText("Select Student ID")
        id_input__layout.addWidget(self.studentID)

        #Name

        main_layout.addLayout(id_input__layout)
        #-----------------score input-----------------

        #Math

        #Science

        #English

        #-----------------button-----------------



        #-----------------Table-----------------
        
        

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Grade_Calculator()
    window.show()
    sys.exit(app.exec())
