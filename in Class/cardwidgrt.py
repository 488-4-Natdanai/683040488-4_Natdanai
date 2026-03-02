from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                                QVBoxLayout, QHBoxLayout, QLabel,
                                QPushButton, QScrollArea, QFrame)
from PySide6.QtCore import Signal
import sys


class CardWidget(QFrame):
    """
    A reusable card component displaying a title, description,
    and a delete button.

    Signals:
        delete_requested (str): Emitted with the card title when delete is clicked.
    """

    delete_requested = Signal(str)

    def __init__(self, title: str, description: str, parent=None):
        """
        Args:
            title (str): Card title text.
            description (str): Card body text.
        """
        super().__init__(parent)
        self._title = title
        self._setup_ui(title, description)
        self.setFrameShape(QFrame.StyledPanel)

    def _setup_ui(self, title, description):
        layout = QVBoxLayout(self)

        self._title_label = QLabel(f"<b>{title}</b>")
        self._desc_label = QLabel(description)
        self._desc_label.setWordWrap(True)

        self._delete_btn = QPushButton("Delete")
        self._delete_btn.clicked.connect(
            lambda: self.delete_requested.emit(self._title) # send title with the signal
        )

        layout.addWidget(self._title_label)
        layout.addWidget(self._desc_label)
        layout.addWidget(self._delete_btn)

    # --- Public API ---
    # text: str -- set hint that text should be a string, but not enforced
    def set_description(self, text: str):
        """Update the card description."""
        self._desc_label.setText(text)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Card Widget Demo")

        scroll = QScrollArea()
        container = QWidget()
        self._layout = QVBoxLayout(container)

        cards_data = [
            ("Task 1", "Design the database schema"),
            ("Task 2", "Build the login screen"),
            ("Task 3", "Write unit tests"),
        ]

        self._cards = {}  # keep track of the titles of card widget

        for title, desc in cards_data:
            card = CardWidget(title, desc)

            # delete_requested a signal emitted when clicking the delete button in the card
            # connect delete_requested signal to on_delete — title will be passed automatically
            card.delete_requested.connect(self.on_delete)

            self._layout.addWidget(card)
            self._cards[title] = card

        self._layout.addStretch()
        scroll.setWidget(container)
        scroll.setWidgetResizable(True)
        self.setCentralWidget(scroll)

    # title comes from CardWidget.delete_requested.emit(self._title)
    def on_delete(self, title: str):
        print(f"Delete requested for: {title}")
        if title in self._cards:
            card = self._cards.pop(title)   # Remove from dict
            self._layout.removeWidget(card) # Remove from layout
            card.deleteLater()              # Delete from memory


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
