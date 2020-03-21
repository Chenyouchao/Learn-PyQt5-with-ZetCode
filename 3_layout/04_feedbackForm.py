import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, 
                             QTextEdit, QLineEdit, QLabel)
from QCandyUi.CandyWindow import colorful
# from QCandyUi import CandyWindow

@colorful("pink")
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()     # ? 通过grid布局加入self, 故可省略self, 6.04
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 1)         # 统一从1计数, 或从0计数, 效果一样
        grid.addWidget(titleEdit, 1, 2)

        grid.addWidget(author, 2, 1)
        grid.addWidget(authorEdit, 2, 2)

        grid.addWidget(review, 3, 1)
        grid.addWidget(reviewEdit, 3, 2, 5, 2)

        self.setLayout(grid)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Review")
        # self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    # ex = CandyWindow.createWindow(ex, 'blue')
    ex.show()       # 调用QCandyUi需将show()写到类外, 否则窗口会隐藏
    sys.exit(app.exec_())