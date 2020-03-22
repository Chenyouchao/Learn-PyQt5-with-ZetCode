import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QPen
from PySide2.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Pen styles")
        self.show()

    def paintEvent(self, e):    # ? 不可省略e

        qp = QPainter()

        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):

        pen = QPen(Qt.black, 2, Qt.SolidLine)       # 宽度, 两像素

        qp.setPen(pen)      # 画家拿起画笔
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])   # 一实一空
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)      # 前两个为起点, 后两个为终点

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()