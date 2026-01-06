from flask import Flask  #從flask套件，放進Flask這個類別
app=Flask(__name__) # __name__代表目前執行的模組
#這行程式碼是在告訴 Flask：「請以當前這個檔案所在的目錄作為起點，去尋找我的相關資源。」
@app.route("/") #函式的裝飾(decorator):以函式為基礎，提供附加的功能
# 例如這個是建立路由器，當連接到網址的最底層(/後方無東西)，執行下面的函式
def home():
	return "HI HAHAHA"
	
if __name__ == "__main__":
	app.run()