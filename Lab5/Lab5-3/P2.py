import sys, os
import pyqtgraph as pg
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QComboBox, QMainWindow, QSpinBox, QMessageBox
)
from PySide6.QtCore import Qt

dir = os.path.dirname(os.path.abspath(__file__))

month = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]

cate = {
    "Electronics": "#1f77b4",
    "Clothing": "#ff7f0e",
    "Food": "#2ca02c",
    "Others": "#d62728"
}

class Monthly_Sales_Chart(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monthly Sales Chart")
        self.resize(900, 550)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # ===== Title =====
        title = QLabel("Monthly Sales Chart")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            background-color: #C21A00;
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 6px;
            border-radius: 15px;
        """)
        main_layout.addWidget(title)

        # ===== Input =====
        input_layout = QHBoxLayout()

        input_layout.addWidget(QLabel("Filename:"))
        self.filename = QLineEdit("sales_data.txt")
        input_layout.addWidget(self.filename)

        input_layout.addWidget(QLabel("Month:"))
        self.month = QComboBox()
        self.month.addItems(month)
        input_layout.addWidget(self.month)

        input_layout.addWidget(QLabel("Sales Amount:"))
        self.salesamount = QSpinBox()
        self.salesamount.setMaximum(1000000)
        input_layout.addWidget(self.salesamount)

        input_layout.addWidget(QLabel("Category:"))
        self.productcate = QComboBox()
        self.productcate.addItems(cate.keys())
        input_layout.addWidget(self.productcate)

        main_layout.addLayout(input_layout)

        # ===== Buttons =====
        btn_layout = QHBoxLayout()

        self.import_button = QPushButton("Import Data")
        self.import_button.clicked.connect(self.import_data)
        btn_layout.addWidget(self.import_button)

        self.add_button = QPushButton("Add Data")
        self.add_button.clicked.connect(self.add_data)
        btn_layout.addWidget(self.add_button)

        self.clear_button = QPushButton("Clear Chart")
        self.clear_button.clicked.connect(self.clear_data)
        btn_layout.addWidget(self.clear_button)

        main_layout.addLayout(btn_layout)

        # ===== Chart =====
        self.plot = pg.PlotWidget()
        self.plot.setTitle("Monthly Sales by Product Category")
        self.plot.setLabel("left", "Sales Amount")
        self.plot.setLabel("bottom", "Month")
        self.plot.addLegend()
        self.plot.showGrid(x=True, y=True)
        main_layout.addWidget(self.plot)

        # ===== Data Storage =====
        self.data = {
            cat: [0]*12 for cat in cate
        }

        self.update_chart()

    # ================= Functions =================

    def import_data(self):
        filepath = os.path.join(dir, self.filename.text())

        if not os.path.exists(filepath):
            QMessageBox.warning(self, "Error", "File not found")
            return

        with open(filepath, "r") as f:
            for line in f:
                try:
                    m, amt, cat = line.strip().split(",")
                    idx = month.index(m)
                    self.data[cat][idx] += int(amt)
                except Exception:
                    continue

        self.update_chart()

    def add_data(self):
        idx = self.month.currentIndex()
        cat = self.productcate.currentText()
        amt = self.salesamount.value()

        self.data[cat][idx] += amt
        self.update_chart()

    def clear_data(self):
        for cat in self.data:
            self.data[cat] = [0]*12

        self.filename.clear()
        self.salesamount.setValue(0)
        self.month.setCurrentIndex(0)
        self.productcate.setCurrentIndex(0)

        self.update_chart()

    def update_chart(self):
        self.plot.clear()
        self.plot.addLegend()

        x = list(range(12))
        bottom = [0]*12

        for cat, color in cate.items():
            values = self.data[cat]
            bar = pg.BarGraphItem(
                x=x,
                height=values,
                width=0.6,
                brush=color,
                y0=bottom,
                name=cat
            )
            self.plot.addItem(bar)
            bottom = [bottom[i] + values[i] for i in range(12)]

        self.plot.getAxis("bottom").setTicks(
            [[(i, m) for i, m in enumerate(month)]]
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Monthly_Sales_Chart()
    window.show()
    sys.exit(app.exec())