import sys
from PySide2.QtWidgets import (QApplication, QWidget, QHBoxLayout, 
QFrame, QSplitter, QStyleFactory)
from PySide2.QtCore import Qt   # 数据类型; Qt布局方向

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout()

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        # topleft.setFrameShape(QFrame.Shadow)    # ? 报错
        
        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)    # 横向增加部件
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("QSplitter")
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
