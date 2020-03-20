import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject

class Communicate(QObject):

    closeApp = pyqtSignal()     # 自定义信号, 相当于clicked

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.c = Communicate()
        # 将自定义信号closeApp与QMainWindow的close()方法绑定
        self.c.closeApp.connect(self.close)     

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Emit signal")
        self.show()

    def mousePressEvent(self, event):

        # 点击鼠标, 触发自定义信号closeApp发送
        self.c.closeApp.emit()      

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())