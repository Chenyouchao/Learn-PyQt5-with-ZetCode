import sys
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout

class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)     # 省略self

        self.setAcceptDrops(True)   # 2. 允许拖动放入

    # 重构button的拖拽方法
    def dragEnterEvent(self, e):

        # e: PySide2.QtGui.QDragEnterEvent Object
        # 当有部件拖拽到button范围时, 触发
        if e.mimeData().hasFormat('text/plain'):        # mime相当于剪切板
            e.accept()
            # print(e)
        else:
            e.ignore()

    def dropEvent(self, e):

        # e: PySide2.QtGui.QDropEvent object
        self.setText(e.mimeData().text())

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout()

        edit = QLineEdit('', self)
        edit.setDragEnabled(True)       # 1. 允许被拖动
        hbox.addWidget(edit)

        button = Button('Button', self)
        hbox.addWidget(button)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Simple drag and drop")
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()