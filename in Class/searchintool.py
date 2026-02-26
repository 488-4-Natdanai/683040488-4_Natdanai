from PySide6.QtWidgets import (QMainWindow, QApplication, QToolBar, 
                             QLineEdit, QVBoxLayout, QWidget, QLabel)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide Search Toolbar")
        self.resize(400, 300)

        # 1. Create the Toolbar
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        # 2. Create the Search Bar (QLineEdit)
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.textChanged.connect(self.update_search)
        
        # 3. Add Widget to Toolbar
        toolbar.addWidget(self.search_bar)

    def update_search(self, text):
        print(f"Searching for: {text}")
        # Add filtering logic here (e.g., filter list widgets)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
