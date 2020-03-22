import sys
from PySide2.QtWidgets import QApplication, QWidget, QFrame, QPushButton
from PySide2.QtGui import QColor

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0)

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)
        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)        # 把这个按钮变为切换按钮(类似checkBox)
        blueb.move(10, 100)
        blueb.clicked[bool].connect(self.setColor)  # True, False切换

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                    self.col.name())
        
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Toggle button")
        self.show()

    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        # >< 金字塔范围
        # == case
        if source.text() == 'Red':
            self.col.setRed(val)
        elif source.text() == 'Green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" 
                                    % self.col.name())
        '''
            分析: rgb三者分开设置, 互不干扰

            QFrame{
                background-color: red;
                background-color: green;
                background-color: blue;
            }
        '''

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())