from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                                QVBoxLayout, QListWidget, QListWidgetItem,
                                QPushButton, QAbstractItemView)
from PySide6.QtCore import Qt
import sys

class DraggableList(QListWidget):
    """
    A QListWidget subclass with drag-and-drop reordering enabled.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.setDefaultDropAction(Qt.DropAction.MoveAction)

    def get_all_items(self) -> list:
        """Return all item texts in current order."""
        return [self.item(i).text() for i in range(self.count())]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drag & Drop Demo")

        central = QWidget()
        layout = QVBoxLayout(central)

        # Creating a subclass object instance
        self._list = DraggableList()
        tasks = ["Design UI", "Write models", "Connect database",
                 "Add validation", "Write tests", "Deploy"]
        for task in tasks:
            self._list.addItem(QListWidgetItem(task))

        # Print button
        print_btn = QPushButton("Print Order")
        print_btn.clicked.connect(self.print_order)

        # Add widgets to the layout
        layout.addWidget(self._list)
        layout.addWidget(print_btn)
        self.setCentralWidget(central)

    def print_order(self):
        for i, text in enumerate(self._list.get_all_items(), 1):
            print(f"{i}. {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()