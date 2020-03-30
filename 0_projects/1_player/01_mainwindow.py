'''
教程地址:
https://www.zhihu.com/search?type=content&q=pyqt%20%E7%BE%8E%E5%8C%96
'''

import sys
import os
from PySide2.QtWidgets import QApplication, QProgressBar, QToolButton ,QLineEdit, QWidget, QGridLayout, QLabel, QMainWindow, QPushButton
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize, Qt
from qtawesome import icon,font

FILE_PATH = sys.path[0]     # 运行文件的目录


class MainUI(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.makeUp()

    def initUI(self):

        ## UI框架
        # main_widget
        self.main_widget = QWidget()        # 部件暂时不用传入self, 最后传入即可
        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(0)
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
        self.left_mini = QPushButton("")
        self.left_visit = QPushButton("")
        self.left_close = QPushButton("")

        self.left_label_1 = QPushButton("每日推介")
        self.left_label_1.setObjectName("left_label")
        self.left_label_2 = QPushButton("我的音乐")
        self.left_label_2.setObjectName("left_label")
        self.left_label_3 = QPushButton("联系与帮助")
        self.left_label_3.setObjectName("left_label")

        self.left_btn_1 = QPushButton(icon('fa.music', color='white'), "华语流行")
        self.left_btn_1.setObjectName("left_btn")
        self.left_btn_2 = QPushButton(icon('fa.sellsy', color='white'), "在线FM")
        self.left_btn_2.setObjectName("left_btn")
        self.left_btn_3 = QPushButton(icon('fa.film', color='white'), "热门MV")
        self.left_btn_3.setObjectName("left_btn")
        self.left_btn_4 = QPushButton(icon('fa.home', color='white'), "本地音乐")
        self.left_btn_4.setObjectName("left_btn")
        self.left_btn_5 = QPushButton(icon('fa.download', color='white'), "下载管理")
        self.left_btn_5.setObjectName("left_btn")
        self.left_btn_6 = QPushButton(icon('fa.heart', color='white'), "我的收藏")
        self.left_btn_6.setObjectName("left_btn")
        self.left_btn_7 = QPushButton(icon('fa.comment', color='white'), "反馈意见")
        self.left_btn_7.setObjectName("left_btn")
        self.left_btn_8 = QPushButton(icon('fa.star', color='white'), "关注我们")
        self.left_btn_8.setObjectName("left_btn")
        self.left_btn_9 = QPushButton(icon('fa.question', color='white'), "遇到问题")
        self.left_btn_9.setObjectName("left_btn")

        # 布置小部件
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)     # 位置 + 尺寸

        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)

        self.left_layout.addWidget(self.left_btn_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_btn_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_btn_3, 4, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)

        self.left_layout.addWidget(self.left_btn_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_btn_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_btn_6, 8, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)

        self.left_layout.addWidget(self.left_btn_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_btn_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_btn_9, 12, 0, 1, 3)
        
        ## right_layout
        # 部件1, search bar
        self.search_bar_widget = QWidget()
        self.search_bar_layout = QGridLayout()
        self.search_bar_widget.setLayout(self.search_bar_layout)

        self.search_bar_icon = QLabel(chr(0xf002) + " 搜索 ")
        self.search_bar_icon.setFont(font('fa', 16))
        self.search_bar_input = QLineEdit()
        self.search_bar_input.setPlaceholderText("输入歌手, 歌曲或用户, 回车进行搜索")

        self.search_bar_layout.addWidget(self.search_bar_icon, 0, 0, 1, 1)
        self.search_bar_layout.addWidget(self.search_bar_input, 0, 1, 1, 8)

        # 部件2, recommend
        self.recommend_label = QLabel("今日推介") 
        self.recommend_label.setObjectName('right_label')

        self.recommend_widget = QWidget()
        self.recommend_layout = QGridLayout()
        self.recommend_widget.setLayout(self.recommend_layout)

        self.recommend_btn_1= QToolButton()
        self.recommend_btn_1.setText("田馥甄")
        self.recommend_btn_1.setIcon(QIcon(FILE_PATH + '\\田馥甄.jpg'))
        self.recommend_btn_1.setIconSize(QSize(150, 150))
        self.recommend_btn_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.recommend_btn_2= QToolButton()
        self.recommend_btn_2.setText("张韶涵")
        self.recommend_btn_2.setIcon(QIcon(FILE_PATH + '\\张韶涵.jpg'))
        self.recommend_btn_2.setIconSize(QSize(150, 150))
        self.recommend_btn_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.recommend_btn_3 = QToolButton()
        self.recommend_btn_3.setText("Jay")
        self.recommend_btn_3.setIcon(QIcon(FILE_PATH + '\\jay.jpg'))
        self.recommend_btn_3.setIconSize(QSize(150, 150))
        self.recommend_btn_3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.recommend_btn_4 = QToolButton()
        self.recommend_btn_4.setText("Love Poem")
        self.recommend_btn_4.setIcon(QIcon(FILE_PATH + '\\lovepoem.jpg'))
        self.recommend_btn_4.setIconSize(QSize(150, 150))
        self.recommend_btn_4.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.recommend_btn_5= QToolButton()
        self.recommend_btn_5.setText("喜欢你")
        self.recommend_btn_5.setIcon(QIcon(FILE_PATH + '\\loveyou.jpg'))
        self.recommend_btn_5.setIconSize(QSize(150, 150))
        self.recommend_btn_5.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        self.recommend_layout.addWidget(self.recommend_btn_1, 0, 0, 1, 1)
        self.recommend_layout.addWidget(self.recommend_btn_2, 0, 1, 1, 1)
        self.recommend_layout.addWidget(self.recommend_btn_3, 0, 2, 1, 1)
        self.recommend_layout.addWidget(self.recommend_btn_4, 0, 3, 1, 1)
        self.recommend_layout.addWidget(self.recommend_btn_5, 0, 4, 1, 1)


        # 部件3, newsongs
        self.newsongs_label = QLabel("最新歌曲")
        self.newsongs_label.setObjectName("right_label")

        self.newsongs_widget = QWidget()
        self.newsongs_layout = QGridLayout()
        self.newsongs_widget.setLayout(self.newsongs_layout)

        self.newsongs_btn_1 = QPushButton("夜机     陈慧娴      永远的朋友      3:29")
        self.newsongs_btn_2 = QPushButton("夜机     陈慧娴      永远的朋友      3:29")
        self.newsongs_btn_3 = QPushButton("夜机     陈慧娴      永远的朋友      3:29")
        self.newsongs_btn_4 = QPushButton("夜机     陈慧娴      永远的朋友      3:29")
        self.newsongs_btn_5 = QPushButton("夜机     陈慧娴      永远的朋友      3:29")
        self.newsongs_btn_6 = QPushButton("夜机     陈慧娴      永远的朋友      3:29")

        self.newsongs_layout.addWidget(self.newsongs_btn_1, 0, 0)
        self.newsongs_layout.addWidget(self.newsongs_btn_2, 1, 0)
        self.newsongs_layout.addWidget(self.newsongs_btn_3, 2, 0)
        self.newsongs_layout.addWidget(self.newsongs_btn_4, 3, 0)
        self.newsongs_layout.addWidget(self.newsongs_btn_5, 4, 0)
        self.newsongs_layout.addWidget(self.newsongs_btn_6, 5, 0)

        # 部件4, playlist
        self.playlist_label = QLabel("热门歌单")
        self.playlist_label.setObjectName("right_label")

        self.playlist_widget = QWidget()
        self.playlist_layout = QGridLayout()
        self.playlist_widget.setLayout(self.playlist_layout)

        self.playlist_btn_1 = QToolButton()
        self.playlist_btn_1.setText("留我独自在湖面成双")
        self.playlist_btn_1.setIcon(QIcon(FILE_PATH + "\\playlist\\alone.jpg"))
        self.playlist_btn_1.setIconSize(QSize(100, 100))
        self.playlist_btn_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.playlist_btn_2 = QToolButton()
        self.playlist_btn_2.setText("让人陷入回忆的老歌")
        self.playlist_btn_2.setIcon(QIcon(FILE_PATH + "\\playlist\\classic.jpg"))
        self.playlist_btn_2.setIconSize(QSize(100, 100))
        self.playlist_btn_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.playlist_btn_3 = QToolButton()
        self.playlist_btn_3.setText("专注力百分百歌单..")
        self.playlist_btn_3.setIcon(QIcon(FILE_PATH + "\\playlist\\learning.jpg"))
        self.playlist_btn_3.setIconSize(QSize(100, 100))
        self.playlist_btn_3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.playlist_btn_4 = QToolButton()
        self.playlist_btn_4.setText("就像静静地看着你..")
        self.playlist_btn_4.setIcon(QIcon(FILE_PATH + "\\playlist\\quiet.jpg"))
        self.playlist_btn_4.setIconSize(QSize(100, 100))
        self.playlist_btn_4.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.playlist_layout.addWidget(self.playlist_btn_1, 0, 0)
        self.playlist_layout.addWidget(self.playlist_btn_2, 0, 1)
        self.playlist_layout.addWidget(self.playlist_btn_3, 1, 0)
        self.playlist_layout.addWidget(self.playlist_btn_4, 1, 1)

        # 部件5, process_bar
        self.process_bar = QProgressBar()
        self.process_bar.setValue(49)
        self.process_bar.setFixedHeight(3)
        self.process_bar.setTextVisible(False)

        # 部件6, play_console
        self.play_console_widget = QWidget()
        self.play_console_layout = QGridLayout()
        self.play_console_widget.setLayout(self.play_console_layout)

        self.play_console_btn_1 = QPushButton(icon('fa.backward', color="#F76677"), '')
        self.play_console_btn_2 = QPushButton(icon('fa.pause', color="#F76677"), '')
        self.play_console_btn_2.setIconSize(QSize(30, 30))
        self.play_console_btn_3 = QPushButton(icon('fa.forward', color="#F76677"), '')

        self.play_console_layout.addWidget(self.play_console_btn_1, 0, 0)     # 部件尺寸一致时可省略(0, 0, 1, 1)
        self.play_console_layout.addWidget(self.play_console_btn_2, 0, 1)
        self.play_console_layout.addWidget(self.play_console_btn_3, 0, 2)
        self.play_console_layout.setAlignment(Qt.AlignCenter)       # 居中显示
        
        # 将6个小部件布置到right_widget
        self.right_layout.addWidget(self.search_bar_widget, 0, 0, 1, 9)
        self.right_layout.addWidget(self.recommend_label, 1, 0, 1, 9)
        self.right_layout.addWidget(self.recommend_widget, 2, 0, 1, 9)
        self.right_layout.addWidget(self.newsongs_label, 3, 0, 1, 5)
        self.right_layout.addWidget(self.newsongs_widget, 4, 0, 4, 5)
        self.right_layout.addWidget(self.playlist_label, 3, 5, 1, 4)    # 前两个从0计数, 后两个从1计数
        self.right_layout.addWidget(self.playlist_widget, 4, 5, 4, 4)
        self.right_layout.addWidget(self.process_bar, 9, 0, 1, 9)
        self.right_layout.addWidget(self.play_console_widget, 10, 0, 1, 9)

        self.setFixedSize(1200, 800)
        self.setWindowOpacity(0.95)
        self.setAttribute(Qt.WA_TranslucentBackground)      # ? 设置窗口背景透明, 变为黑色(默认窗口背景为黑色)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.show()

    def makeUp(self):

        ## left
        self.left_mini.setFixedSize(20, 20)
        self.left_visit.setFixedSize(20, 20)
        self.left_close.setFixedSize(20, 20)

        self.left_mini.setStyleSheet('''
            QPushButton{
                background: #6DDF6D;
                border-radius: 5px;
            }
            QPushButton:hover{
                background: green;
            }
        ''')

        self.left_visit.setStyleSheet('''
            QPushButton{
                background: #F7D674;
                border-radius: 5px;
            }
            QPushButton:hover{
                background: yellow;
            }
        ''')

        self.left_close.setStyleSheet('''
            QPushButton{
                background: #F76677;
                border-radius: 5px;
            }
            QPushButton:hover{
                background: red;
            }
        ''')

        self.left_widget.setStyleSheet('''
            QPushButton{
                border: none;
                color: white;
                height: 30px;
            }
            QPushButton#left_label{
                border: none;
                border-bottom: 1px solid white;
                font-size: 18px;
                font-weight: 700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_btn:hover{
                border-left: 6px solid red;
                font-weight: 700;
            }
            QWidget#left_widget{
                background: gray;
                border-top: 1px solid white;
                border-left: 1px solid white;
                border-bottom: 1px solid white;
                border-top-left-radius: 10px;
                border-bottom-left-radius: 10px;
            }
        ''')    # font-weight, 字体粗度. border-radius, border-bottom
                # 选择器QWidget会选出自身及所有子类

        ## right
        self.search_bar_input.setStyleSheet('''
            QLineEdit{
                border: 1px solid gray;
                width: 300px;
                border-radius: 10px;
                padding: 2px 4px;
            }
        ''')        # 区别css, #代表一类, 而非唯一ID
 
        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color: #232c51;
                background: white;
                border-top: 1px solid darkGray;
                border-right: 1px solid darkGray;
                border-bottom: 1px solid darkGray;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
            }
            QLabel#right_label{
                border: none;
                font-size: 16px;
                font-weight: 700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')        # right_widget中含有很多QWidget, 需要靠#属性筛选. 

        self.recommend_widget.setStyleSheet('''
            QToolButton{
                border: none;
            }
            QToolButton:hover{
                border-bottom: 2px solid #F76677;
            }
        ''')

        self.playlist_widget.setStyleSheet('''
            QToolButton{
                border: none;
            }
            QToolButton:hover{
                border-bottom: 2px solid #F76677;
            }
        ''')        # 边框去掉, 才可显示hover. 各部分分开设置, 解耦.

        self.newsongs_widget.setStyleSheet('''
            QPushButton{
                border: none;
                color: gray;
                font-size: 18px;
                height: 40px;
                padding-left: 40px;
                padding-right: 10px;
                text-align: left;
            }
            QPushButton:hover{
                color: black;
                border: 1px solid #F3F3F5;
                border-radius: 10px;
                background: LightGray;
            }
        ''')

        self.process_bar.setStyleSheet('''
            QProgressBar::chunk{
                background-color: #F76677;
            }
        ''')

        self.play_console_widget.setStyleSheet('''
            QPushButton{
                border:none;
            }
        ''')


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main_ui = MainUI()
    app.exec_()
