from os import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QLabel, QPushButton,
                                QWidget, QVBoxLayout, QProgressBar)
from PySide6.QtCore import QThread, Signal
import time

class WorkerThread(QThread):
    """
    Simulates a long-running background task.

    Signals:
        progress_updated (int): Current progress value (0–100).
    """
    progress_updated = Signal(int)

    def run(self):
        """Task logic — runs in the background thread."""
        for i in range(1, 11):
            time.sleep(0.5)           # Simulate work
            self.progress_updated.emit(i * 10)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progress in Status Bar")
        self.resize(400, 300)

        # Status bar setup
        self.statusBar().showMessage("Ready")

        # Embed a QProgressBar in the status bar
        self._progress = QProgressBar()
        self._progress.setRange(0, 100)
        self._progress.setValue(0)
        self._progress.setFixedWidth(150)
        self._progress.hide()         # Hidden until a task starts
        self.statusBar().addPermanentWidget(self._progress) # add the progress bar on the right of the status bar

        # Central widget
        central = QWidget()
        layout = QVBoxLayout(central)
        self._start_btn = QPushButton("Start Task")
        self._start_btn.clicked.connect(self.start_task)
        layout.addWidget(self._start_btn)
        self.setCentralWidget(central)

    def start_task(self):
        self._start_btn.setEnabled(False)   # Prevent double-clicking
        self._progress.setValue(0)
        self._progress.show()         # show the progress bare
        self.statusBar().showMessage("Processing...")

        self.worker = WorkerThread()
        self.worker.progress_updated.connect(self.update_progress)
        self.worker.finished.connect(self.task_done)
        self.worker.start()

    def update_progress(self, value):
        self._progress.setValue(value)

    def task_done(self):
        self._progress.hide()
        self._start_btn.setEnabled(True)
        self.statusBar().showMessage("Done!", 3000)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()