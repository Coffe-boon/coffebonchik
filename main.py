import random
import sys

from PyQt6 import QtWidgets, uic, QtGui
from PyQt6.QtWidgets import QApplication


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        self.cir = []
        super(MainApp, self).__init__()
        uic.loadUi("UI.ui", self)
        self.setGeometry(100, 100, 800, 600)
        self.pushButton.clicked.connect(self.draw_circles)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        for circle in self.cir:
            painter.setBrush(QtGui.QColor(255, 255, 0))
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])

    def draw_circles(self):
        self.cir.clear()
        for _ in range(10):
            diameter = random.randint(20, 100)
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            self.cir.append((x, y, diameter))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec())
