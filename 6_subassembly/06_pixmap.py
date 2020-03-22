import sys
from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PySide2.QtGui import QPixmap

class Example(QWidget):     # QMainWindow是QWidget的子类

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)    # setLayout(hbox) 已经将此对象指向self, 
                                    # 故此处可以省略self

        filePath = 'D:\Documents\Python\Git\Learn-PyQt5-with-ZetCode\\6_subassembly\\'
        pixmap = QPixmap(filePath + 'monkey.png')

        lbl = QLabel()
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('monkey')
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())