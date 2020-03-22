import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton
from PySide2.QtCore import QBasicTimer

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()

        self.pbar = QProgressBar()      # 3.04 加入布局可省略self !!!
        # self.pbar.setGeometry(30, 40, 200, 25)
        vbox.addWidget(self.pbar)

        self.btn = QPushButton('Start')
        # self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)     # 6.02 对比click[bool]
        vbox.addWidget(self.btn)

        self.setLayout(vbox)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('QPressBar')
        self.show()

    # 重写原生槽函数. 没过一个单位时间, 执行一次
    def timerEvent(self, event):

        # 到达100%时, 即便点了按钮, 也会马上变为Finished
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)     # 绑定self, 为self及时, 时限100s
            self.btn.setText('Stop')

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())