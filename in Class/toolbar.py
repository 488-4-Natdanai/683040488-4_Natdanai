from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QStyle, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, QAction
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QToolBar Example")
        self.resize(400, 300)

        # Create a toolbar
        toolbar = QToolBar("My Main Toolbar")
        self.addToolBar(toolbar)

        # Add actions to the toolbar with connections
        # New action
        new_icon = self.style().standardIcon(QStyle.SP_FileIcon)
        new_action = QAction(new_icon, "New", self)
        new_action.triggered.connect(self.new_file)
        toolbar.addAction(new_action)

        # Open action
        open_icon = self.style().standardIcon(QStyle.SP_DialogOpenButton)
        open_action = QAction(open_icon, "Open", self)
        open_action.triggered.connect(self.open_file)
        toolbar.addAction(open_action)

        # Save action
        save_icon = self.style().standardIcon(QStyle.SP_DialogSaveButton)
        save_action = QAction(save_icon, "Save", self)
        save_action.triggered.connect(self.save_file)
        toolbar.addAction(save_action)

        # custom-made actions
        action1 = QAction(QIcon("icon.png"), "Action 1", self)
        action1.triggered.connect(self.action1_triggered)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("icon.png"), "Action 2", self)
        action2.triggered.connect(self.action2_triggered)
        toolbar.addAction(action2)

    def new_file(self):
        """Handle creating a new file"""
        # Clear current work or create a new window
        print("New file created")
        QMessageBox.information(self, "New File", "New file created")

    def open_file(self):
        """Open an existing file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "All Files (*);;Text Files (*.txt);;Python Files (*.py)"
        )

        if file_path:
            print(f"Opening file: {file_path}")
            # Here you would add code to read the file and display it
            QMessageBox.information(self, "File Opened", f"Opened: {file_path}")

    def save_file(self):
        """Save the current file"""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "",
            "All Files (*);;Text Files (*.txt);;Python Files (*.py)"
        )

        if file_path:
            print(f"Saving file to: {file_path}")
            # Here you would add code to save your content to the file
            QMessageBox.information(self, "File Saved", f"Saved to: {file_path}")

    def action1_triggered(self):
        print("Action 1 triggered")


    def action2_triggered(self):
        print("Action 2 triggered")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()