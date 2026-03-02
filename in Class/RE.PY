from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog,
                                QVBoxLayout, QLabel, QListWidget, QListWidgetItem,
                                QLineEdit, QPushButton, QDialogButtonBox)
import sys

class AddItemDialog(QDialog): # inherit from QDialog
    """
    A modal dialog that collects a new item name from the user.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Item")
        self._result_text = ""
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)

        self._input = QLineEdit()
        self._input.setPlaceholderText("Enter item name...")

        btn_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        btn_box.accepted.connect(self._on_ok)
        btn_box.rejected.connect(self.reject)

        layout.addWidget(QLabel("Item name:"))
        layout.addWidget(self._input)
        layout.addWidget(btn_box)

    def _on_ok(self):
        self._result_text = self._input.text()
        self.accept()

    def get_result(self) -> str: # for hint: return value as string
        """Return the text entered by the user."""
        return self._result_text


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multiple Windows Demo")

        central = QWidget()
        layout = QVBoxLayout(central)

        self._label = QLabel("My List:")
        self._list = QListWidget()
        add_btn = QPushButton("Add Item")
        add_btn.clicked.connect(self.open_dialog)

        layout.addWidget(self._label)
        layout.addWidget(self._list)
        layout.addWidget(add_btn)
        self.setCentralWidget(central)

    def open_dialog(self):
        dialog = AddItemDialog(parent=self) # mainwindow is an owner
        if dialog.exec() == QDialog.DialogCode.Accepted:
            item = dialog.get_result()
            if item.strip(): # check for empty input
                self._list.addItem(QListWidgetItem(item))

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()