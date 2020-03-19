import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        iconFile = 'D:\Documents\Python\Git\Learn-PyQt5-with-ZetCode\menu\exit.png'
        exitAct = QAction(QIcon(iconFile), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')      # 将工具小条Exit加到bar
        self.toolbar.addAction(exitAct)             # 将动作关联到工具小条

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Toolbar")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())