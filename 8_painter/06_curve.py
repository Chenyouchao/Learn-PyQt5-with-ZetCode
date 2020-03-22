import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QPainterPath
from PySide2.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Bézier curve')
        self.show()

    def paintEvent(self, event):

        qp = QPainter()

        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)     # 去除锯齿
        self.drawBezierCurve(qp)
        qp.end()

    def drawBezierCurve(self, qp):

        path = QPainterPath()
        path.moveTo(30, 30)
        path.cubicTo(30, 30, 200, 350, 350, 30)     # 二阶贝塞尔曲线(cubic: 立方体)
                                                    # 起始点, 控制点, 终止点

        qp.drawPath(path)       # 让画家照着path描画

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()