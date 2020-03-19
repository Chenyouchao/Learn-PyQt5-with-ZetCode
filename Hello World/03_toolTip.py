import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()  # 父类.方法(), 自动传入self指向实例

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))    # 静态方法, 类名.方法()

        self.setToolTip('This is a <b>QWidget</b> widget')  # 提示小工具

        btn = QPushButton('Button', self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())      # 默认尺寸
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())