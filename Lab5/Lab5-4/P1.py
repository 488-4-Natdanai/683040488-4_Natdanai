## For Master ##

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QFormLayout,
                               QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton,
                               QFrame, QSpinBox, QColorDialog, QFileDialog, QToolBar, QStyle)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QAction, QIcon, QPixmap
import sys, os, pyperclip
dir = os.path.dirname(os.path.abspath(__file__))

default_color = "#B0E0E6"

class PersonalCard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P1: Personal Info Card")
        self.setGeometry(100, 100, 400, 500)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)

        self.main_layout.addSpacing(15)

        # input section
        self.input_layout = QFormLayout()
        self.input_layout.setVerticalSpacing(12)
        self.create_form()

        self.main_layout.addSpacing(5)

        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        line.setLineWidth(1)
        line.setStyleSheet("background-color: #cccccc;")

        self.main_layout.addSpacing(10)

        # Output section
        self.bg_widget = QWidget()
        self.output_layout = QVBoxLayout(self.bg_widget)
        self.create_display()

        # menu
        self.create_menu()

        # toolbar
        self.create_toolbar()

        # status bar
        self.statusBar().showMessage("Fill in your details and click generate") 

    def create_form(self):
        form_layout = QGridLayout()
        self.name = QLineEdit()
        self.name.setPlaceholderText("First name and Lastname")
        
        self.age = QSpinBox()
        self.age.setRange(1,120)
        self.age.setValue(25)
        
        self.email = QLineEdit()
        self.email.setPlaceholderText("username@domain.name")
        
        self.position = QComboBox()
        self.position.addItems(["Teaching Staff","Supporting Staff","Student","Visitor"])
        self.position.setPlaceholderText("Choose your position")
        self.position.setCurrentIndex(-1)
        
        color_row = QWidget()
        color_layout = QHBoxLayout(color_row)
        self.fav_color = QColor(default_color)
        self.color_swatch = QLabel()
        self.color_swatch.setFixedSize(22, 22)
        self.color_swatch.setStyleSheet(f"background-color: {self.fav_color.name()}; border: 1px solid #888;")
        color_layout.addWidget(self.color_swatch)
        color_button = QPushButton("Pick New Color")
        color_button.clicked.connect(self.pick_color)
        color_layout.addWidget(color_button)

        form_layout.addWidget(QLabel("Full name:"), 0, 0)
        form_layout.addWidget(self.name, 0, 1)
        form_layout.addWidget(QLabel("Age:"), 1, 0)
        form_layout.addWidget(self.age, 1, 1)
        form_layout.addWidget(QLabel("Email:"), 2, 0)
        form_layout.addWidget(self.email, 2, 1)
        form_layout.addWidget(QLabel("Position:"), 3, 0)
        form_layout.addWidget(self.position, 3, 1)
        form_layout.addWidget(QLabel("Your favorite color:"), 4, 0)
        form_layout.addWidget(color_row, 4, 1)
        self.main_layout.addLayout(form_layout)

    def pick_color(self):
        color = QColorDialog.getColor(self.fav_color, self, "Pick a Color")
        if color.isValid():
            self.fav_color = color
            self.color_swatch.setStyleSheet(f"background-color: {self.fav_color.name()}; border: 1px solid #888;")

    def create_display(self):
    
        self.bg_widget.setStyleSheet(f"background-color: {self.fav_color.name()}; \
                                     border-radius: 6px;")

        self.name_label = QLabel("Your name here")
        self.name_label.setStyleSheet("font-size: 18pt; font-weight: bold;")
        self.age_label = QLabel("(Age)")
        self.position_label = QLabel("Your position here")
        self.position_label.setStyleSheet("font-size: 14pt;")
        email_icon = QLabel()
        email__icon_file = os.path.join(dir, "mail.png")
        email_icon.setPixmap(QPixmap(email__icon_file).scaled(18, 18, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.email_label = QLabel("your_username@domain.name")


    def update_display(self):
        pass

    def clear_form(self):
        self.name.clear()
        self.age.setValue(25)
        self.position.setCurrentIndex(-1)
        self.email.setText("username@domain.name")
        self.bg_widget.setStyleSheet(f"background-color: {default_color}; \
                                     border-radius: 4px;")

    def save_card(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save Card",        # dialog title
            "my_card.txt",      # default filename
            "Text Files (*.txt);;All Files (*)"  # filter
        )

        if filename:  # user didn't cancel
            with open(filename, "w") as f:
                pass

    def clear_display(self):
        self.name_label.setText("Your Name")
        self.age_label.setText(f"(Age)")
        self.position_label.setText("Your Position")
        self.email_label.setText("your_username@domain.name")
        self.bg_widget.setStyleSheet(f"background-color: {default_color}; \
                                     border-radius: 4px;")

    def copy_card(self):
        pass

    def clear_all(self):
        self.clear_form()
        self.clear_display()

    def create_menu(self):
        self.menu_bar = self.menuBar()
        file_menu = self.menu_bar.addMenu("File")

        gen_card_ac = QAction("Generate Card", self)
        #gen_card_ac.triggered.connect()
        file_menu.addAction(gen_card_ac)

        save_card_ac = QAction("Save Card", self)
        #save_card_ac.triggered.connect()
        file_menu.addAction(save_card_ac)

        clear_dis_ac = QAction("Clear Display", self)
        #clear_dis_ac.triggered.connect()
        file_menu.addAction(clear_dis_ac)

        exit_ac = QAction("Exit", self)
        #exit_ac.triggered.connect()
        file_menu.addAction(exit_ac)

        edit_menu = self.menu_bar.addMenu("Edit")

        copy_ac = QAction("Copy Card", self)
        #copy_ac.triggered.connect()
        edit_menu.addAction(copy_ac)

        clear_form_ac = QAction("Clear Form", self)
        #clear_form_ac.triggered.connect()
        edit_menu.addAction(clear_form_ac)
        
    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        gen_icon = self.style().standardIcon(QStyle.SP_CommandLink)
        gen_action = QAction(gen_icon, "Generate Card", self)
        #gen_action.triggered.connect()
        toolbar.addAction(gen_action)

        save_icon = self.style().standardIcon(QStyle.SP_DialogSaveButton)
        save_action = QAction(save_icon, "Generate Card", self)
        #save_action.triggered.connect()
        toolbar.addAction(save_action)

        clr_icon = self.style().standardIcon(QStyle.SP_DialogDiscardButton)
        clr_action = QAction(clr_icon, "Generate Card", self)
        #clr_action.triggered.connect()
        toolbar.addAction(clr_action)

        pass

def main():
    sys.argv += ['-platform', 'windows:darkmode=1'] 
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    style_file = os.path.join(dir, "P1_style.qss")
    with open(style_file, "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    window = PersonalCard()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()