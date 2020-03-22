import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QColor, QFont
from PySide2.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.text = "Лев Николаевич Толстой\nАнна Каренина"

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Drawing text")
        self.show()

    # 信号: 窗口变动
    def paintEvent(self, event):

        qp = QPainter()     # 画家, 低级绘画类
        # 加入self后print, QPainter::begin: Painter already active

        qp.begin(self)      # 不可省略self
        self.drawText(event, qp)
        qp.end()            # 不可添加self

        # print(event)

    # 重写drawText方法
    def drawText(self, event, qp):

        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()