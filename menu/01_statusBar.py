import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        # 重写构造器的目的
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Status Bar")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())