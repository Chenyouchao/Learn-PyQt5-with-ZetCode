import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtCore import Qt, QMimeData
from PySide2.QtGui import QDrag

class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):

        if e.buttons() != Qt.RightButton:   # 联系Qt.Horizontal, 6.08
            return
        # if-return, 相当于if-else

        # 鼠标移动时, 应产生mime数据(拖放中传输的数据)
        # 用于QWidget的拖动释放时, 传输mime数据
        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())    # 光标位置
        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):

        # 父类也调用了mousePressEvent()方法
        # 负责, 看不到按钮按下的效果
        super().mousePressEvent(e)

        if e.button() == Qt.LeftButton:
            print('press')

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setAcceptDrops(True)

        self.button = Button("Button", self)
        self.button.move(100, 65)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("click of move")
        self.show()

    def dragEnterEvent(self, e):

        e.accept()

    def dropEvent(self, e):

        position = e.pos()
        self.button.move(position)

        # 指定释放动作为move模式
        e.setDropAction(Qt.MoveAction)
        # e.accept()    # ?

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()