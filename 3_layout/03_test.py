import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        button_1 = QPushButton('0-0')
        grid.addWidget(button_1, 0, 0)
        button_2 = QPushButton('9-9')
        grid.addWidget(button_2, 9, 9)

        button_3 = QPushButton('5-5')
        grid.addWidget(button_3, 5, 5)
        button_4 = QPushButton('5-6')
        grid.addWidget(button_4, 5, 6)

        # 总结
        # 9 x 9 网格
        # 整行都没有按钮的, 此行自动压缩为空

        # self.setLayout(grid)
        # 只要将grid布局设置到self就行, 或者说将self布局设置为grid

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Calculator")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())