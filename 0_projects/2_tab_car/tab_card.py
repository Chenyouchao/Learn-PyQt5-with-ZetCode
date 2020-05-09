# https://www.cnblogs.com/jyroy/p/9457882.html

import sys
import os

from PySide2.QtCore import QUrl, QSize, Qt
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QApplication, QHBoxLayout, QWidget, QListWidget, QListWidgetItem, QStackedWidget

PATH = os.path.dirname(sys.argv[0])


class LeftTabWidget(QWidget):

    def __init__(self):
        super().__init__()

        with open(PATH + '/tab_card.qss', 'r') as f:
            self.list_style = f.read()

        self.init_ui()

    def init_ui(self):

        self.main_layout = QHBoxLayout(self, spacing=0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # 左侧选项列表
        self.left_widget = QListWidget()    
        self.left_widget.setStyleSheet(self.list_style)
        self.main_layout.addWidget(self.left_widget)

        # 右侧
        self.right_widget = QStackedWidget()
        self.main_layout.addWidget(self.right_widget)

        # 关联
        self.left_widget.currentRowChanged.connect(self.right_widget.setCurrentIndex)    # 左侧按钮与右侧窗口绑定

        self.left_widget.setFrameShape(QListWidget.NoFrame)
        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str = ['项目参考', '百度', 'bilibili', '腾讯网']
        url_list = ['https://www.cnblogs.com/jyroy/p/9457882.html', 
                    'https://www.baidu.com/', 
                    'https://www.bilibili.com/', 
                    'https://www.qq.com']

        for i in range(4):
            self.item = QListWidgetItem(list_str[i], self.left_widget)
            self.item.setSizeHint(QSize(30, 60))
            self.item.setTextAlignment(Qt.AlignCenter)    # 居中显示

            self.brower = QWebEngineView()
            self.brower.setUrl(QUrl(url_list[i]))
            self.right_widget.addWidget(self.brower)

        self.setObjectName('LeftTabWidget')
        self.setWindowTitle('LeftTabWidget')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = LeftTabWidget()
    win.show()

    app.exec_()
