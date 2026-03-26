import sys, os
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout,
                               QLabel,QPushButton, QLineEdit, QCheckBox, QComboBox, QSpinBox, QMessageBox, QTextEdit)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QFont
current_dir = os.path.dirname(os.path.abspath(__file__))
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("APP NAME")
        self.setFixedSize(400, 500)
        self.setMinimumSize(300, 400)
        self.setGeometry(100, 100, 400, 500)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        text = QLabel("Hello World")
        text.setFont(QFont("Arial", 14, QFont.Bold))
        text.setAlignment(Qt.AlignCenter)
        text.setText("World Hello ")

        bt = QPushButton("text")
        bt.clicked.connect(lambda: text.setText("Wello Horld"))
        bt.setCheckable(True)

        le = QLineEdit()
        le.setPlaceholderText("Enter text here")
        le.setText("Initial text")
        le.setEchoMode(QLineEdit.Password) # ซ่อนข้อความ
        # อัพเดตข้อความใน QLabel ตามที่พิมพ์ใน QLineEdit
        le.textChanged.connect(lambda: text.setText(le.text())) 
    
        cb = QCheckBox("text")
        # เช็คสถานะของ CheckBox และอัพเดตข้อความใน QLabel ตามสถานะ
        cb.stateChanged.connect(lambda: text.setText("Checked") 
                                if cb.isChecked() else text.setText("Not checked"))
        comb = QComboBox
        comb.addItems([1,2,3])
        comb.currentText()

        sb = QSpinBox
        sb.setRange(0, 60) #min max
        sb.value() #ดึงค่าปัจจุบัน
        
        layout.addWidget(text)
        
        image_label = QLabel()
        image_path = os.path.join(current_dir, "img.png")
        pixmap = QPixmap(image_path)
        image_label.setPixmap(pixmap.scaled(200, 200,
            Qt.KeepAspectRatio,  # maintain aspect ratio
            Qt.SmoothTransformation  # smooth scaling
            ))
        image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(image_label)

        rich_label = QLabel()
        rich_label.setText("<h1>Title</h1><p>This is <b>bold</b> and <i>italic</i> text</p>")
        rich_label.setTextFormat(Qt.RichText)
        rich_label.setOpenExternalLinks(True)  # Allow clicking links
        rich_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(rich_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())