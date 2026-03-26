import sys, os
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QComboBox,
    QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout,
    QFileDialog, QStatusBar, QToolBar, QSlider, QStyle
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
dir = os.path.dirname(os.path.abspath(__file__))
MAX_POINTS = 40
DEFAULT_STAT = 5


class CharacterBuilder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPG Character Builder")
        self.resize(820, 500)

        self.build_ui()
        self.build_menu()
        self.build_toolbar()
        self.build_statusbar()

    # ---------- UI ----------
    def build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)

        # LEFT PANEL
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        form = QFormLayout()
        self.name_input = QLineEdit()
        self.race_box = QComboBox()
        self.class_box = QComboBox()
        self.gender_box = QComboBox()

        self.race_box.addItems(["Human", "Elf", "Dwarf", "Orc", "Undead"])
        self.class_box.addItems(["Warrior", "Mage", "Rogue", "Paladin", "Ranger"])
        self.gender_box.addItems(["Male", "Female", "Other"])

        form.addRow("Character Name:", self.name_input)
        form.addRow("Race:", self.race_box)
        form.addRow("Class:", self.class_box)
        form.addRow("Gender:", self.gender_box)

        left_layout.addLayout(form)

        # STATS (SLIDERS)
        self.stats = {}
        self.stat_labels = {}

        for stat in ["STR", "DEX", "INT", "VIT"]:
            label = QLabel(f"{stat}: {DEFAULT_STAT}")
            slider = QSlider(Qt.Horizontal)
            slider.setRange(1, 20)
            slider.setValue(DEFAULT_STAT)
            slider.setTickInterval(1)
            slider.setTickPosition(QSlider.TicksBelow)

            slider.valueChanged.connect(
                lambda value, s=stat: self.on_stat_changed(s, value)
            )

            self.stats[stat] = slider
            self.stat_labels[stat] = label

            left_layout.addWidget(label)
            left_layout.addWidget(slider)

        self.total_label = QLabel()
        left_layout.addWidget(self.total_label)

        self.generate_btn = QPushButton("Generate Character Sheet")
        self.generate_btn.clicked.connect(self.generate_sheet)
        left_layout.addWidget(self.generate_btn)

        # RIGHT PANEL
        self.sheet_display = QLabel("— Character Sheet —")
        self.sheet_display.setFixedWidth(250)
        self.sheet_display.setAlignment(Qt.AlignTop)
        self.sheet_display.setAlignment(Qt.AlignCenter)
        self.sheet_display.setStyleSheet(
            "background-color:#1e1e2f; color:white; padding:10px;"
        )

        main_layout.addWidget(left_panel)
        main_layout.addWidget(self.sheet_display)

        self.update_total()

    # ---------- MENU ----------
    def build_menu(self):
        game_menu = self.menuBar().addMenu("Game")
        edit_menu = self.menuBar().addMenu("Edit")

        game_menu.addAction("New Character", self.reset_all)
        game_menu.addAction("Generate Sheet", self.generate_sheet)
        game_menu.addAction("Save Sheet", self.save_sheet)
        game_menu.addSeparator()
        game_menu.addAction("Exit", self.close)

        edit_menu.addAction("Reset Stats", self.reset_stats)
        edit_menu.addAction("Randomize", self.randomize_all)

    # ---------- TOOLBAR ----------
    def build_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        toolbar.addAction(QAction(QIcon.fromTheme("document-new"), "Reset", self, triggered=self.reset_all))
        toolbar.addAction(QAction(QIcon.fromTheme("address-book-new"), "Generate", self, triggered=self.generate_sheet))
        toolbar.addAction(QAction(QIcon.fromTheme("view-refresh"), "Random", self, triggered=self.randomize_all))
        toolbar.addAction(QAction(QIcon.fromTheme("document-save"), "Save", self, triggered=self.save_sheet))

    # ---------- STATUS BAR ----------
    def build_statusbar(self):
        self.status = QStatusBar()
        self.setStatusBar(self.status)

    # ---------- LOGIC ----------
    def on_stat_changed(self, stat, value):
        self.stat_labels[stat].setText(f"{stat}: {value}")
        self.update_total()

    def update_total(self):
        total = sum(slider.value() for slider in self.stats.values())
        self.total_label.setText(f"Points used: {total} / {MAX_POINTS}")

        if total > MAX_POINTS:
            self.total_label.setStyleSheet("color:red;")
        else:
            self.total_label.setStyleSheet("color:white;")

    def stat_bar(self, value):
        return "█" * value + "░" * (20 - value)

    def generate_sheet(self):
        sheet = f"""
{self.name_input.text()}
{self.race_box.currentText()} | {self.class_box.currentText()} | {self.gender_box.currentText()}

STR {self.stat_bar(self.stats['STR'].value())}
DEX {self.stat_bar(self.stats['DEX'].value())}
INT {self.stat_bar(self.stats['INT'].value())}
VIT {self.stat_bar(self.stats['VIT'].value())}
"""
        self.sheet_display.setText(sheet.strip())
        self.status.showMessage("Character sheet generated.", 3000)

    def save_sheet(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save Sheet", "", "Text Files (*.txt)")
        if path:
            with open(path, "w") as f:
                f.write(self.sheet_display.text())
            self.status.showMessage("Character sheet saved.", 3000)

    def reset_stats(self):
        for stat, slider in self.stats.items():
            slider.setValue(DEFAULT_STAT)
            self.stat_labels[stat].setText(f"{stat}: {DEFAULT_STAT}")
        self.status.showMessage("Stats reset.", 2000)

    def reset_all(self):
        self.name_input.clear()
        self.race_box.setCurrentIndex(0)
        self.class_box.setCurrentIndex(0)
        self.gender_box.setCurrentIndex(0)
        self.reset_stats()
        self.sheet_display.setText("— Character Sheet —")
        self.status.showMessage("New character created.", 3000)

    def randomize_all(self):
        self.name_input.setText(random.choice(["Aryn", "Thalos", "Nyx", "Korr", "Elira"]))
        self.race_box.setCurrentIndex(random.randint(0, 4))
        self.class_box.setCurrentIndex(random.randint(0, 4))
        self.gender_box.setCurrentIndex(random.randint(0, 2))

        remaining = MAX_POINTS
        for stat in self.stats:
            value = random.randint(1, min(20, remaining))
            self.stats[stat].setValue(value)
            remaining -= value

        self.status.showMessage("Character randomized.", 3000)


if __name__ == "__main__":
    sys.argv += ['-platform', 'windows:darkmode=2']
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    with open(os.path.join(dir, "P2.style.qss") , "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())
    window = CharacterBuilder()
    window.show()
    sys.exit(app.exec())