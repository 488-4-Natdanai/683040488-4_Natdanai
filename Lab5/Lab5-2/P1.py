import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QComboBox, QGroupBox, QMainWindow, QTableWidget,
    QTableWidgetItem, QFormLayout, QMessageBox
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
        title.setFixedSize(280,35)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            background-color: #6f969b;
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

        self.age_combo = QComboBox()
        self.age_combo.addItems([
            "Adult Age 20+",
            "Child (2 - 19)"
        ])
        form_layout.addRow("BMI age group:", self.age_combo)

        # Weight
        weight_layout = QHBoxLayout()
        self.weight_input = QLineEdit()
        self.weight_input.setFixedWidth(60)

        self.weight_unit = QComboBox()
        self.weight_unit.addItems(["kilograms", "pounds"])

        weight_layout.addWidget(self.weight_input)
        weight_layout.addWidget(self.weight_unit)
        form_layout.addRow("Weight:", weight_layout)

        # Height
        height_layout = QHBoxLayout()
        self.height_input = QLineEdit()
        self.height_input.setFixedWidth(60)

        self.height_unit = QComboBox()
        self.height_unit.addItems(["meters", "centimeters", "feet"])

        height_layout.addWidget(self.height_input)
        height_layout.addWidget(self.height_unit)
        form_layout.addRow("Height:", height_layout)

        main_layout.addLayout(form_layout)

        # -------------------------
        # Buttons
        # -------------------------
        button_layout = QHBoxLayout()

        self.clear_button = QPushButton("Clear")
        self.clear_button.setFixedSize(80, 35)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.setStyleSheet("""
            QPushButton {
                background-color: #6f969b;
            }
            QPushButton:hover {
                background-color: #65898d;
            }
            QPushButton:pressed {
                background-color: #4a6467;
            }
        """)
        self.calculate_button.setFixedHeight(35)

        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.calculate_button)

        main_layout.addLayout(button_layout)

        # -------------------------
        # Result Section
        # -------------------------
        result_group = QGroupBox()
        result_layout = QVBoxLayout()

        self.your_label = QLabel("Your BMI:")
        self.your_label.setAlignment(Qt.AlignCenter)
        self.your_label.setStyleSheet("font-weight: bold;")

        self.result_label = QLabel("0.00")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 35px; font-weight: bold;")

        # -------------------------
        # Child
        # -------------------------
        self.child1_label = QLabel("For child's BMI interpretation, \nplease click one of the following links.")
        self.child1_label.setAlignment(Qt.AlignCenter)
        self.child1_label.setStyleSheet("font-size: 12px;;")
        self.child1_label.hide()
        self.child2_label = QLabel('<a href="https://kku.world/boysbmi4884">BMI graph for BOYS</a> <a href="https://kku.world/girlsbmi4884">BMI graph for GIRLS</a>')
        self.child2_label.setOpenExternalLinks(True)
        self.child2_label.setAlignment(Qt.AlignCenter)
        self.child2_label.setStyleSheet("font-size: 12px;;")
        self.child2_label.hide()
        
        result_layout.addWidget(self.your_label)
        result_layout.addWidget(self.result_label)
        result_layout.addWidget(self.child1_label)
        result_layout.addWidget(self.child2_label)
        result_layout.addStretch()

        # -------------------------
        # BMI Table
        # -------------------------
        self.bmi_table = QTableWidget(4, 2)
        self.bmi_table.setHorizontalHeaderLabels(["BMI", "Condition"])
        self.bmi_table.verticalHeader().setVisible(False)
        self.bmi_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.bmi_table.setFixedHeight(150)
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
        self.bmi_table.hide()
        
        result_group.setLayout(result_layout)
        main_layout.addWidget(result_group)
        self.setLayout(main_layout)

        # -------------------------
        # Connections
        # -------------------------
        self.calculate_button.clicked.connect(self.calculate_bmi)
        self.clear_button.clicked.connect(self.clear_fields)

    # =============================
    # BMI Logic
    # =============================
    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())

            # Convert weight
            if self.weight_unit.currentText() == "pounds":
                weight = weight * 0.453592

            # Convert height
            unit = self.height_unit.currentText()
            if unit == "centimeters":
                height = height / 100
            elif unit == "feet":
                height = height * 0.3048

            if height <= 0:
                raise ValueError

            bmi = weight / (height ** 2)
            self.result_label.setText(f"{bmi:.2f}")

            if self.age_combo.currentText() == "Adult Age 20+":
                self.child1_label.hide()
                self.child2_label.hide()
                self.bmi_table.show()
            elif self.age_combo.currentText() == "Child (2 - 19)":
                self.bmi_table.hide()
                self.child1_label.show()
                self.child2_label.show()

            #self.highlight_category(bmi)

        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numbers.")

    def clear_fields(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.bmi_table.hide()
        self.child1_label.hide()
        self.child2_label.hide()
        self.result_label.setText("0.00")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("BMI Calculator")
    window.setFixedSize(300, 480)
    window.setCentralWidget(BMICalculator())
    window.show()
    sys.exit(app.exec())
