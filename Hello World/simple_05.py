import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Message Box")
        self.show()

    # 此槽函数已经默认与关闭窗口信号相连接(连接已经存在), 此处做了重写
    # 如果关闭QWidget, 就会产生一个QCloseEvent, 作为信号参数传给event
    # 过程:
    # 1. 关闭按钮被点击
    # 2. 发出信号(带参数), 触发连接
    # 3. 调槽函数(传参数)
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", 
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())