import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Center')

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()  # 获取屏幕中点
        qr.moveCenter(cp)           # 将框架中心移到屏幕中点对齐
        self.move(qr.topLeft())     # 获取此时框架的左上位置点, 并将窗口移到此位置

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())