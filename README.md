# tweeter
twitterキーワード検索（リアルタイム）
## ライブラリのインストール
```
pip install -r requirements.txt
```
## 設定
tweeter.pyファイルを開いて20~23行目にTwitterAPIキーをそれぞれ設定してください。
```
consumer_key='CONSUMER_KEY'
consumer_secret='CONSUMER_SECRET'
access_key='ACCESS_KEY'
access_secret='ACCESS_SECRET'
```
30行目に検索キーワードを設定してください。
```
trend_name = "キーワード exclude:retweets"
```
## 実行
python3のみ実行可能
```
python tweepy.py
```
