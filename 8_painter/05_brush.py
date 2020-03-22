import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Brushes")
        self.show()

    def paintEvent(self, e):

        qp = QPainter()

        qp.begin(self)
        self.drawBrushes(qp)    # 将画家送到方法中画画
        qp.end()

    def drawBrushes(self, qp):

        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)      # 画家拿起了刷子
        qp.drawRect(10, 15, 90, 60)

        brush = QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)

        brush = QBrush(Qt.DiagCrossPattern)     # 双对角
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush = QBrush(Qt.Dense5Pattern)        # 数值越大, 空白越多
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)

        brush = QBrush(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        brush = QBrush(Qt.HorPattern)       # horizental
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush = QBrush(Qt.VerPattern)       # veritical
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)

        brush = QBrush(Qt.BDiagPattern)     # 正斜杆对角
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()