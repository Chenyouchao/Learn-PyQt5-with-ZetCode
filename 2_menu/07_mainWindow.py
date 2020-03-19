'''
    main window = menubar, toolbar, statusbar, and a central widget.
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        iconFile = 'D:\Documents\Python\Git\Learn-PyQt5-with-ZetCode\menu\exit.png'
        exitAct = QAction(QIcon(iconFile), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip("Exit application")
        exitAct.triggered.connect(self.close)

        self.statusBar()    # 无需向statusBar上再添加部件

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar("Exit")
        toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Main window")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())