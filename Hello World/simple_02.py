import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')

        # ? 非绝对路径, 图标显示异常
        self.setWindowIcon(QIcon('D:\Documents\Python\Git\Learn-PyQt5-with-ZetCode\Hello World\web.png'))

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 若直接写为：Example(), 由于没有指向对象的标识符, 
    # 对象会被回收, 所以窗口一闪而过. 
    ex = Example()

    sys.exit(app.exec_())