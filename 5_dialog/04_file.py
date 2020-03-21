import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, 
QTextEdit, QFileDialog)
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()     # ? 无self
        self.setCentralWidget(self.textEdit)    # 居中显示, 对比hello_world中的center
        self.statusBar()

        icon = 'D:\Documents\Python\Git\Learn-PyQt5-with-ZetCode\\5_dialog\open.png'
        openFile = QAction(QIcon(icon), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()        # ? QMainDialog的方法, 所以不用self
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        # 区别, input, font, color 无self
        # 参数: 标题, 默认路径
        # 返回元组: ('D:/Documents/记事本.txt', 'All Files (*)')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())