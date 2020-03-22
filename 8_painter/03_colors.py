import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush, QColor

class EXample(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Colours")
        self.show()

    def paintEvent(self, e):        # Event一般为原生槽

        qp = QPainter()

        # qp.start(self)
        qp.begin(self)
        self.drawRectangles(qp)       # 画家层次的抽象. 封装画笔, 颜料等细节
        qp.end()

    def drawRectangles(self, qp):

        # 颜料
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        # 笔蘸墨
        qp.setPen(col)      # ? 取消黑色边框

        qp.setBrush(QColor(200, 0, 0))      # 直接装好墨的刷子
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(130, 15, 90, 60)        # rect的边框用pen画, 中间用brush刷底色

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 90, 60)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = EXample()
    app.exec_()