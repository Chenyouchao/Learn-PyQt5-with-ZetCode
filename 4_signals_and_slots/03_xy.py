import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        # 初始化label为(0, 0)
        x = 0 
        y = 0
        self.text = "x: {0}, y: {1}".format(x, y)   # 对比%(x, y)
        self.label = QLabel(self.text, self)

        grid.addWidget(self.label, 0, 0, Qt.AlignTop)   # 顶行
        self.setMouseTracking(True)     # 追踪鼠标(无需点击)
        # self.setMouseTracking(False)      # 追踪鼠标(需按下左键或右键), 默认为False  
        self.setLayout(grid)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Event object")
        self.show()

    def mouseMoveEvent(self, event):

        x = event.x()
        y = event.y()

        self.text = "x: %d, y: %d" % (x, y)

        self.label.setText(self.text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())