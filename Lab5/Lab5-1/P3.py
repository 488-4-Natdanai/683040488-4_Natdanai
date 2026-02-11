import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QComboBox, QGroupBox, QGridLayout,
    QMainWindow, QTableWidget, QTableWidgetItem, QFormLayout
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
        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignRight)
        form_layout.setFormAlignment(Qt.AlignTop)

        # Age Group
        self.age_combo = QComboBox()
        self.age_combo.addItems([
            "Adult Age 20+",
            "Child (2 - 19)"
        ])
        form_layout.addRow("BMI age group:", self.age_combo)

        # Weight
        weight_layout = QHBoxLayout()
        self.weight_input = QLineEdit()
        self.weight_input.setFixedWidth(80)

        self.weight_unit = QComboBox()
        self.weight_unit.addItems([
            "kilograms",
            "pounds"
        ])

        weight_layout.addWidget(self.weight_input)
        weight_layout.addWidget(self.weight_unit)

        form_layout.addRow("Weight:", weight_layout)

        # Height
        height_layout = QHBoxLayout()
        self.height_input = QLineEdit()
        self.height_input.setFixedWidth(80)

        self.height_unit = QComboBox()
        self.height_unit.addItems([
            "meters",
            "centimeters",
            "feet"
        ])

        height_layout.addWidget(self.height_input)
        height_layout.addWidget(self.height_unit)

        form_layout.addRow("Height:", height_layout)

        main_layout.addLayout(form_layout)


        # -------------------------
        # Buttons
        # -------------------------
        button_layout = QHBoxLayout()

        self.clear_button = QPushButton("Clear")
        self.clear_button.setFixedSize(80,35)
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.setFixedHeight(35)

        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.calculate_button)

        main_layout.addLayout(button_layout)

        # -------------------------
        # result Section
        # -------------------------
        result_group = QGroupBox()
        result_layout = QVBoxLayout()

        self.your_label = QLabel("Your BMI: ")
        self.your_label.setAlignment(Qt.AlignCenter)
        self.your_label.setStyleSheet("font-weight: bold;")

        result_layout.addWidget(self.your_label)

        result_label = QLabel("0.00")
        result_label.setAlignment(Qt.AlignCenter)
        result_label.setStyleSheet("font-size: 30px; font-weight: bold;")
        result_layout.addWidget(result_label)
        result_layout.setAlignment(result_label, Qt.AlignTop | Qt.AlignHCenter)
        result_layout.addSpacing(20)

        # -------------------------
        # BMI Table (Adult)
        # -------------------------
        self.bmi_table = QTableWidget(4, 2)
        self.bmi_table.setHorizontalHeaderLabels(["BMI", "Status"])
        self.bmi_table.verticalHeader().setVisible(False)
        self.bmi_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.bmi_table.setFixedHeight(150)
        self.bmi_table.setColumnWidth(0, 120)
        self.bmi_table.setColumnWidth(1, 120)
        self.bmi_table.horizontalHeader().setStretchLastSection(True)
        data = [
            ("≤ 18.4", "Underweight"),
            ("18.5 - 24.9", "Normal"),
            ("25.0 - 39.9", "Overweight"),
            ("≥ 40.0", "Obese"),
        ]

        for row, (bmi, status) in enumerate(data):
            self.bmi_table.setItem(row, 0, QTableWidgetItem(bmi))
            self.bmi_table.setItem(row, 1, QTableWidgetItem(status))

        result_layout.addWidget(self.bmi_table)
        result_group.setLayout(result_layout)

        main_layout.addWidget(result_group)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("BMI Calculator")
    window.setFixedSize(300, 480)
    window.setCentralWidget(BMICalculator())
    window.show()
    sys.exit(app.exec())
