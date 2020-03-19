import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, qApp

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Context menu")
        self.show()

    # 原生信号与槽
    def contextMenuEvent(self, event):
        cmenu = QMenu()     # 直接新建菜单. 
                            # 区别于02, menuBar = self.menuBar(), 再往bar上addMenu
        
        # 总结: bar ----> menu -----> action
        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("open")
        quitAct = cmenu.addAction("Quit")
        
        # action = cmenu.exec_()
        action = cmenu.exec_(self.mapToGlobal(event.pos()))     # 设置菜单执行位置为pos()
                                                                # 返回执行的Action

        if action == quitAct:
            qApp.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())