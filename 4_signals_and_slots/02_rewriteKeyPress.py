import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Event hander")
        self.show()

    # 键盘按下有很多不同的情况, event就是键盘发来的不同按击方式的信号
    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())