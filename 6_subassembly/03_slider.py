import sys
from PySide2.QtWidgets import QApplication, QWidget, QSlider, QLabel, QHBoxLayout
from PySide2.QtCore import Qt   # 搭配QSlider
from PySide2.QtGui import QPixmap   # 将图片转换为Pixmap, 再用label显示

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout()

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)      # 取消选中sld (默认选中, 可直接用方向键调节)
        # sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
        hbox.addWidget(sld)

        self.filePath = 'D:\Documents\Python\Git\Learn-PyQt5-with-ZetCode\\6_subassembly\\'
        
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap(self.filePath + 'mute.png'))
        # self.label.setGeometry(160, 40, 80, 30)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("QSlider")
        self.show()

    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap(self.filePath + 'mute.png'))
        elif value <= 30:
            self.label.setPixmap(QPixmap(self.filePath + 'min.png'))
        elif value <= 80:
            self.label.setPixmap(QPixmap(self.filePath + 'med.png'))
        else:
            self.label.setPixmap(QPixmap(self.filePath + 'max.png'))

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())