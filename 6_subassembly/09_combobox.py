import sys
from PySide2.QtWidgets import QApplication, QWidget, QComboBox, QLabel

class EXample(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lbl = QLabel("Ubuntu", self)   # 设置Label默认值

        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("QComboBox")
        self.show()

    def onActivated(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = EXample()
    sys.exit(app.exec_())