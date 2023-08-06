<h1 align="center">𝙤𝙟𝙞𝙘𝙝𝙖𝙩.𝙥𝙮</h1>
<h2 align="center">𝑶𝒋𝒊𝒔𝒂𝒏 𝑵𝒂𝒏𝒄𝒉𝒂𝒕𝒕𝒆 (𝒐𝒋𝒊𝒄𝒉𝒂𝒕) 𝑮𝒆𝒏𝒆𝒓𝒂𝒕𝒐𝒓</h2>
  
## なんだこれは
Go製ツール[ojichat](https://github.com/greymd/ojichat)のPython移植版です

## 開発環境
Python 3.11  
*海外の方の利用を1ミリも想定していないため、docstringも含めすべて日本語で整備していますのでご了承ください。

## インストール
```sh
pip install ojichat-py
```
`ojichat`というパッケージもありますが別のパッケージですのでご注意ください。  
おじさんで環境が汚れるのが嫌な方は仮想環境でご利用ください。  

## 使い方
### CLI
```
Usage:
  ojichat [options]
Options:
  -h, --help        ヘルプを表示
  -V, --version     バージョンを表示
  -s, --seed <Any>  シード値を指定する
  -n, --name <Any>  女の子の名前を指定する(-1でランダム)
  -e <number>       絵文字/顔文字の最大連続数 [default: 4]
  -p <level>        句読点挿入頻度レベル [min:0, max:3] [default: 0]
  -q, --quiet       出力を結果のみにします  デバッグモードと併用不可
  -d, --debug       デバッグモード
  --json            結果をJSON形式で返す
std I/O:
  標準入力から入力があった場合、--nameを指定しても標準入力の値に上書きされます
  また、出力は結果のみが標準出力に出力されます
```
example:
```
基本
$ ojichat

ログを出さない
$ ojichat -q
->ハナチャン、今日もお仕事かな🎵😂出張で愛知に行ってきたよ(^_^)観光でも、行きたいなぁ😂モチロン、ハナチャントネ

JSONで出力する
$ ojichat -q --json
->{"name": "クレハ", "seed": 53304354378, "punc_level": 0, "emoji_num": 4,
   "message": "クレハチャン、お疲れ様〜🎵😋（笑）ちょっと電話できるかな❓（￣ー￣?）🤔❓このホテル🏨、クラブサンドイッチ🥪がオイシイんだって❗💗😊ｵﾚと一緒に行こうよ😘😃なんてね😘😃☀ "}

上の情報を元に名前だけ変更する
$ ojichat -q -n ミコ -s 53304354378 --json
->{"name": "ミコ", "seed": 53304354378, "punc_level": 0, "emoji_num": 4,
  "message": "ミコチャン、お疲れ様〜🎵😋（笑）ちょっと電話できるかな❓（￣ー￣?）🤔❓このホテル🏨、クラブサンドイッチ🥪がオイシイんだって❗💗😊ｵﾚと一緒に行こうよ😘😃なんてね😘😃☀ "}

名前だけをランダムに変更する
$ ojichat -q -n -1 -s 53304354378 --json
->{"name": "萌美", "seed": 53304354378, "punc_level": 0, "emoji_num": 4,
  "message": "萌美チャン、お疲れ様〜🎵😋（笑）ちょっと電話できるかな❓（￣ー￣?）🤔❓このホテル🏨、クラブサンドイッチ🥪がオイシイんだって❗💗😊ｵﾚと一緒に行こうよ😘😃なんてね😘😃☀ "}

標準入力から名前を渡す(ただし、PowerShellで日本語をパイプで渡すと文字化けします)
$ echo リン | ojichat
->リンちゃん、オッハー(^з<)❗お弁当のフレンチトースト🍞が美味しくて、それと一緒にリンちゃんのことも食べちゃいたいナ〜（笑）🎵😃♥なんちゃって💗😃☀

ランダムで出力したいときは空文字を渡します
$ echo "" | ojichat
カズホﾁｬﾝ、こんな遅い時間😤に何をしているのかな🤔⁉今日はもう寝ちゃったのかな(＃￣З￣)🛌（￣▽￣）😪ｵｼﾞｻﾝはプライベートで、カズホﾁｬﾝを癒やして（笑）😚あげたい😋って思ってるヨ😒😎💤(^^;;
```

### 組み込み
```python
from ojichat import OjichatGenerator

ojichat = OjichatGenerator()
# 戻り値はOjiMessageクラス
result = ojichat.generator()
print(result)

# 新たな文章を生成する
ojichat.reset()
result = ojichat.generator()

# 引数にTrueを与えると生成後にプロパティを初期値に戻せます
for i in range(10):
    print(ojichat.generator(True))

# 生成した文章の名前だけ変更する
result1 = ojichat.generator()
ojichat.set_props(name="ひな")
result2 = ojichat.generator()

# シード値で文章を固定しつつ名前をランダムに変更する
result1 = ojichat.generator()
ojichat.set_props(name=-1)
result2 = ojichat.generator()

# 生成した文章の名前だけ利用して新たな文章を生成する
result1 = ojichat.generator()
ojichat.set_props(name=result1.name, seed=-1)
result2 = ojichat.generator()

# インスタンス生成時にプロパティを渡す
ojichat = OjichatGenerator(name="れな")
result = ojichat.generator()

# 渡せる引数等はdocstringをご覧ください
```
### 注意事項
- 引数は基本的に本家を参考にしてますので[本家](https://github.com/greymd/ojichat)の説明も合わせてご覧ください。
- おじさんは一途なので本家の変更に追随していくつもりですが、おじさんは気まぐれでもあるので違う道を走り始めるかもしれません。
## 問い合わせ
[Twitter](https://twitter.com/__Charahiro)