import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QComboBox, QGroupBox, QGridLayout,
    QMainWindow, QTableWidget, QTableWidgetItem
)
from PySide6.QtCore import Qt


class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(12)

        # -------------------------
        # Title
        # -------------------------
        title = QLabel("Adult and Child BMI Calculator")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            background-color: #b54a38;
            color: white;
            font-weight: bold;
            padding: 6px;
            border-radius: 4px;
        """)
        main_layout.addWidget(title)

        # -------------------------
        # Form Section
        # -------------------------
        
        age_layout = QHBoxLayout()
        age_layout.setAlignment(Qt.AlignCenter)
        # Age group
        age_layout.addWidget(QLabel("Calculate BMI for"))

        self.age_combo = QComboBox()
        self.age_combo.addItems([
            "Adult Age 20+",
            "Child (2 - 19)"
        ])
        age_layout.addWidget(self.age_combo)

        form_layout = QGridLayout()
        form_layout.setContentsMargins(35, 0, 35, 10)
        # Weight
        form_layout.addWidget(QLabel("Weight:"), 1, 0)

        self.weight_input = QLineEdit()
        self.weight_input.setFixedWidth(80)
        form_layout.addWidget(self.weight_input, 1, 1)

        self.weight_unit = QComboBox()
        self.weight_unit.addItems([
            "kilograms",
            "pounds"
        ])
        form_layout.addWidget(self.weight_unit, 1, 2)

        # Height (feet + inches OR meters)
        form_layout.addWidget(QLabel("Height:"), 2, 0)

        self.height_input = QLineEdit()
        self.height_input.setFixedWidth(80)
        form_layout.addWidget(self.height_input, 2, 1)

        self.height_unit = QComboBox()
        self.height_unit.addItems([
            "meters",
            "centimeters",
            "feet"
        ])
        form_layout.addWidget(self.height_unit, 2, 2)

        # Inches input (used if feet selected)
        self.inches_input = QLineEdit()
        self.inches_input.setFixedWidth(80)
        form_layout.addWidget(self.inches_input, 3, 1)

        inches_label = QLabel("inches")
        form_layout.addWidget(inches_label, 3, 2)
        main_layout.addLayout(age_layout)
        main_layout.addLayout(form_layout)

        # -------------------------
        # Buttons
        # -------------------------
        button_layout = QHBoxLayout()

        self.clear_button = QPushButton("Clear")
        self.calculate_button = QPushButton("Calculate")

        button_layout.addWidget(self.clear_button)
        button_layout.addStretch()
        button_layout.addWidget(self.calculate_button)

        main_layout.addLayout(button_layout)

        # -------------------------
        # Answer Section
        # -------------------------
        answer_group = QGroupBox("Answer:")
        answer_layout = QVBoxLayout()

        self.result_label = QLabel("BMI = ")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-weight: bold;")

        answer_layout.addWidget(self.result_label)

        # -------------------------
        # BMI Table (Adult)
        # -------------------------
        table_label = QLabel("Adult BMI")
        table_label.setAlignment(Qt.AlignCenter)
        table_label.setStyleSheet("font-weight: bold;")

        answer_layout.addWidget(table_label)

        self.bmi_table = QTableWidget(4, 2)
        self.bmi_table.setHorizontalHeaderLabels(["BMI", "Status"])
        self.bmi_table.verticalHeader().setVisible(False)
        self.bmi_table.setEditTriggers(QTableWidget.NoEditTriggers)

        data = [
            ("≤ 18.4", "Underweight"),
            ("18.5 - 24.9", "Normal"),
            ("25.0 - 39.9", "Overweight"),
            ("≥ 40.0", "Obese"),
        ]

        for row, (bmi, status) in enumerate(data):
            self.bmi_table.setItem(row, 0, QTableWidgetItem(bmi))
            self.bmi_table.setItem(row, 1, QTableWidgetItem(status))

        answer_layout.addWidget(self.bmi_table)
        answer_group.setLayout(answer_layout)

        main_layout.addWidget(answer_group)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("BMI Calculator")
    window.setFixedSize(300, 470)
    window.setCentralWidget(BMICalculator())
    window.show()
    sys.exit(app.exec())
