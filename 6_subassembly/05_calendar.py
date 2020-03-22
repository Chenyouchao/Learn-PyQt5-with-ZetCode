import sys
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
QCalendarWidget, QLabel)
from PySide2.QtCore import QDate    # QtCore 包含Qt数据类型

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)

        cal = QCalendarWidget()
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)
        vbox.addWidget(cal)

        self.lbl = QLabel()
        # lbl显示默认已选日期
        date = cal.selectedDate()       # 帕斯卡构造器, 驼峰方法
        self.lbl.setText(date.toString())
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):

        self.lbl.setText(date.toString())

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())