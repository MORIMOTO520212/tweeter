# -*- coding: utf-8 -*-
from time import sleep
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font
import emoji, sys
import tweepy
import threading

# ~ NOTE ~

#-ウィンドウサイズ指定-#
window_width = 500 # x
window_height = 200 # y

#-ツイート格納リスト-#
tweets = []

consumer_key='CONSUMER_KEY'
consumer_secret='CONSUMER_SECRET'
access_key='ACCESS_KEY'
access_secret='54Dqdt8Kx7CoVKq2XqOSoTsKkTI7liPtpPugaZjGrTbRK'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth_handler=auth)

#-検索ワード-#
trend_name = "最初の言語 exclude:retweets"
textnum = 0

#--ウィンドウ作成--#
root = Tk()
root.title("Tweeter1.2")

window_width = root.winfo_screenwidth() # x
window_height = root.winfo_screenheight() # y

x_place = window_width/2

root.configure(width=window_width, height=window_height, bg='#101922') #ウィンドウの大きさを指定
root.attributes("-fullscreen", True) # フルスクリーン
textfont = font.Font(size=23, weight="bold", family=("Arial", "ヒラギノ角ゴ Pro W3", "Hiragino Kaku Gothic Pro", "Osaka", "メイリオ", "Meiryo", "ＭＳ Ｐゴシック", "MS PGothic", "sans-serif"))
textfont2 = font.Font(size=18, weight="bold", family=("Arial", "ヒラギノ角ゴ Pro W3", "Hiragino Kaku Gothic Pro", "Osaka", "メイリオ", "Meiryo", "ＭＳ Ｐゴシック", "MS PGothic", "sans-serif"))
text = ttk.Label(root, text="Tweeter", font=textfont, wraplength=window_width/1.5, foreground='#FFFFFF' ,background='#101922')# padding=(幅, 高さ)

#--終了ボタン配置--#
def DeleteEntryValue():
    print("EXIT")
    sys.exit()
Button = tkinter.Button(text='EXIT', width=50) # #ffffff00
Button.bind("<Button-1>",DeleteEntryValue) 

#--ツイート内絵文字削除--#
def remove_emoji(src_str):
    return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI)

#--第一トレンドのツイート取得--#
def trend_tweet():
    global trend_name
    trend = api.trends_place(23424856)[0] # 日本のワールドID
    trends = trend['trends']
    #trend_name = trends[0]["name"] # トレンド名
    for status in api.search(q=trend_name, lang='ja', result_type='recent',count=100):
        textmain = remove_emoji(status.text)
        textmain = textmain.split('https')[0]
        #textmain = textmain.encode('shift_jis', errors='ignore')
        if len(textmain) < 40:
            tweets.append(textmain) # ツイートリスト
    return tweets
tweets = trend_tweet()

trend_text = ttk.Label(root, text="Search "+trend_name.replace("exclude:retweets",""), font=textfont2, foreground='#FFFFFF' ,background='#101922')# padding=(幅, 高さ)
trend_text.place(x=10, y=20, anchor='w') # anchor=文字列  オフセットの位置を指定する

# ツイート取得数
print("GET LENGTH: "+str(len(tweets)))

#--スレッド処理--#
def thread():
    global x_place, textnum, tweets

    def wisper_s():
        global text
        for i in range(5):
            if i == 0:
                text["foreground"] = '#1f2b36'
            elif i == 1:
                text["foreground"] = '#3c4e61'
            elif i == 2:
                text["foreground"] = '#8594a1'
            elif i == 3:
                text["foreground"] = '#a5b9c9'
            elif i == 4:
                text["foreground"] = '#FFFFFF'
            # - - 減速 - - #
            sleep(0.1)

    def wisper_e():
        global text
        for i in range(5):
            if i == 0:
                text["foreground"] = '#FFFFFF'
            elif i == 1:
                text["foreground"] = '#a5b9c9'
            elif i == 2:
                text["foreground"] = '#8594a1'
            elif i == 3:
                text["foreground"] = '#3c4e61'
            elif i == 4:
                text["foreground"] = '#1f2b36'
            # - - 減速 - - #
            sleep(0.1)

    while True:
        text.place(x=x_place, y=window_height/2, anchor=CENTER) # anchor=文字列  オフセットの位置を指定する
        wisper_s()
        sleep(2)
        wisper_e()
        try:
            text["text"] = str(tweets[textnum])
        except:
            text["text"] = "Exception handling message..."
            print("Exception handling message...")
        if textnum!=len(tweets)-1:
            textnum+=1
        else:
            textnum=0
            tweets = []
            tweets = trend_tweet()
            # ツイート取得数
            print("GET LENGTH: "+str(len(tweets)))

if __name__=="__main__":
    thread_1 = threading.Thread(target=thread)
    thread_1.start()

#--終了--#
root.mainloop()