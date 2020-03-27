import os
import sys
import datetime
from PySide2.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QHBoxLayout
from PySide2.QtCore import Qt, QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 创建tabwidget
        self.tabWidget = QTabWidget()
        # self.tabWidget.setTabShape(QTabWidget.Triangular)     
        # self.tabWidget.setDocumentMode(True)
        # self.tabWidget.setMovable(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.setCentralWidget(self.tabWidget)   # 也又指向self的作用

        self.brower = WebEngineView(self)   # 必须有self(指向不明不可用layout指定parent), 实际传入self.brower, self
        self.brower.load(QUrl("http://www.baidu.com"))
        self.createTab(self.brower)

        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(300, 300, 600, 400)
        self.showMaximized()
        self.setWindowTitle("My Brower")
        # self.show()
 
    def createTab(self, brower):

        # 将widget变为标签页的形式
        self.tab = QWidget()
        self.tabWidget.addTab(self.tab, "新标签页")
        self.tabWidget.setCurrentWidget(self.tab)       # 设置为当前标签呀
        
        self.tab_layout = QHBoxLayout(self.tab)
        # self.tab_layout.setContentsMargins(0, 0, 0, 0)
        self.tab_layout.addWidget(brower)
        # brower无指向, 长在tab上, tab又add到tabWidget, 

    def closeTab(self, index):

        if self.tabWidget.count() > 1:
            self.tabWidget.removeTab(index)
        else:
            self.close()

class WebEngineView(QWebEngineView):

    def __init__(self, parent=None):    
        super().__init__(parent)    # 实际是(self, parent)

        self.mainwindow = parent

        # self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        # self.page().windowCloseRequested.connect(self.onWindowCloseRequested)
        self.page().profile().downloadRequested.connect(self.onDownloadRequested)

    # def onWindowCloseRequested(self):

    #     the_index = self.mainwindow.tabWidget.currentIndex()
    #     self.mainwindow.tabWidget.removeTab(the_index)

    # 下载文件
    def onDownloadRequested(self, downloadItem):

        if downloadItem.isFinished() is False and downloadItem.state() == 0:

            the_filename = downloadItem.url().fileName()
            
            if len(the_filename) == 0 or "." not in the_filename:
                cur_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                the_filename = "下载文件" + cur_time + ".xls"

            the_source_file = os.path.join(os.getcwd(), the_filename)

            downloadItem.setPath(the_source_file)
            downloadItem.accept()
            downloadItem.finished.connect(self.onDownloadFinished)

    # 弹出提示
    def onDownloadFinished(self):

        js_string = '''
                    alert("下载成功!")
                    '''
        self.page().runJavaScript(js_string)

    # 原生槽, brower的重写
    def createWindow(self, event):

        new_web_page = WebEngineView(self.mainwindow)

        self.mainwindow.createTab(new_web_page)

        return new_web_page     # 返回网页内容


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mw = MainWindow()
    app.exec_()