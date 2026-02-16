## For Student ##

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QTableWidget, QTableWidgetItem, QSpinBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
import sys


class InventoryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Inventory Manager")
        self.setGeometry(100, 100, 600, 400)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Input section layout
        input_layout = QHBoxLayout()

        # Product Name input
        input_layout.addWidget(QLabel("Product Name:"))
        self.product_input = QLineEdit()
        self.product_input.setPlaceholderText("Enter product name")
        input_layout.addWidget(self.product_input)

        # Quantity input
        input_layout.addWidget(QLabel("Quantity:"))
        self.quantity_input = QSpinBox()
        self.quantity_input.setRange(0, 1000)
        input_layout.addWidget(self.quantity_input)

        # Add Product button
        self.add_button = QPushButton("Add Product")
        input_layout.addWidget(self.add_button)
        self.add_button.clicked.connect(self.add_product)

        # Clear All button
        self.clear_button = QPushButton("Clear All")
        input_layout.addWidget(self.clear_button)
        self.clear_button.clicked.connect(self.clear_all)

        # add input layout to the main layout
        main_layout.addLayout(input_layout)

        # Table widget
        # create table widget, set col, set headers
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Product Name", "Quantity", "Status"])

        # set additional col properties
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setColumnWidth(0, 200) # name col
        self.table.setColumnWidth(1, 100) # quantity col
        self.table.setColumnWidth(2, 300) # status col

        # add table to the main layout
        main_layout.addWidget(self.table)

    def add_product(self):
        """Add a new product to the inventory table"""

        # get product data from the class object
        # LineEditWidget.text().strip()
        # SpinBoxWidget.value()
        name = self.product_input.text().strip()
        amount = self.quantity_input.value()

        # Validate input: product name
        if not name:
            print("Input a product name")
            return

        # Determine status based on quantity\
        if amount < 10:
            status = "Low Stock"

        else:
            status = "In Stock"

        # Add new row to table
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        # Add items to the row
        # QTableItemWidget.setTextAlignment(Qt.AlignCenter)
        
        name_item = QTableWidgetItem(name)
        quan_item = QTableWidgetItem(str(amount))
        quan_item.setTextAlignment(Qt.AlignCenter)
        if amount < 10:
            status_item = QTableWidgetItem("Low Stock")
            status_item.setBackground(QColor("#ff7a7a"))
        else:
            status_item = QTableWidgetItem("In Stock")
            status_item.setBackground(QColor("#63ff63"))

        # Color code the status
        # QTableItemWidget.setBackground(Qt.red)

        self.table.setItem(row_position, 0, name_item)
        self.table.setItem(row_position, 1, quan_item)
        self.table.setItem(row_position, 2, status_item)

        # Clear input fields
        # Move the focus to the product input
        # product_input.setFocus()
        self.product_input.clear()
        self.quantity_input.setValue(0)
        self.product_input.setFocus()

    def clear_all(self):
        """Clear all rows from the table"""
        self.table.setRowCount(0)


def main():
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()