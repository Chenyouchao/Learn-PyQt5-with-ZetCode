import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
QPushButton, QLabel, QFontDialog, QSizePolicy)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()    # 不设置布局, label不会自动调整, 导致显示不全

        btn = QPushButton('Dialog', self)

        # 改变布局策略, 横纵尺寸都固定为sizeHint()
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        btn.move(20, 20)
        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):

        font, ok = QFontDialog.getFont()    # 同QInputDialog.getText(), 失败返回空
        if ok:
            self.lbl.setFont(font)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())