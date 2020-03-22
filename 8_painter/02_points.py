import sys, random
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter
from PySide2.QtCore import Qt       # 单一熟悉, 字体, 颜色等

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()   # 方法调用, 会自动传入self,
                        # 再加就变为了initUI(self, self)

    def initUI(self):

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Points")
        self.show()

    def paintEvent(self, e):

        qp = QPainter()

        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):

        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width() - 1)     # 不会画在边上
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()