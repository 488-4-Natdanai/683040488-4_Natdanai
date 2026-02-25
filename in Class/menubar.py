import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar
from PySide6.QtGui import QIcon, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Example")
        self.resize(400, 300)

        # Create menu bar
        self.menu_bar = self.menuBar()

        # Create File menu
        file_menu = self.menu_bar.addMenu("&File")

        # Add actions to File menu
        new_action = QAction("&New", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        open_action = QAction("&Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        export_menu = QMenu("&Export As", self)
        file_menu.addMenu(export_menu)
        export_pdf_action = QAction("&PDF", self)
        export_pdf_action.triggered.connect(self.export_pdf)
        export_menu.addAction(export_pdf_action)

        # Add a separator
        file_menu.addSeparator()

        # Add Exit action
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Create Edit menu
        edit_menu = self.menu_bar.addMenu("&Edit")

        # Add actions to Edit menu
        copy_action = QAction("&Copy", self)
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(self.copy)
        edit_menu.addAction(copy_action)

        paste_action = QAction("&Paste", self)
        paste_action.setShortcut("Ctrl+V")
        paste_action.triggered.connect(self.paste)
        edit_menu.addAction(paste_action)

    def new_file(self):
        print("New file")

    def open_file(self):
        print("Open file")

    def copy(self):
        print("Copy")

    def paste(self):
        print("Paste")

    def export_pdf(self):
        print("Export PDF")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
