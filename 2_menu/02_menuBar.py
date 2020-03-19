import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
# from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        iconFile = 'D:\Documents\Python\Git\Learn-PyQt5-with-ZetCode\menu\exit.png'
        exitAct = QAction(QIcon(iconFile), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')    # 区别于setToolTip()
        exitAct.triggered.connect(qApp.quit)
        # exitAct.triggered.connect(QCoreApplication.instance().quit)
        # qApp, a global pointer, equivalent to QCoreApplication.instance()

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.statusBar()

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Simple Menu')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())