import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class Example(QWidget):
    def __init__(self):
        # __init__()被重写, 保证集成父类构造器
        # 相当于QObject.__init__(self), 这里的self是子类QWidget的实例
        super().__init__()  # 此处可省略self

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