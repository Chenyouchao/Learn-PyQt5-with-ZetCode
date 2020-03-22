import sys
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        self.lbl.move(60, 40)
        qle.move(60, 100)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("QLineEdit")
        self.show()

    def onChanged(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()   # 自动调整label大小

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())