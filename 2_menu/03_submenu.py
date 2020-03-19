import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')  # 向菜单栏添加菜单

        impMenu = QMenu('Import', self)     # 新建菜单对象
        impAct = QAction('Import mail', self)   # 动作要指向QMainWindow
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Submenu')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())