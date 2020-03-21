import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QColorDialog, 
                                QFrame, QPushButton)
from PyQt5.QtGui import QColor      # Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        col = QColor(0, 0, 0)

        self.btn = QPushButton("Dialog", self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget{ background-color: %s }" 
                                % col.name())   # 类似css
        self.frm.setGeometry(140, 20, 100, 100)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):

        col = QColorDialog.getColor()   # 区别, QInputDialog自动返回ok
        
        if col.isValid():
            self.frm.setStyleSheet('QWidget{ background-color: %s }' 
                                    % col.name())

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())