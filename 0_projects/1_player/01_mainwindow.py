'''
教程地址:
https://www.zhihu.com/search?type=content&q=pyqt%20%E7%BE%8E%E5%8C%96
'''

import sys
import os
from PySide2.QtWidgets import QApplication, QToolButton ,QLineEdit, QWidget, QGridLayout, QLabel, QMainWindow, QPushButton
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize, Qt
from qtawesome import icon,font

FILE_PATH = sys.path[0]     # 运行文件的目录

class MainUI(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        ## UI框架
        # main_widget
        self.main_widget = QWidget()        # 部件暂时不用传入self, 最后传入即可
        self.main_layout = QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        # left_widget
        self.left_widget = QWidget()
        self.left_widget.setObjectName('left_widget')       # 类比css的.class
        self.left_layout = QGridLayout()
        self.left_widget.setLayout(self.left_layout)

        # right_widget
        self.right_widget = QWidget()
        self.right_widget.setObjectName("right_widget")
        self.right_layout = QGridLayout()
        self.right_widget.setLayout(self.right_layout)

        # 整体布局
        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)
        self.setCentralWidget(self.main_widget)     # 具有指向self的功能

        ## left_layout
        # 创建小部件
        self.left_close = QPushButton("")
        self.left_visit = QPushButton("")
        self.left_mini = QPushButton("")

        self.left_label_1 = QPushButton("每日推介")
        self.left_label_1.setObjectName("left_label")
        self.left_label_2 = QPushButton("我的音乐")
        self.left_label_2.setObjectName("left_label")
        self.left_label_3 = QPushButton("联系与帮助")
        self.left_label_3.setObjectName("left_label")

        self.left_botton_1 = QPushButton(icon('fa.music', color='white'), "华语流行")
        self.left_botton_2 = QPushButton(icon('fa.sellsy', color='white'), "在线FM")
        self.left_botton_3 = QPushButton(icon('fa.film', color='white'), "热门MV")
        self.left_botton_4 = QPushButton(icon('fa.home', color='white'), "本地音乐")
        self.left_botton_5 = QPushButton(icon('fa.download', color='white'), "下载管理")
        self.left_botton_6 = QPushButton(icon('fa.heart', color='white'), "我的收藏")
        self.left_botton_7 = QPushButton(icon('fa.comment', color='white'), "反馈意见")
        self.left_botton_8 = QPushButton(icon('fa.star', color='white'), "关注我们")
        self.left_botton_9 = QPushButton(icon('fa.question', color='white'), "遇到问题")

        # 布置小部件
        self.left_layout.addWidget(self.left_close, 0, 0, 1, 1)     # 位置 + 尺寸
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_mini, 0, 2, 1, 1)

        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)

        self.left_layout.addWidget(self.left_botton_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_botton_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_botton_3, 4, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)

        self.left_layout.addWidget(self.left_botton_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_botton_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_botton_6, 8, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)

        self.left_layout.addWidget(self.left_botton_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_botton_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_botton_9, 12, 0, 1, 3)
        
        ## right_layout
        # search bar
        self.search_bar_widget = QWidget()
        self.search_bar_layout = QGridLayout()
        self.search_bar_widget.setLayout(self.search_bar_layout)

        self.search_bar_icon = QLabel(chr(0xf002) + " 搜索 ")
        self.search_bar_icon.setFont(font('fa', 16))
        self.search_bar_input = QLineEdit()
        self.search_bar_input.setPlaceholderText("输入歌手, 歌曲或用户, 回车进行搜索")

        self.search_bar_layout.addWidget(self.search_bar_icon, 0, 0, 1, 1)
        self.search_bar_layout.addWidget(self.search_bar_input, 0, 1, 1, 8)

        # recommend
        self.recommend_label = QLabel("今日推介") 
        self.recommend_label.setObjectName('right_label')

        self.recommend_widget = QWidget()
        self.recommend_layout = QGridLayout()
        self.recommend_widget.setLayout(self.recommend_layout)

        self.recommend_button_1= QToolButton()
        self.recommend_button_1.setText("田馥甄")
        self.recommend_button_1.setIcon(QIcon(FILE_PATH + '\\田馥甄.jpg'))
        self.recommend_button_1.setIconSize(QSize(150, 150))
        self.recommend_button_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.recommend_button_2= QToolButton()
        self.recommend_button_2.setText("张韶涵")
        self.recommend_button_2.setIcon(QIcon(FILE_PATH + '\\张韶涵.jpg'))
        self.recommend_button_2.setIconSize(QSize(150, 150))
        self.recommend_button_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.recommend_button_3 = QToolButton()
        self.recommend_button_3.setText("Jay")
        self.recommend_button_3.setIcon(QIcon(FILE_PATH + '\\jay.jpg'))
        self.recommend_button_3.setIconSize(QSize(150, 150))
        self.recommend_button_3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.recommend_button_4 = QToolButton()
        self.recommend_button_4.setText("Love Poem")
        self.recommend_button_4.setIcon(QIcon(FILE_PATH + '\\lovepoem.jpg'))
        self.recommend_button_4.setIconSize(QSize(150, 150))
        self.recommend_button_4.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.recommend_button_5= QToolButton()
        self.recommend_button_5.setText("喜欢你")
        self.recommend_button_5.setIcon(QIcon(FILE_PATH + '\\loveyou.jpg'))
        self.recommend_button_5.setIconSize(QSize(150, 150))
        self.recommend_button_5.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        self.recommend_layout.addWidget(self.recommend_button_1, 0, 0, 1, 1)
        self.recommend_layout.addWidget(self.recommend_button_2, 0, 1, 1, 1)
        self.recommend_layout.addWidget(self.recommend_button_3, 0, 2, 1, 1)
        self.recommend_layout.addWidget(self.recommend_button_4, 0, 3, 1, 1)
        self.recommend_layout.addWidget(self.recommend_button_5, 0, 4, 1, 1)

        # 布置部件seach_bar 和 recommend
        self.right_layout.addWidget(self.search_bar_widget, 0, 0, 1, 9)
        self.right_layout.addWidget(self.recommend_label, 1, 0, 1, 9)
        self.right_layout.addWidget(self.recommend_widget, 2, 0, 1, 9)

        self.setFixedSize(1200, 800)
        # self.resize(1200, 800)
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main_ui = MainUI()
    app.exec_()
