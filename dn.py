import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

# 其實就是用PyQt 做一個簡易的瀏覽器 
# 單純使用這個的話 一樣是沒辦法瀏覽Flash的
# QtWebEngine使用的是chrome的內核 所以要安裝一個對應的Flash包
# Flash包跟這個腳本放在同一個目錄下 記得先安裝
# 安裝好後 編譯這個腳本 就可以開始用, !別使用UPX 不然打不開!

title = "Flash遊戲萬能登入器" # 改成你要的Flash網頁遊戲名稱
login = "http://example.com" # 改成Flash網頁遊戲登入頁網址

# 解析度設定, 按照個人喜好 或是Flash遊戲的畫面去調整
x = 1280 
y = 720

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, x, y)

        self.browser = QWebEngineView()
        settings = self.browser.settings()
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.setCentralWidget(self.browser)

        # 加載Flash文件
        self.browser.setUrl(QUrl(login))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
