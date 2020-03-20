import sys
from PyQt5.QtWidgets import (QApplication, QWidget, 
    QVBoxLayout, QSlider, QLCDNumber)
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        lcd = QLCDNumber(self)      # ? QLineEdit(), 无self
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("QLCDNumber")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())