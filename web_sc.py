import webbrowser, sys, pyperclip
from urllib.parse import quote

# 指定した URL を開く
#webbrowser.open('https://inventwithpython.com/')

# コマンドライン引数をリストで取得する
# 例：python3 web_sc.py 東京都新宿区
# sys.argv = ['web_sc.py', '東京都新宿区']
if len(sys.argv) > 1:
    # 指定したファイル以降のものをスペースで結合
    # sys.argv = ['web_sc.py', '東京都', '新宿区']
    address = ' '.join(sys.argv[1:]) 
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + quote(address))

print('https://www.google.com/maps/place/' + address)