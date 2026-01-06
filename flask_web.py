from datetime import datetime
import os
from flask import Flask  #從flask套件，放進Flask這個類別
web=Flask(__name__) # __name__代表目前執行的模組
#這行程式碼是在告訴 Flask：「請以當前這個檔案所在的目錄作為起點，去尋找我的相關資源。」
@web.route("/") #函式的裝飾(decorator):以函式為基礎，提供附加的功能
# 例如這個是建立路由器，當連接到網址的最底層(/後方無東西)，執行下面的函式
def home():
	current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return f"<p>這是我第一個挑戰成功的網站喔ww</p><p>你看網址，是不是蝦蝦愛貓咪~</p><p>給你一個大大的啾啾！</p>"
	
if __name__ == "__main__":
	port = int(os.environ.get("PORT",5000))
	web.run(host="0,0,0,0",port=port)