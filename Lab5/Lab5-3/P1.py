import sys, os
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QComboBox, QMainWindow, QTableWidget,
    QTableWidgetItem, QMessageBox, QSpinBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

class Grade_Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grade Calculator")
        self.setFixedSize(780, 550)

        #——————————Create Central Widget——————————#
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        self.setLayout(main_layout)

        #——————————————————Title——————————————————#
        title = QLabel("Student Grade Calculator")
        title.setAlignment(Qt.AlignCenter)
        title.setFixedHeight(40)
        title.setStyleSheet("""
            background-color: #6f969b;
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 6px;
            border-radius: 15px;
        """)
        main_layout.addWidget(title)
        main_layout.addSpacing(10)

        #—————————————————id input—————————————————#
        id_input_layout = QHBoxLayout()
        id_input_layout.addStretch()

        #---ID---
        id_input_layout.addWidget(QLabel("Student ID: "))
        self.id = QComboBox()
        self.id.setPlaceholderText("Select Student ID")

        #---read file to combo box---
        self.student_map = {}
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "students.txt")
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    student_id, student_name = line.split(",", 1)
                    self.student_map[student_id] = student_name
                    self.id.addItem(student_id)
        id_input_layout.addWidget(self.id)

        #---Name---
        id_input_layout.addWidget(QLabel("Student Name: "))

        self.name = QLineEdit()
        self.name.setReadOnly(True)
        self.name.setFixedWidth(250)
        self.id.currentTextChanged.connect(self.update_student_name)
        
        id_input_layout.addWidget(self.name)
        id_input_layout.addStretch()

        main_layout.addLayout(id_input_layout)
        main_layout.addSpacing(10)
        
        #—————————————————score input—————————————————#
        score_input_layout = QHBoxLayout()
        score_input_layout.addStretch()

        #---Math---
        score_input_layout.addWidget(QLabel("Math:"))
        self.math = QSpinBox()
        self.math.setRange(0, 100)
        score_input_layout.addWidget(self.math)
        score_input_layout.addSpacing(25)

        #---Science---
        score_input_layout.addWidget(QLabel("Science:"))
        self.sci = QSpinBox()
        self.sci.setRange(0, 100)
        score_input_layout.addWidget(self.sci)
        score_input_layout.addSpacing(25)

        #---English---
        score_input_layout.addWidget(QLabel("English:"))
        self.eng = QSpinBox()
        self.eng.setRange(0, 100)
        score_input_layout.addWidget(self.eng)
        score_input_layout.addStretch()

        main_layout.addLayout(score_input_layout)
        main_layout.addSpacing(10)

        #—————————————————button—————————————————#

        #---Add Student---
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Student")
        self.add_button.setFixedSize(600, 63)
        self.add_button.setStyleSheet("""
            QPushButton {
                    background-color: #6f969b;
                    color: white;
                    font-size: 20px;
                    font-weight: bold;
                    padding: 6px;
                    border-radius: 18px;
                }
                QPushButton:hover {
                    background-color: #65898d;
                }
                QPushButton:pressed {
                    background-color: #4a6467;
                }
            """)
        button_layout.addWidget(self.add_button)
        self.add_button.clicked.connect(self.add_student)

        #---reset & clear---
        re_cle_button_layout = QVBoxLayout()

        self.re_button = QPushButton("Reset Input")
        re_cle_button_layout.addWidget(self.re_button)
        self.re_button.setFixedHeight(30)
        self.re_button.setStyleSheet("""
            QPushButton {
                    background-color: #6f969b;
                    color: white;
                    font-size: 13px;
                    padding: 6px;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #65898d;
                }
                QPushButton:pressed {
                    background-color: #4a6467;
                }
            """)
        self.re_button.clicked.connect(self.reset_input)

        re_cle_button_layout.addSpacing(-3)

        self.cle_button = QPushButton("Clear All")
        re_cle_button_layout.addWidget(self.cle_button)
        self.cle_button.setFixedHeight(30)
        self.cle_button.setStyleSheet("""
            QPushButton {
                    background-color: #6f969b;
                    color: white;
                    font-size: 13px;
                    padding: 6px;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #65898d;
                }
                QPushButton:pressed {
                    background-color: #4a6467;
                }
            """)
        self.cle_button.clicked.connect(self.clear_all)

        button_layout.addLayout(re_cle_button_layout)

        main_layout.addLayout(button_layout)
        main_layout.addSpacing(10)

        #—————————————————Table—————————————————#
        self.table = QTableWidget()
        #self.table.setFixedWidth(760)
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["Student ID", "Name", "Math", 
                                              "Science", "English", "Total", 
                                              "Average", "Grade"])
        
        self.table.horizontalHeader().setStretchLastSection
        self.table.setColumnWidth(0, 120) # id
        self.table.setColumnWidth(1, 200) # name
        self.table.setColumnWidth(2, 70) # math
        self.table.setColumnWidth(3, 70) # sci
        self.table.setColumnWidth(4, 70) # eng
        self.table.setColumnWidth(5, 70) # total
        self.table.setColumnWidth(6, 70) # avg
        self.table.setColumnWidth(7, 80) # grade
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        main_layout.addWidget(self.table)
#======================================================================

    #—————————————————Logic—————————————————#
    def update_student_name(self, student_id):
        """Update student name according to the student ID"""
        self.name.setText(self.student_map.get(student_id, ""))
    
    def add_student(self):
        """add the student to the table and calculate score"""
        id = self.id.currentText()
        name = self.name.text()
        math = self.math.value()
        sci = self.sci.value()
        eng = self.eng.value()

        #---validate input---
        if not id:
            QMessageBox.warning(self, "Input Error", "Please enter student ID!.")
            return
        
        #---add new row---
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        #---logic---
        total = (math + sci + eng)

        avg = total/3

        if avg >= 80:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        elif avg >= 50:
            grade = "D"
        else:
            grade = "F"

        #---add items---
        id_item = QTableWidgetItem(id)
        name_item = QTableWidgetItem(name)
        math_item = QTableWidgetItem(str(math))
        sci_item = QTableWidgetItem(str(sci))
        eng_item = QTableWidgetItem(str(eng)) 
        total_item = QTableWidgetItem(str(total))
        avg_item = QTableWidgetItem(str(f"{avg:.2f}"))
        grade_item = QTableWidgetItem(grade)

        #---colors---
        self.set_score_color(math_item, math)
        self.set_score_color(sci_item, sci)
        self.set_score_color(eng_item, eng)
        self.set_grade_color(grade_item, grade)

        #---set items---
        self.table.setItem(row_position, 0, id_item)
        self.table.setItem(row_position, 1, name_item)
        self.table.setItem(row_position, 2, math_item)
        self.table.setItem(row_position, 3, sci_item)
        self.table.setItem(row_position, 4, eng_item)
        self.table.setItem(row_position, 5, total_item)
        self.table.setItem(row_position, 6, avg_item)
        self.table.setItem(row_position, 7, grade_item)

        self.table.sortItems(0, Qt.AscendingOrder)

        self.id.setCurrentIndex(-1)
        self.name.clear()
        self.math.setValue(0)
        self.sci.setValue(0)
        self.eng.setValue(0)

    def set_score_color(self, item, score):
        if score >= 80:
            item.setBackground(QColor("#40bd40"))
        elif score >= 70:
            item.setBackground(QColor("#AFC81B"))
        elif score >= 60:
            item.setBackground(QColor("#FFD000"))
        elif score >= 50:
            item.setBackground(QColor("#E08913"))
        else:
            item.setBackground(QColor("#B62C2C"))

    def set_grade_color(self, item, grade):
        if grade == "A":
            color = "#40bd40"
        elif grade == "B":
            color = "#AFC81B"
        elif grade == "C":
            color = "#FFD000"
        elif grade == "D":
            color = "#E08913"
        elif grade == "F":
            color = "#B62C2C"
        else:
            return

        item.setBackground(QColor(color))

    def reset_input(self):
        """Clear all input fields"""
        self.id.setCurrentIndex(-1)
        self.name.clear()
        self.math.setValue(0)
        self.sci.setValue(0)
        self.eng.setValue(0)

    def clear_all(self):
        """Remove all entries"""
        self.table.setRowCount(0)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Grade_Calculator()
    window.show()
    sys.exit(app.exec())
