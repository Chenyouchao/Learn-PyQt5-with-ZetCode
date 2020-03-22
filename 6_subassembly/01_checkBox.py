import sys
from PySide2.QtWidgets import QApplication, QWidget, QCheckBox
from PySide2.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()     # 选中checkBox
        cb.stateChanged.connect(self.changeTitle)
        # checkBox, 带参数信号

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle("QCheckBox")
        else:
            self.setWindowTitle(' ')

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())