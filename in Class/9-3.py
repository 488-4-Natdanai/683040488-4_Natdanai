import sys
import csv
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QTableWidget, QTableWidgetItem,
    QFileDialog, QLineEdit, QMessageBox
)
from PySide6.QtCore import Qt
from pathlib import Path

class StudentManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Score Manager")
        self.resize(700, 500)
        self.current_path = None

        # ── Central widget & layout ──────────────────
        widget = QWidget()
        main_layout = QVBoxLayout(widget)
        self.setCentralWidget(widget)

        # ── Toolbar: Load / Save buttons ─────────────
        toolbar = QHBoxLayout()
        self.btn_load = QPushButton("Load CSV")
        self.btn_save = QPushButton("Save CSV")
        self.lbl_file = QLabel("No file loaded")
        self.btn_save.setEnabled(False)

        toolbar.addWidget(self.btn_load)
        toolbar.addWidget(self.btn_save)
        toolbar.addWidget(self.lbl_file)
        toolbar.addStretch()

        # ── Table ─────────────────────────────────────
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Score", "Grade"])
        self.table.horizontalHeader().setStretchLastSection(True)

        # ── Add new student row ───────────────────────
        add_layout = QHBoxLayout()
        self.input_name  = QLineEdit()
        self.input_score = QLineEdit()
        self.input_grade = QLineEdit()
        self.input_name.setPlaceholderText("Name")
        self.input_score.setPlaceholderText("Score")
        self.input_grade.setPlaceholderText("Grade")
        self.btn_add = QPushButton("Add Row")

        add_layout.addWidget(self.input_name)
        add_layout.addWidget(self.input_score)
        add_layout.addWidget(self.input_grade)
        add_layout.addWidget(self.btn_add)

        # ── Status bar ────────────────────────────────
        self.statusBar().showMessage("Ready")

        # ── Assemble layout ───────────────────────────
        main_layout.addLayout(toolbar)
        main_layout.addWidget(self.table)
        main_layout.addLayout(add_layout)

        # ── Connect signals ───────────────────────────
        self.btn_load.clicked.connect(self.load_file)
        self.btn_save.clicked.connect(self.save_file)
        self.btn_add.clicked.connect(self.add_row)

    # ──────────────────────────────────────────────────
    # TODO 1: Open a file dialog, read the CSV,
    #         and populate self.table with the data
    # ──────────────────────────────────────────────────
    def load_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select a File",
            "",
            "All Files (*)"
            )
        if not path:
            return
        self.current_path = path
        self.lbl_file.setText(path)
        self.table.setRowCount(0)

        with open(path, "r", newline="", encoding="utf-8") as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                name = row["name"]
                score = row["score"]
                grade = row["grade"]

                r = self.table.rowCount()
                self.table.insertRow(r)

                self.table.setItem(r, 0, QTableWidgetItem(name))
                self.table.setItem(r, 1, QTableWidgetItem(score))
                self.table.setItem(r, 2, QTableWidgetItem(grade))

        self.btn_save.setEnabled(True)

        
        self.statusBar().showMessage("CSV loaded")

    # ──────────────────────────────────────────────────
    # TODO 2: Read all rows from self.table,
    #         and write them to a CSV file
    # ──────────────────────────────────────────────────
    def save_file(self):
            path, _ = QFileDialog.getSaveFileName(
                self,
                "Save File",
                "",
                "All Files (*)"
            )

            if not path:
                return

            self.current_path = path

            with open(self.current_path, "w", newline="", encoding="utf-8") as fout:

                writer = csv.writer(fout)

                writer.writerow(["name", "score", "grade"])

                rows = self.table.rowCount()
                cols = self.table.columnCount()

                for r in range(rows):

                    row_data = []
                    for c in range(cols):

                        item = self.table.item(r, c)

                        if item:
                            row_data.append(item.text())
                        else:
                            row_data.append("")

                writer.writerow(row_data)

            self.statusBar().showMessage("File Saved")

    # ──────────────────────────────────────────────────
    # Read the three input fields,
    #      and add a new row to self.table
    # ──────────────────────────────────────────────────
    def add_row(self):
        name  = self.input_name.text().strip()
        score = self.input_score.text().strip()
        grade = self.input_grade.text().strip()

        if not name or not score or not grade:
            QMessageBox.warning(self, "Missing Data", "Please fill in all fields")
            return

        r = self.table.rowCount()
        self.table.insertRow(r)
        self.table.setItem(r, 0, QTableWidgetItem(name))
        self.table.setItem(r, 1, QTableWidgetItem(score))
        self.table.setItem(r, 2, QTableWidgetItem(grade))

        self.input_name.clear()
        self.input_score.clear()
        self.input_grade.clear()

        self.statusBar().showMessage(f"Added {name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = StudentManager()
    win.show()
    sys.exit(app.exec())