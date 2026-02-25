import sys
from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sales Chart")

        # Your data
        months = [1, 2, 3, 4, 5, 6] # x
        sales_a = [150, 200, 180, 250, 300, 280]  # y_1
        sales_b = [100, 120, 160, 200, 220, 260] # y_2

        # Create plot
        plot_widget = pg.PlotWidget()
        plot_widget.setBackground("w")
        plot_widget.setTitle("Monthly Sales")
        plot_widget.setLabel("left", "Sales ($)")
        plot_widget.setLabel("bottom", "Month")
        plot_widget.addLegend()

        # Plot the data
        plot_widget.plot(months, sales_a, pen=pg.mkPen("b", width=2), name="Store A")
        plot_widget.plot(months, sales_b, pen=pg.mkPen("r", width=2), name="Store B")

        self.setCentralWidget(plot_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec())